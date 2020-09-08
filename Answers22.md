---
title: Wallis Excercise 2.2 Answers
date: Fall, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amsfonts}
  - \usepackage{amssymb}
  - \usepackage{mathtools}
---

1. $A = \{a,b,c,d,e\}, B = \{a,c,e,g,i\}, C = \{c,f,i,e,o\}$
      i.   $A \cup B = \{a,b,c,d,e,g,i\}$
      ii.  $A \cap C = \{c,e\}$
      iii. $A \setminus B = \{b,d\}$
      iv.  $A \cup (B \setminus C) = \{a,b,c,d,e,g\}$
2. $A = \{2, 3, 5, 6, 8, 9\}, B = \{1, 2, 3, 4, 5\}, C = \{5, 6, 7, 8, 9\}$
      i.   $A \cap B = \{2, 3, 5\}$
      ii.  $A \cup C = \{2, 3, 5, 6, 7, 8, 9\}$
      iii. $A \setminus (B \cap C) = \{2, 3, 6, 8, 9\}$
      iv.  $(A \cup B) \setminus C = \{1, 2, 3, 4\}$
3. $A = \{1, 2, 4, 5, 6, 7\}, B = \{1, 3, 5, 7, 9\}, C = \{2, 4, 6, 7, 8, 9\}$
      i.   $A \cup B \cup C = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$
      ii.  $A \cup (B \cap C) = \{1, 2, 4, 5, 6, 7, 9\}$
      iii. $A \setminus C = \{1, 5\}$
      iv.  $A \cap (B \setminus C) = \{1, 5\}$
4. $A = \mathbb{Z}^{+}, B = \{-4, -2, 1, 3, 5, 7\}, C= \{x| x^2 = 1\}$
      i.   $(A \cap B) \cup C = \{-1, 1, 3, 5, 7\}$
      ii.  $A \cap B \cap C = \{1\}$
      iii. $C \setminus A = \{-1\}$
      iv.  $A \cap (B \setminus C) = \{3, 5, 7\}$
5. $S_1 = \{2, 5\}, S_2 = \{1, 2, 4\}, S_3 = \{1, 2, 4, 5, 10\}, S_4 = \{1, 2, 4, 5, 10, 20\}, S_5 = \{1, 2, 4\}$
      - $S_1 = S_1, S_1 \subseteq S_1, S_1 \subseteq S_3, S_1 \subseteq S_4$
      - $S_2 = S_2, S_2 \subseteq S_2, S_2 \subseteq S_3, S_2 \subseteq S_4, S_2 = S_5, S_2 \subseteq S_5$
      - $S_3 = S_3, S_3 \subseteq S_3, S_3 \subseteq S_4$
      - $S_4 = S_4, S_4 \subseteq S_4$
      - $S_5 \subseteq S_2, S_5 \subseteq S_3, S_5 \subseteq S_4, S_5 = S_5, S_5 \subseteq S_5$
6. Are sets $S$ and $T$ disjoint? If not, what is their intersection?
      i.   The intersection of $S$ and $T$ is the set of sixth powers $\{1, 64, 729, 15625, \ldots \}$.
      ii.  $S$ and $T$ are disjoint.
      iii. $S$ and $T$ are disjoint.
7. Are sets $S$ and $T$ disjoint? If not, what is their intersection?
      i.   The intersection of $S$ and $T$ is $\{x^2| x$ is a multiple of 5 $\} = \{25, 100, 225, \ldots \}$.
      ii.  The intersection of $S$ and $T$ is $S$.


23) $A = \{\emptyset\}, B = \{A\}, C = \{\emptyset, A\}, D = \{\emptyset, A, C\}, S = \{\emptyset, A, B, C, D\}$ Show that:

      i.    $\{x| x \in S$ and $x \subseteq D\} = S$;
          - $\{x| x \in S\} = S$ is true by definition, so it suffices to show that every element of $S$ is a subset of $D$.
	  - $\emptyset$ is a subset of $D$ because $\emptyset$ is a subset of every set.
	  - $A$ is a subset of $D$ because $A = \{\emptyset\}$ and $\emptyset \in D$.
	  - $B$ is a subset of $D$ because $B = \{A\}$ and $A \in D$.
	  - $C$ is a subset of $D$ because $C = \{\emptyset, A\}$ and both $\emptyset$ and $A$ are elements of $D$.
	  - $D$ is a subset of $D$ because every set is a subset of itself.
      ii.   $\{x| x \in S$ and $x \in D\} = D$;
          - $\{x| x \in S$ and $x \in D\}$ is by definition $S \cap D$.
	  - But every element of $D$ is also an element of $S$, so $D \subseteq S$.
	  - And for any sets $V$ and $T$, if $T \subseteq V$ then $T \cap V = T$.


In exercises 31-42, numbers 31, 32, 34, 37, 39, and 42 are true. The others are false.


