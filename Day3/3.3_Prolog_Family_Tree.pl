% Prolog: Family Tree (CO3)

male(john). male(bob). male(tom). male(sam).
female(mary). female(alice). female(sue).

parent(john, bob). parent(john, alice).
parent(mary, bob). parent(mary, alice).
parent(bob, tom). parent(bob, sue).
parent(alice, sam).

father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(B, S) :- male(B), sibling(B, S).
sister(S, B) :- female(S), sibling(S, B).
grandparent(G, C) :- parent(G, P), parent(P, C).
grandfather(G, C) :- male(G), grandparent(G, C).
grandmother(G, C) :- female(G), grandparent(G, C).
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).
