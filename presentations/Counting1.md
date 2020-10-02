---
title: Counting
author: from Alan Tucker's *Applied Combinatorics*
date: Fall, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

# The addition principle

If there are $r_{1}$ different objects in the first set, $r_{2}$
objects in the second set, \ldots and $r_{m}$ objects in the mth set,
and if the different sets are disjoint, then the number of ways to
select an object from one of the m sets is $r_{1} + r_{2} + \ldots + r_{m}$.

# The multiplication principle

Suppose a procedure can be broken into m successive (ordered) stages, with
$r_{1}$ outcomes in the first stage, $r_{2}$ outcomes in the second stage,
\ldots , and $r_{m}$ outcomes in the mth stage. If the composite outcomes are all distinct, then the total procedure has
$r_{1} \times r_{2} \times  \ldots \times r_{m}$ different composite outcomes.

# Permutations

A *permutation* of *n* distinct objects is an arrangement, or
ordering, of the *n* objects. An *r-permutation* of
*n* distinct objects is an arrangement using *r* of the *n* objects. An *r-combination* of *n* distinct objects is an unordered selection or subset of *r* out of the *n* objects. We use $P(n,r)$ and $C(n,r)$ to denote the number of r-permutations and r-combinations, respectively, of a set of n objects.

# Formulas

$P(n,n) = n!$

$P(n,r) = \frac{n!}{(n-r)!}$

$C(n,r) = \frac{P(n,r)}{P(r,r)} = \frac{n!}{r!(n-r)!}$

$C(n,r)$ is sometimes written $\binom{n}{r}$

