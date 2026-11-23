% Prolog: Medical Diagnosis (CO4)

symptom(flu, fever). symptom(flu, cough). symptom(flu, body_ache).
symptom(cold, runny_nose). symptom(cold, sneezing). symptom(cold, sore_throat).
symptom(malaria, fever). symptom(malaria, chills). symptom(malaria, sweating).
symptom(covid, fever). symptom(covid, cough). symptom(covid, loss_of_smell).

diagnose(PatientSymptoms, Disease) :-
    symptom(Disease, S),
    member(S, PatientSymptoms).

strong_diagnosis(PatientSymptoms, Disease) :-
    findall(S, (symptom(Disease, S), member(S, PatientSymptoms)), Matches),
    length(Matches, N),
    N >= 2.
