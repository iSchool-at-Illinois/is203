---
title: Relations
author: Dave Dubin
date: Fall, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Tuples are ordered sets

- $\langle a,b \rangle =_{def} \{\{a\},\{a,b\}\}$
- $\langle a,b,c \rangle =_{def} \langle\langle a,b \rangle,c\rangle$
- Cartesian products are sets of tuples.
- $A \times B =_{def} \{\langle x,y \rangle\ |\ x \in A\ and\ y \in B\}$
- Relations are subsets of cartesian products.
- If $A$ and $B$ are sets and $R \subseteq A \times B$ we say that $R$ is a binary relation from $A$ to $B$.
- $A \times B \times C =_{def} ((A \times B) \times C)$


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


# From sets to relations
- Suppose, for example, our domain ($\Delta$) includes things that are
  courses, course sections, students, and instructors.
- Define $C, E, I, O, P, S \subseteq \Delta$ as the sets of courses,
  events, instructors, course sections (offerings), persons, and students, respectively.
- $I \subseteq P$, $S \subseteq P$, $O \subseteq E$

# From relations to relationships

- We can model relationships in the world as relations between two or more sets.
- For example, define the "has section" relationship $H \subseteq (C \times O)$
- Let $a, b, c, d$ represent IS101, IS203, Fa2020-IS101-OA, and
  Fa2020-IS203-OA, respectively.
- $\langle a, c \rangle \in (C \times O), \langle a, d \rangle \in (C \times O), \langle b, c \rangle \in (C \times O), \langle b, d \rangle \in (C \times O)$
- $\langle a, c \rangle \in H$ but $\langle a, d \rangle \notin H$
- $\langle b, d \rangle \in H$ but $\langle b, c \rangle \notin H$

# Properties of relations

- A relation $R$ on set $A$ is *reflexive* if every element of $A$ stands in relation $R$ with itself.
- A relation $R$ on set $A$ is *symmetric* if over the cartesian product $A \times A$,
  $(\langle x,y \rangle) \rightarrow (\langle y,x \rangle)$
- A relation $R$ on set $A$ is *transitive* if over the cartesian product $A \times A$,
  $(\langle x,y \rangle \wedge \langle y,z \rangle) \rightarrow (\langle x,z \rangle)$
- These properties apply to relations where the domain and codomain are the same set.
- A relation that is reflexive, symmetric, and transitive is called an *equivalence relation*.

# Function and equivalence relations

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
