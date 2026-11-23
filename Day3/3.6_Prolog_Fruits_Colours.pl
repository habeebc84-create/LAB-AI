% Prolog: Fruits and Colours using Backtracking (CO4)

fruit(apple). fruit(banana). fruit(cherry). fruit(grape).
color(red). color(yellow). color(red). color(purple).

pair(F, C) :- fruit(F), color(C).
fruit_of_color(Color, Fruit) :- fruit(Fruit), pair(Fruit, Color).

assign([], []).
assign([F | Fs], [C | Cs]) :-
    color(C),
    \+ member(C, Cs),
    assign(Fs, Cs).
