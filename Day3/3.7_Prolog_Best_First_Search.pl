% Prolog: Best First Search (CO4)

edge(a, b, 1). edge(a, c, 4).
edge(b, d, 2). edge(b, e, 5).
edge(c, f, 1).
edge(d, g, 3). edge(e, g, 1).
edge(f, g, 4).

heuristic(a, g, 6). heuristic(b, g, 4). heuristic(c, g, 3).
heuristic(d, g, 2). heuristic(e, g, 1). heuristic(f, g, 2).
heuristic(g, g, 0).

best_first(Start, Goal, Path) :-
    bfs([[Start]], Goal, Path).

bfs([], _, _) :- fail.
bfs([[Goal | Rest] | _], Goal, [Goal | Rest]) :- !.
bfs([Path | Rest], Goal, Sol) :-
    Path = [Node | _],
    findall([Next, Node | RestPath],
            (edge(Node, Next, _), \+ member(Next, Path), RestPath = Path),
            Children),
    append(Rest, Children, NewOpen),
    sort_by_heuristic(NewOpen, Goal, Sorted),
    bfs(Sorted, Goal, Sol).

sort_by_heuristic(Open, Goal, Sorted) :-
    map_list_to_pairs(heur_key(Goal), Open, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

heur_key(Goal, [Node | _], H) :- heuristic(Node, Goal, H).
