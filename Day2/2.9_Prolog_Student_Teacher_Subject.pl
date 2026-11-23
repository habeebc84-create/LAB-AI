% Prolog: Student - Teacher - Subject Code (CO1)

teaches(teacher1, math101).
teaches(teacher2, physics101).
teaches(teacher3, cs101).

enrolled(student1, math101).
enrolled(student2, physics101).
enrolled(student3, cs101).
enrolled(student1, cs101).

student_teacher(Student, Teacher) :-
    enrolled(Student, Subject),
    teaches(Teacher, Subject).

subject_of(Student, Subject) :-
    enrolled(Student, Subject).
