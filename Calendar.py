#!/usr/bin/python
from rdflib import *
# import bibtexparser
import sys
import re

ttlfilename = str(sys.argv[1])

project = ""
newdefs = {}
dstring = ""
regex1 = re.compile(r"([^.]+)\.ttl")
mymatch = re.search(regex1,ttlfilename)
if mymatch:
        project = mymatch.group(1)

if project:
        cldrfilename = project + ".cldr"
        cldrfile = open(cldrfilename,"w")
        defsfilename = project + ".defs"
        defsfile = open(defsfilename,"w")

i203 = Namespace("http://courseweb.ischool.illinois.edu/is203/")
event = Namespace("http://purl.org/NET/c4dm/event.owl#")
tl = Namespace("http://purl.org/NET/c4dm/timeline.owl#")
dc = Namespace("http://purl.org/dc/terms/")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")

mygraph = ConjunctiveGraph()
mygraph.parse(ttlfilename,format="n3")


# 'Weeks' can be any time interval, they're just usually weeks.

wlist = []  # List of weeks
weekstart = {} # associate weeks with their starting date

for s in mygraph.subjects(RDF.type, i203.TimeInterval):
  for i in mygraph.objects(s,event.time):
    for a in mygraph.objects(i,tl.at):
      weekstart[str(a)] = s

deadlines = {}

for d in mygraph.subjects(RDF.type, i203.Deadline):
                            weekdue = duedate = adue = moodleiri = moodlealias = dlabel = alabel = ""
                            for o in mygraph.objects(d,RDFS.label):
                                    dlabel = str(o)
                            for o in mygraph.objects(d,i203.during):
                                    weekdue = o
                            for o in mygraph.objects(d,i203.date):
                                    duedate = str(o)
                            for o in mygraph.objects(d,i203.moodleIRI):
                                    moodleiri = str(o)
                            for o in mygraph.objects(d,i203.moodleAlias):
                                    moodlealias = str(o)
                            for a in mygraph.subjects(i203.hasDeadline,d):
                                    for o in mygraph.objects(a,RDFS.label):
                                            alabel = str(o)
                                    for o in mygraph.objects(a,i203.dueDate):
                                            adue = str(o)
                            if (weekdue in deadlines.keys()):
                                    deadlines[weekdue] += "- **" + duedate + ":** " + dlabel + ", " + alabel + "\n"
                            else:
                                    deadlines[weekdue] = "- **" + duedate + ":** " + dlabel + ", " + alabel + "\n"
                            newdefs[adue] = duedate
                            newdefs[moodlealias] = moodleiri                            


cldrfile.write("# Topic Schedule\n")

wlist = list(weekstart.keys())
wlist.sort()


for d in wlist:
  myweek = myconcept = required = weekdate = background  = ''
  for o in mygraph.objects(weekstart[d], RDFS.label):
    myweek = str(o)
  for o in mygraph.objects(weekstart[d], i203.date):
    weekdate = str(o)
  if weekdate:    
    cldrfile.write("\n")
    cldrfile.write("### " +  myweek + ": " + weekdate + "\n\n")
    if weekstart[d] in deadlines.keys():
      cldrfile.write(dstring + "" + deadlines[weekstart[d]] + "\n")
      cldrfile.write("\n")
    for s in mygraph.objects(weekstart[d],dc.subject):
      for p in mygraph.objects(s,skos.prefLabel):
        myconcept = str(p)
        for q in mygraph.objects(s,i203.backgroundReading):
          background = str(q)
        for r in mygraph.objects(s,i203.reqReading):
          required = str(r)
      cldrfile.write("#### Topic: " + myconcept + "\n\n")  
      rstring = "- **Required Readings:** "
      if required:
        cldrfile.write(rstring + " " + required + "\n")
        cldrfile.write("\n")
      dstring = ""
      bstring = "- **Further Background:** "
      if background:
        cldrfile.write(bstring + " " + background + "\n")
        cldrfile.write("\n")
      myconcept = background = required = ''

if newdefs:
        for k in newdefs.keys():
                defsfile.write("define(" + k + ", " + newdefs[k] + ")dnl\n")

          
cldrfile.close()
defsfile.close()
