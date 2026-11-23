% Prolog: Forward Chaining (CO5)

fact(raining).
fact(cloudy).

rule(wet_ground) :- fact(raining).
rule(carry_umbrella) :- fact(raining), fact(cloudy).
rule(stay_inside) :- fact(raining), fact(cold).

forward_chain :-
    (rule(X), \+ fact(X) -> assertz(fact(X)), forward_chain ; true).
