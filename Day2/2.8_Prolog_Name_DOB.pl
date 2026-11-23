% Prolog: Database with Name and DOB (CO5)

dob(john, date(1990, 5, 12)).
dob(mary, date(1992, 8, 23)).
dob(alice, date(1988, 1, 30)).
dob(bob, date(1995, 11, 7)).

person_dob(Name, DOB) :- dob(Name, DOB).
born_in_year(Name, Year) :- dob(Name, date(Year, _, _)).
