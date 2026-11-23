% Prolog: Towers of Hanoi (CO2)

hanoi(1, Source, Target, _) :-
    format('Move disk from ~w to ~w~n', [Source, Target]).
hanoi(N, Source, Target, Aux) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Aux, Target),
    hanoi(1, Source, Target, Aux),
    hanoi(N1, Aux, Target, Source).
