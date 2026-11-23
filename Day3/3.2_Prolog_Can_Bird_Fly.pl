% Prolog: Can a Bird Fly? (CO3)

bird(eagle). bird(sparrow). bird(penguin). bird(ostrich). bird(parrot).
flightless(penguin). flightless(ostrich).
can_fly(B) :- bird(B), \+ flightless(B).
