% Prolog: Backward Chaining (CO1)

fact(raining).
fact(cloudy).

rule(wet_ground, [raining]).
rule(carry_umbrella, [raining, cloudy]).
rule(stay_inside, [raining, cold]).

prove(Goal) :- fact(Goal).
prove(Goal) :-
    rule(Goal, Conditions),
    prove_all(Conditions).

prove_all([]).
prove_all([H | T]) :- prove(H), prove_all(T).
