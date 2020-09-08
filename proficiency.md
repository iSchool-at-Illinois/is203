---
title: Discussion questions
author: IS203
date: Fall 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
  - \usecolortheme{lily}  
---

## Scheduling Assignment

Students assigned to project groups need to meet together. We wish to
book the smallest number of meeting rooms and times that we can, which
means scheduling meetings at the same time if possible.

If the students are identified by letter, and the groups by number,
what's the smallest number of rooms and times that we can book while
ensuring that no student will miss a meeting? Produce a timetable of
meeting times and places.

     1   2   3   4   5   6   7   8
--- --- --- --- --- --- --- --- --- 
 A   X   X           X
 B   X               X   X
 C   X                   X   X
 D                       X   X   X
 E           X               X   X
 F           X   X               X
 G       X   X   X
 H       X       X   X
 I               X   X           X
 J                   X   X       X

Table: Meeting times


## Measurement scales


Mohs Hardness Scale is an ordinal index that represents an empirical relation over the domain of minerals.
A tuple ${\langle}x,y\rangle$ is an element of the relation if mineral x scratches mineral y.

Let **sample 1** consist of equal quantities of Flourite and Apatite. Let **sample 2** consist of equal quantities
of Calcite and Orthoclase. In the spaces provided, write numeric values for an index that represents the empirical
relation equally well, but which falsifies the scale-free statement, "The mean hardness values of samples 1 and 2
are equal."

+----------------+--------------------+----------------------+
| Mineral        | Mohs Scale         | Your scale           |
+================+====================+======================+
| Talc           |        1           |                      |
+----------------+--------------------+----------------------+
| Gypsum         |        2           |                      |
+----------------+--------------------+----------------------+
| Calcite        |        3           |                      |
+----------------+--------------------+----------------------+
| Fluorite       |        4           |                      |
+----------------+--------------------+----------------------+
| Apatite        |        5           |                      |
+----------------+--------------------+----------------------+
| Orthoclase     |        6           |                      |
+----------------+--------------------+----------------------+
| Quartz         |        7           |                      |
+----------------+--------------------+----------------------+
| Topaz          |        8           |                      |
+----------------+--------------------+----------------------+
| Corundum       |        9           |                      |
+----------------+--------------------+----------------------+
| Diamond        |        10          |                      |
+----------------+--------------------+----------------------+


## Parents and artists

Consider the following argument:

- All fathers are parents.
- All artists are dreamers. ${\forall}x (Ax \rightarrow Dx)$
- Therefore all fathers of artists are parents of artists, and fathers of dreamers. ${\forall}x ({\exists}y (Fxy \wedge Ay) \rightarrow {\exists}wz((Pxw \wedge Aw) \wedge (Fxz \wedge Dz)))$

Is the argument valid, as worded in English? We have expressed the
second premise and the conclusion in first order logic. Write two
different translations of the first premise into logical form. Use only
the predicates shown; do not introduce any new ones or change the
number of arguments they take. Both formulas must capture the meaning
of first premise equally well, but your first formula should create a valid
argument when combined with the two shown. Your second translation
should produce an invalid argument when combined with the two shown.



## Friends at a party

Fifteen students attend a party. Is it possible that each attendee is friends with exactly three of the other attendees? If not, why not? If so, how so?

