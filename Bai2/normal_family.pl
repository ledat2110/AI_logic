/* facts */
/*Level 0*/
parent(adam, woody).
parent(adam, rose).
parent(eva, woody).
parent(eva, rose).

/*Level 1*/
/*Batch 1*/
parent(peggy, amy).
parent(peggy, paige).

parent(woody, amy).
parent(woody, paige).

/*Batch 2*/
parent(rose, jack).
parent(rose, paul).

parent(george, jack).
parent(george, paul).

/*Level 2*/
/*Batch 1*/
parent(amy, alex).
parent(amy, tim).

parent(andrew, alex).
parent(andrew, tim).

/*Batch 2*/
parent(ashley, ginger).
parent(ashley, jackie).

parent(jack, ginger).
parent(jack, jackie).

/*Sex*/
male(adam).
male(woody).
male(george).
male(jack).
male(paul).
male(andrew).
male(alex).
male(tim).

female(eva).
female(peggy).
female(rose).
female(amy).
female(paige).
female(ashley).
female(ginger).
female(jackie).

/*Married*/
married(adam, eva).
married(eva, adam).

married(peggy, woody).
married(woody, peggy).

married(rose, george).
married(george, rose).

married(andrew, amy).
married(amy, andrew).

married(jack, ashley).
married(ashley, jack).

husband(X, Y) :- married(X, Y), male(X).
wife(X, Y) :- married(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
child(X, Y) :- parent(Y, X).
son(X, Y) :- parent(Y, X), male(X).
daughter(X, Y) :- parent(Y, X), female(X).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandmother(X, Z) :- parent(X, Y), parent(Y, Z), female(X).
grandfather(X, Z) :- parent(X, Y), parent(Y, Z), male(X).
grandchild(X, Z) :- parent(Z, Y), parent(Y, X).
grandson(X, Z) :- parent(Z, Y), parent(Y, X), male(X).
granddaughter(X, Z) :- parent(Z, Y), parent(Y, X), female(X).

sibling(X, Y) :- father(Z,X), mother(T,X),father(Z,Y),mother(T,Y), X\=Y.
brother(X, Y) :- sibling(X, Y),male(X).
sister(X, Y) :- sibling(X, Y),female(X).

aunt(X, Z) :- parent(Y,Z),sibling(X, Y),female(X).
uncle(X, Z) :- parent(Y,Z),sibling(X, Y),male(X).
niece(X, Y) :- (aunt(Y,X);uncle(Y,X)),female(X).
nephew(X, Y) :- (aunt(Y,X);uncle(Y,X)),male(X).


