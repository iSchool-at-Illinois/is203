# Start by clearing the list of suffixes
.SUFFIXES:
# Then specify our suffixes
.SUFFIXES: .tex .dvi .bib .pdf .sgml .html .m4 .md

M4PATH := ./md
export M4PATH

%.md : %.m4 %.cldr %.defs IS203.m4 
	m4 -DFORMATDEFS="wpformat.m4" -DMOREDEFS="$*.defs" -DMYDEFS="$*.m4" IS203.m4 > $*.md

%.docx : %.md 
	pandoc -s -o $*.docx $*.md

%.bib : 
	cat currentReadings.bib > $*.bib

%.work : %.deadlines %.assignments
	cat $*.assignments $*.deadlines > $*.work

%.ttl : %.topics %.sched %.work turtlePrefixes currentCalendar
	cat turtlePrefixes currentCalendar $*.topics $*.sched $*.work > $*.ttl

%.cldr : %.ttl 
	 python3 Calendar.py $*.ttl

%.defs : %.ttl 
	 python3 Calendar.py $*.ttl


