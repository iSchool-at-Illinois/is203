---
title: Relations
author: Dave Dubin
date: Fall, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

The sources for my domain model are articles 2 (section 2-105) and 3 (section 3-110) of the University of Illinois Student Code, available online
at <https://studentcode.illinois.edu/>.

# Domain, codomain, functions, and composition.

- The set \textbf{dom} $R = \{a\ |\ \langle a,b \rangle \in R$ for some $b\}$ is called the \emph{domain}
  of the relation $R$ and \ldots
- \ldots the set \textbf{codom} $R = \{b\ |\ \langle a,b \rangle \in R$ for some $a\}$ is called the
   \emph{codomain} of relation $R$.
- If  $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R^{-1} \subseteq B \times A$ is the
  \emph{inverse} of $R$, where $R^{-1} =_{def} \{\langle b,a \rangle\ |\ \langle a,b \rangle \in R\}$.
- Given relations $R \subseteq A \times B$ and $S \subseteq B \times C$ the composite of $R$ and $S$,
  written $S \circ R =_{def} \{\langle x,z \rangle |$ for some $y, \langle x,y \rangle \in R$ and $\langle y,z \rangle \in S \}$
- A relation $F \subseteq A \times B$ is a \emph{function} (or mapping) $F:A \rightarrow B$ if and only if
  the domain of $F$ is $A$ and $F$ pairs every element in that domain with exactly one element in the codomain,
  i.e. $\langle a,b \rangle \in F$ and $\langle a,c \rangle \in F$ implies $b = c$.


- Define set $E$ as the set of enrollment statuses $E = \{g,p,d,w,a,z \}$.
- Define set $S$ as the set of University of Illinois students.
- Define set $T$ as the set of all times.
- Define relation $R \subseteq (S \times T \times E)$ where
  $\langle s,t,e \rangle \in R$ if and only if student $s \in S$ at time
  $t \in T$ has enrollment status $e \in E$.
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
