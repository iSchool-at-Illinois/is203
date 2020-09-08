---
title: Propositional Logic
author: Dave Dubin
date: Fall Semester, 2020
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{amssymb}
  - \usepackage{syllogism}  
  - \usepackage{mathtools}
---

# Reasoning and representation

- With this topic we'll give some attention to logical reasoning and inference.
- The same rules that govern valid argumentation also enable information systems to answer interesting questions.
- Logic is also a means to describe a *domain* (some part of the world
  we're interested in).

# Differences in notation

- Both our authors explain how to construct logical expressions.
- Magnus uses '&' for 'and' while Wallis uses $\wedge$. I'll use $\wedge$.
- Wallis uses '~' for 'not' while Magnus uses $\neg$. I'll use $\neg$.
- Wallis uses lower case letters to represent propositions, while Magnus uses lower case. We'll use lower case letters.
- Wallis only uses parentheses to disambiguate the scope of an operator.
- Magnus insists on WFF rules that call for parentheses even where there's no ambiguity.
- We will follow Magnus's example and add parentheses according to the WFF rules.


# Differences in vocabulary

- Magnus says his capital letters represent 'sentences'
- Wallis says a proposition is 'a statement that has a truth value.'
- I say that propositions are language independent bearers of truth values.
- Think of them as the information content of simple declarative sentences.

# Different sentence, same proposition

1. "This table is made of wood."
2. "This is a wooden table."
3. "Ĉi tiu tablo estas el ligno."
4. "Jen ligna tablo."
5. "Dieser Tisch ist aus Holz."
6. "Dies ist ein Holztisch."


# Propositions, statements, sentences, and truth values

- There are two truth values: **true** and **false**.

- Propositions are the bearers of truth values: the kinds of things that can be
  true or false.

- States of affairs are arrangements of reality that make propositions true or false.

- We will model states of affairs using sets of proposition letters.


# Propositional logic

 - We represent propositions with lower case letters (typically $p, q,$ and $r$).
 - A set of proposition letters generates a set of states of affairs: ways the world might be.
 - $n$ proposition letters generate $2^n$ states of affairs.
 - $\{pqr,pq\overline{r},p\overline{q}r,p\overline{qr},\overline{p}qr,\overline{p}q\overline{r},\overline{pq}r,\overline{pqr}\}$

# Logical Operators

Symbol               In natural language   Technical name
------------------- --------------------- ---------------
$\neg$                       not                 negation
$\wedge$                     and              conjunction
$\vee$                       or               disjunction
$\rightarrow$              if ... then        implication
$\leftrightarrow$       if and only if        equivalence

# Logical Expressions

 - A sentence constructed from proposition letters and operators is true
   or false in each state of affairs.
 - Consider, for example: $(({\neg}p \vee q) \rightarrow r)$
 - The sentence is mapped to a truth value via the following tables

 
# Truth tables for the operators

  $\varphi$   $\neg\varphi$
 ----------- ---------------
      0            1
      1            0	

  $\varphi$   $\psi$   $\varphi \wedge \psi$   $\varphi \vee \psi$   $\varphi \rightarrow \psi$   $\varphi \leftrightarrow \psi$
 ----------- -------- ----------------------- --------------------- ---------------------------- -------------------------------- 
      0         0               0                       0                        1                         1                          
      0         1               0                       1                        1                         0                          
      1         0               0                       1                        0                         0                          
      1         1               1                       1                        1                         1                           

# From natural language to propositional logic

- "I will only go to school if I get a cookie now."
- Compare with "I will go to school if I get a cookie"
- The latter is cookie implies school, but the former is school implies cookie.
- You want $(s \rightarrow c)$
- Gloss: s =  "I will go to school" and c =  "I get a cookie."
- John and Mary are running
- $(j \wedge m)$
- A foreign national is entitled to social security if he has legal
  employment or if he has had such less than three years ago, unless
  he is currently also employed abroad.
- $(((e \vee l) \wedge {\neg}a) \rightarrow s)$
- $e =$ "A foreign national has legal employment."
- $l =$  "He has had legal employment less than three years ago."
- $a =$  "He is currently employed abroad."
- $s =$ "He is entitled to social security."

# Drawing truth tables for expressions

\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & 0 & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 1 & \textcolor{red}{1} & \\
1 & 1 & 0 &  &  & 0 & \textcolor{red}{1} & 1 & \textcolor{red}{1} &  & 0 & \textcolor{red}{0} & \\
1 & 0 & 1 &  &  & 0 & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & \textcolor{red}{1} & \\
1 & 0 & 0 &  &  & 0 & \textcolor{red}{1} & 0 & \textcolor{red}{0} &  & 1 & \textcolor{red}{0} & \\
0 & 1 & 1 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 1 & \textcolor{red}{1} & \\
0 & 1 & 0 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{1} &  & 0 & \textcolor{red}{0} & \\
0 & 0 & 1 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 1 & \textcolor{red}{1} & \\
0 & 0 & 0 &  &  & 1 & \textcolor{red}{0} & 1 & \textcolor{red}{0} &  & 0 & \textcolor{red}{0} & \\
\end{tabular}

# Drawing truth tables for expressions

\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 1 & 1 &  & 1 & 1 & \\
1 & 1 & 0 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 1 & 1 &  & 0 & 0 & \\
1 & 0 & 1 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 0 & 0 &  & 1 & 1 & \\
1 & 0 & 0 &  &  & \textcolor{red}{0} & \textcolor{green}{1} & 0 & 0 &  & 1 & 0 & \\
0 & 1 & 1 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 1 &  & 1 & 1 & \\
0 & 1 & 0 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 1 &  & 0 & 0 & \\
0 & 0 & 1 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 0 &  & 1 & 1 & \\
0 & 0 & 0 &  &  & \textcolor{red}{1} & \textcolor{green}{0} & 1 & 0 &  & 0 & 0 & \\
\end{tabular}


# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{1} & \textcolor{green}{1} &  & 1 & 1 & \\
1 & 1 & 0 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{1} & \textcolor{green}{1} &  & 0 & 0 & \\
1 & 0 & 1 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{0} & \textcolor{green}{0} &  & 1 & 1 & \\
1 & 0 & 0 &  &  & \textcolor{green}{0} & 1 & \textcolor{red}{0} & \textcolor{green}{0} &  & 1 & 0 & \\
0 & 1 & 1 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{1} &  & 1 & 1 & \\
0 & 1 & 0 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{1} &  & 0 & 0 & \\
0 & 0 & 1 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{0} &  & 1 & 1 & \\
0 & 0 & 0 &  &  & \textcolor{green}{1} & 0 & \textcolor{red}{1} & \textcolor{green}{0} &  & 0 & 0 & \\
\end{tabular}


# Drawing truth tables for expressions


\begin{tabular}{@{ }c@{ }@{ }c@{ }@{ }c | c@{}@{}c@{}@{ }c@{ }@{ }c@{ }@{ }c@{ }@{ }c@{ }@{}c@{}@{ }c@{ }@{ }c@{ }@{}c@{ }}
p & q & r & ( & ( & $\neg$ & p & $\vee$ & q & ) & $\rightarrow$ & r & )\\
\hline 
1 & 1 & 1 &  &  & 0 & 1 & \textcolor{green}{1} & 1 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
1 & 1 & 0 &  &  & 0 & 1 & \textcolor{green}{1} & 1 &  & \textcolor{red}{0} & \textcolor{green}{0} & \\
1 & 0 & 1 &  &  & 0 & 1 & \textcolor{green}{0} & 0 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
1 & 0 & 0 &  &  & 0 & 1 & \textcolor{green}{0} & 0 &  & \textcolor{red}{1} & \textcolor{green}{0} & \\
0 & 1 & 1 &  &  & 1 & 0 & \textcolor{green}{1} & 1 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
0 & 1 & 0 &  &  & 1 & 0 & \textcolor{green}{1} & 1 &  & \textcolor{red}{0} & \textcolor{green}{0} & \\
0 & 0 & 1 &  &  & 1 & 0 & \textcolor{green}{1} & 0 &  & \textcolor{red}{1} & \textcolor{green}{1} & \\
0 & 0 & 0 &  &  & 1 & 0 & \textcolor{green}{1} & 0 &  & \textcolor{red}{0} & \textcolor{green}{0} & \\
\end{tabular}



# Grammar of propositional logic

Let $P$ be a set of proposition letters and let $p \in P$. 

The following expression defines the recursive grammar for a logical
expression $\varphi$ in [Backus–Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form):

$\varphi \Coloneqq p|\neg\varphi|(\varphi \wedge \varphi)|(\varphi \vee \varphi)|(\varphi \rightarrow \varphi)|(\varphi \leftrightarrow \varphi)$

# Syntactically conforming expressions

Let $P = \{o,q,r,s\}$



Examples of grammatically conforming expressions include:

- $r$
- ${\neg}q$
- $(s \leftrightarrow o)$
- $({\neg}(s \leftrightarrow \neg\neg{\neg}o) \rightarrow (q \wedge q))$

Grammatically *incorrect* expressions would include:

- $\neg\vee p$ 
- $\vee ) p \neg$
- ${\neg}p \vee q \rightarrow r$ 

How many correct expressions are consistent with the last one?

# Syntactic ambiguity

These conforming expressions are all consistent with ${\neg}p \vee q \rightarrow r$

- $(({\neg}p \vee q) \rightarrow r)$
- $({\neg}(p \vee q) \rightarrow r)$
- ${\neg}((p \vee q) \rightarrow r)$
- $({\neg}p \vee (q \rightarrow r))$
- ${\neg}(p \vee (q \rightarrow r))$


# Well-formed formulas

Which of the following are formulas in propositional logic?

- $p \rightarrow {\neg}q$
- ${\neg}{\neg} \wedge q \vee p$
- $p{\neg}q$

# Logical truth and logical falsity.

- A statement $\varphi$ is logically true if it is true in every state of
  affairs generated by its propositional variables.

- A statement $\varphi$ is logically false if it is false in every state of
  affairs generated by its propositional variables.

- If a statement $\varphi$ is neither logically true or logically false then
  it is contingent.

- Examples:
    1. $(q \vee {\neg}q)$ is logically true.
    2. $(q \wedge {\neg}q)$ is logically false.

# Consistency

- A set of propositional logic statements is consistent if
  at least one state of affairs satisfies every statement in 
  the set.

- A set of propositional logic statements is inconsistent if
  no state of affairs satisfies every statement in 
  the set.

# Inference and validity

- A conclusion is \emph{valid} with respect to a set of premises if the conclusion
  is true in every sitation where the premises are true.
- One can validly infer a conclusion $\varphi$ from a set of premises
  $P$ if the negation of $\varphi$ is inconsistent with the set of statements
  $P$.


# Computation and expressive power

1. Computing a truth value for a formula takes linear time.
2. Computing a truth table for validity takes exponential time.
3. The problem of testing for validity in propositional logic is
   decidable: there exists a mechanical method that computes the
   answer, at least in principle.