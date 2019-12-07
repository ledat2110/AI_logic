%Define parent relationship level 0, from left to right
parent(queen_elizabeth, prince_charles).
parent(queen_elizabeth, princess_anne).
parent(queen_elizabeth, prince_andrew).
parent(queen_elizabeth, prince_edward).

parent(prince_phillip, prince_charles).
parent(prince_phillip, princess_anne).
parent(prince_phillip, prince_andrew).
parent(prince_phillip, prince_edward).

%Define parent relationship level 1, from left to right
%Batch 1
parent(princess_diana, prince_william).
parent(princess_diana, prince_harry).

parent(prince_charles, prince_william).
parent(prince_charles, prince_harry).

%Batch 2
parent(captain_mark_phillips, peter_phillips).
parent(captain_mark_phillips, zara_phillips).

parent(princess_anne, peter_phillips).
parent(princess_anne, zara_phillips).

%Batch 3
parent(sarah_ferguson, princess_beatrice).
parent(sarah_ferguson, princess_eugenie).

parent(prince_andrew, princess_beatrice).
parent(prince_andrew, princess_eugenie).

%Batch 4
parent(sophie_rhys_jones, james).
parent(sophie_rhys_jones, lady_louise).

parent(prince_edward, james).
parent(prince_edward, lady_louise).

%Define parent relationship level 2, from left to right
%Batch 1
parent(prince_william, prince_george).
parent(prince_william, princess_charlotte).
parent(prince_william, prince_louis).

parent(kate_middleton, prince_george).
parent(kate_middleton, princess_charlotte).
parent(kate_middleton, prince_louis).

%Batch 2
parent(prince_harry, harrison).
parent(markle, harrison).

%Define sex
%male
male(prince_phillip).
male(prince_charles).
male(captain_mark_phillips).
male(timothy_laurence).
male(prince_andrew).
male(prince_edward).
male(prince_william).
male(prince_harry).
male(peter_phillips).
male(mike_tindall).
male(james).
male(prince_george).
male(harrison).

%female
female(queen_elizabeth).
female(princess_diana).
female(camilla_parker_bowles).
female(princess_anne).
female(sarah_ferguson).
female(sophie_rhys_jones).
female(kate_middleton).
female(autumn_kelly).
female(zara_phillips).
female(princess_beatrice).
female(princess_eugenie).
female(lady_louise).
female(princess_charlotte).
female(savannah_phillips).
female(isla_phillips).
female(markle).

%married
married(queen_elizabeth, prince_phillip).
married(prince_phillip, queen_elizabeth).

married(prince_charles, camilla_parker_bowles).
married(camilla_parker_bowles, prince_charles).


married(prince_harry, markle).
married(markle, prince_harry).

married(princess_anne, timothy_laurence).
married(timothy_laurence, princess_anne).

married(sophie_rhys_jones, prince_edward).
married(prince_edward, sophie_rhys_jones).

married(kate_middleton, prince_william).
married(prince_william, kate_middleton).

married(autumn_kelly, peter_phillips).
married(peter_phillips, autumn_kelly).

married(zara_phillips, mike_tindall).
married(mike_tindall, zara_phillips).

%married(Y, X) :- married(X, Y).

%divorced
divorced(princess_diana, prince_charles).
divorced(prince_charles, princess_diana).

divorced(captain_mark_phillips, princess_anne).
divorced(princess_anne, captain_mark_phillips).
%divorced(Y, X) :- divorced(X, Y).

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




