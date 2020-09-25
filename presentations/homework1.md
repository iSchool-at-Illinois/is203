---
title: First homework example
author: Dave Dubin
date: Fall Semester, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{syllogism}  
  - \usepackage{mathtools}
---

# From the student code

University of Illinois Student Code

> A student is eligible for a medical withdrawal only when the following conditions have been met:
>
> 1. The student has experienced a physical or mental health condition
>    that significantly impacts their ability to function safely and/or
>    successfully as a member of the university community; 
> 2. The student requires time away from campus for the treatment of
>    said health condition;
> 3. The student is seeking a withdrawal from the semester in which they
>    are currently enrolled;
> 4. The student initiates the request on or before the last day of classes
>    for the term and has not taken any final exams; and
> 5. The student has documentation from a treating healthcare provider
>    attesting to and in support of the medical withdrawal.


Function and equivalence relations

Define set $E$ as the set of enrollment statuses $E = {g,p,d,w,a,z}$.
Define set $S$ as the set of University of Illinois students.
Define set $T$ as the set of all times.

Define relation $R \subseteq (S \times T \times E)$ where
$\langle s,t,e \rangle \in R$ if and only if student $s \in S$ at time
$t \in T$ has enrollment status $e \in E$.

Define relation $Q \subseteq (S \times $ \times T)$ where
$\langle r,s,t \rangle \in Q$ if and only if students $r,s \in S$ have the
same enrollment status at time $t \in T$, i.e.,
$\langle r,t,e \rangle \in R \wedge \langle s,t,e \rangle \in R$.

1. At any given time, a student has the same enrollment status as herself, so relation $Q$ is reflexive.
2. If students $r$ and $s$ have the same enrollment status at time $t$, then $\langle r,s,t \rangle \in Q$
   and $\langle s,r,t \rangle \in Q$, so $Q$ is symmetric.
3. If any three students have the same enrollment status at time $T$, then all three pairs of students with time $t$ will be elements of $Q$. Relation $Q$ is therefore transitive.
4. Since relation $Q$ is reflexive, symmetric, and transitive, it is an equivalence relation.
5. Every student has exactly one enrollment status at a given
   time. Relation $R$ is therefore a function with domain $(S \times T)$
   and codomain $E$.





- Define relation $Q \subseteq (S \times S \times T)$ where
  $\langle r,s,t \rangle \in Q$ if and only if students $r,s \in S$ have the
  same enrollment status at time $t \in T$, i.e.,
  $\langle r,t,e \rangle \in R \wedge \langle s,t,e \rangle \in R$.

# Function and equivalence relations

1. At any given time, a student has the same enrollment status as herself, so relation $Q$ is reflexive.
2. If students $r$ and $s$ have the same enrollment status at time $t$, then $\langle r,s,t \rangle \in Q$
   and $\langle s,r,t \rangle \in Q$, so $Q$ is symmetric.
3. If any three students have the same enrollment status at time $T$, then all three pairs of students with time $t$ will be elements of $Q$. Relation $Q$ is therefore transitive.
4. Since relation $Q$ is reflexive, symmetric, and transitive, it is an equivalence relation.
5. Every student has exactly one enrollment status at a given
   time. Relation $R$ is therefore a function with domain $(S \times T)$
   and codomain $E$.
