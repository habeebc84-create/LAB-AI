% Prolog: Planets Database (CO2)

planet(mercury, rocky, 0.39, 0).
planet(venus, rocky, 0.72, 0).
planet(earth, rocky, 1.00, 1).
planet(mars, rocky, 1.52, 2).
planet(jupiter, gas_giant, 5.20, 79).
planet(saturn, gas_giant, 9.58, 83).
planet(uranus, ice_giant, 19.22, 27).
planet(neptune, ice_giant, 30.05, 14).

has_moons(P) :- planet(P, _, _, M), M > 0.
closer_than(P, D) :- planet(P, _, Dist, _), Dist < D.
