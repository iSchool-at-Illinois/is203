---
title: Relations and logic homework example
author: Dave Dubin
date: Fall, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---



The sources for my domain model are articles 2 (section 2-105) and 3 (section 3-110) of the University of Illinois Student Code, available online
at <https://studentcode.illinois.edu/>.

### Part 2: a relation that's not an equivalence relation

I begin by modeling the relationship between University of Illinois
students and their enrollment statuses on September 25, 2020.

- Define $U$ our universe of discourse as the University of Illinois students and enrollment statuses at 9:00 AM Central Time on 09/25/2020.
- Define set $E$ as the set of enrollment statuses $E = \{g,p,d,w,a,z\}$. The element g = 'good standing,' p = 'academic parole,' d = 'dropped,' w = 'withdrawn,' a = 'alumni,' and z = 'not yet enrolled.'
- Define set $S \subseteq U$ as the set of University of Illinois students on 09/25/2020.
- Define relation $R \subseteq (S \times E)$ where $\langle s,t,e
  \rangle \in R$ if and only if student $s \in S$ has enrollment status $e \in E$.

Students are not enrollment statuses, so sets $E$ and $S$ are
disjoint. Since there can be no overlap between the domain and range
of $R$, relation $R$ cannot be reflexive, symmetric, or transitive. It is not an equivalence relation

### Part 1: an equivalence relation

- Define relation $Q \subseteq (S \times S)$ where
  $\langle r,s \rangle \in Q$ if and only if students $r,s \in S$ have the same
  enrollment status on 09/25/2020.
  That is to say, $(\langle r,e \rangle \in R) \wedge (\langle s,e \rangle \in R)$.
- Another way to define the same relation is $Q = R \circ R^{-1}$. That is to say,
  $Q$ is the composition of $R$ with the inverse of $R$.

$Q$ is an equivalence relation because:

1. At any given time, a student has the same enrollment status as herself, so relation $Q$ is reflexive.
2. If students $r$ and $s$ have the same enrollment status, then $\langle r,s, \rangle \in Q$ and $\langle s,r, \rangle \in Q$, so $Q$ is symmetric.
3. If any three students have the same enrollment status, then all three pairs of students will be elements of $Q$. Relation $Q$ is therefore transitive.

### Part 3: a function

Relation $Q$ is not a function, because any student will share the
same enrollment status with many others. An element of the domain will
not be mapped to a unique element of the codomain. But at 9:00 AM on
September 25, 2020, each student in $S$ had exactly one of the six
statuses in set $E$. Relation $R$ is therefore a function from
$S \rightarrow E$.

### Ternary relations

If I wanted to extend my universe of discourse to all times, I could:

- Define set $T$ as the set of all times.
- Define relation $R \subseteq (S \times T \times E)$ where $\langle
  s,t,e \rangle \in R$ if and only if student $s \in S$ at time $t \in
  T$ has enrollment status $e \in E$.
- Define relation $Q \subseteq (S \times S \times T)$ where
  $\langle r,s,t \rangle \in Q$ if and only if students $r,s \in S$ have the
  same enrollment status at time $t \in T$, i.e.,
  $(\langle r,t,e \rangle \in R) \wedge (\langle s,t,e \rangle \in R)$.


### Part 4: two domain rules

From section 2-105 of the Student Code:

A student is eligible for a medical withdrawal only when the following conditions have been met:

1. The student has experienced a physical or mental health condition that significantly impacts their ability to function safely and/or successfully as a member of the university community;
2. The student requires time away from campus for the treatment of said health condition;
3. The student is seeking a withdrawal from the semester in which they are currently enrolled;
4. The student initiates the request on or before the last day of classes for the term and has not taken any final exams; and
5. The student has documentation from a treating healthcare provider attesting to and in support of the medical withdrawal.

Define the following propositions:

- e = 'A student is eligible for medical withdrawal.'
- p = 'The student has experienced a physical health condition.'
- m = 'The student has experienced a mental health condition.'
- j = 'The health condition significantly impacts the student's ability to function safely in the university community.'
- k = 'The health condition significantly impacts the student's ability to function successfully in the university community.'
- t = 'The student requires time away from campus for treatment of the health condition.'
- w = 'The student seeks a withdrawal from the semester in which they are currently enrolled.'
- r = 'The student has requested a withdrawal on or before the last day of classes in the semester.'
- f = 'The student has taken at least one final exam this semester.'
- c = 'The student has documentation from a treating healthcare provider attesting to the medical condition.'
- d = 'The student has documentation from a treating healthcare providor in support of medical withdrawal.'

The rule is expressed as an 'only if' implication, so we must interpret the requirements as necessary, but not sufficient. The logical form of this
rule is therefore $(e \rightarrow ((((((((p \vee m) \wedge (j \vee k)) \wedge t) \wedge w) \wedge r) \wedge \neg f) \wedge c) \wedge d))$

From section 3-110 of the Student Code:

A student on probation who fails to meet his or her established
probation level is dropped unless the student has achieved at least a
2.0 average or better for that semester and his or her cumulative
average is at least 2.0.

Define the following propositions:

- p = 'The student is currently on probation.'
- e = 'The student has met his or her established probation level.'
- d = 'The student is dropped.'
- a = 'The student has achieved a grade point average of at least 2.0 for the current semester.'
- b = 'The student has a cumulative grade point average of at least 2.0.'

This rule is expressed using an 'unless' clause, so the logical form of the rule is $(((p \wedge \neg e) \wedge \neg (a \wedge b)) \rightarrow d)$.