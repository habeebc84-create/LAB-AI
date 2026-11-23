% Prolog: Monkey and Banana Problem (CO4)

initial(state(a, b, no, no)).
goal(state(_, _, _, yes)).

move(state(M, B, no, H), walk(NewLoc), state(NewLoc, B, no, H)) :- M \= NewLoc.
move(state(M, M, no, H), push(NewLoc), state(NewLoc, NewLoc, no, H)) :- M \= NewLoc.
move(state(M, M, no, H), climb, state(M, M, yes, H)).
move(state(c, c, yes, no), grasp, state(c, c, yes, yes)).

solve(State, []) :- goal(State).
solve(State, [Action | Rest]) :-
    move(State, Action, Next),
    solve(Next, Rest).
