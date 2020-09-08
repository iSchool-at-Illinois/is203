---
title: Sets and set operations
author: Dave Dubin
date: Fall, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# Rationale for this presentation

- We will encounter sets and set notation throughout the remainder of the semester.
- Sets are not just part of our toolkit; to mathematicians they represent the simplest possible type of object to accept on faith.

# From last time

1. Sets are abstract objects. That means they have no extension in time or space.
2. Mathematicians are concerned for certainty, and the weaknesses of our intuitions.
3. All proofs have a starting point: that which doesn't have to be proven.
4. Wallis defines a set as "any collection of objects, provided only
   that there is a well-defined rule, called the *membership law*, for
   determining whether a given object belongs to the set."
5. That membership law can be just an enumeration of the set elements.


# The membership relationship is accepted without proof or defintion.

- We use the $\in$ operator to relate an element to the set it belongs to.
- For example, $b \in \{a,b,c\}$
- Mathematicians need their foundations to rely on as little intuition as possible.
- So everything else is built up from this minimal, primitive, membership relation.
- We usually use a capital letter to denote a set and lower case letters for elements.

# From the membership relation we can define set identity

- Sets are defined by their elements, not their membership rules.
- That is to say, two sets with exactly the same elements are one and the same.
- $A = B$ if and only if for every $x, x \in A \leftrightarrow x \in B$.
- Set elements have no order, so $\{a, b, c, d\} = \{c, a, d, b\}$.

# Same elements means same set

- The property of being an odd integer less than 8 and greater than 2
  is different from the property of being a prime integer less than 8
  and greater than 2, because "being prime" and "being odd" are different
  properties.
- But the set of odd integers between 2 and 8 is the same as the set
  of primes between 2 and 8. This is not just any equivalence
  relationship: we're talking about only one set: $\{3, 5, 7\}$.
- The *empty set* or *null set* is denoted by $\emptyset$ and contains no elements.

# From the membership relation we can define a subset relationship

- If all the elements of set A are also elements of set B, then A is a *subset* of B.
- The subset relationship is different from the membership relationship.
- $A \subseteq B$ if and only if for every $x, x \in A \rightarrow x \in B$.
- A *proper subset* of $B$ is a subset of B that isn't identical with B.
- $A \subset B$ if and only if $A \subseteq B$ and $A \neq B$.

# From the membership relation we can define set union, intersection and complement
- Union: $A \cup B =_{def} \{x : x \in A$ or $x \in B\}$
- Intersection: $A \cap B =_{def} \{x : x \in A$ and $x \in B\}$
- Complement:  $\bar{A} =_{def} \{x : x \notin A\}$
- Relative Complement:  $A \setminus B =_{def} \{x : x \in A$ and $x \notin B\}$
- Sets with no elements in common are *disjoint*.

# Universal set

- We assume (with Wallis) that any set we mention is a subset of some *universal set* $U$, or some universe of discourse.
- $\bar{A} = U \setminus A$

# We can even define ordered sets in terms of basic sets

- The ordered set $\langle a,b \rangle$ is different from the ordered set $\langle b,a \rangle$.
- The ordered set $\langle a,b \rangle$ has the same information as $\{\{a\}, \{a,b\}\}$
- No one ever uses the second construction. The point is to demonstrate that the ordering relationship on the
  elements doesn't have to be accepted as primitive.

# Power sets

- The *power set* of any set $S$ is the set of all subsets of $S$, including $S$ itself and the empty set.
- $\mathcal{P}(A) = \{B : B \subseteq A\}$.








