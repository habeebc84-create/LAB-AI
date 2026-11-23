% Prolog: Diet Suggestion System Based on Disease (CO3)

diet(diabetes, [vegetables, whole_grains, lean_protein], [sugar, refined_carbs]).
diet(hypertension, [fruits, vegetables, low_sodium], [salt, red_meat]).
diet(anemia, [spinach, red_meat, lentils], [tea, coffee]).
diet(obesity, [salad, fruits, grilled], [fried, sweets]).

suggest(Disease, Eat, Avoid) :- diet(Disease, Eat, Avoid).
