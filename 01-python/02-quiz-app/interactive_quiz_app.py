# Data



questions = [
    "Which keyword is used to define a function in Python?",
    "Which data type is immutable in Python?",
    "What is the output of 10 // 3?",
    "Which method adds an element to the end of a list?",
    "Which symbol is used for comments in Python?"
]

options = [
    ["A. function", "B. def", "C. fun", "D. define"],
    ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
    ["A. 3.33", "B. 3", "C. 4", "D. 1"],
    ["A. add()", "B. insert()", "C. append()", "D. extend()"],
    ["A. //", "B. <!-- -->", "C. #", "D. **"]
]

correct_answers = [
    "B",
    "D",
    "B",
    "C",
    "C"
]


print("========== PYTHON QUIZ ==========")

total_questions = len(questions)
correct_answers_count = 0
wrong_answers_count = 0

for i, (question, option, correct_answer) in enumerate(zip(questions, options, correct_answers)):
    print(f"\nQuestion {i + 1}:")
    print(f"{question}")
    for op in option:
        print(op)
    entered_answer = input("Enter your answer: ").strip().upper()

    if entered_answer == correct_answer:
        print("\nCorrect answer!")
        correct_answers_count += 1
    else:
        wrong_answers_count += 1
        print("\nWrong answer!")
        correct_option = next(op for op in option if op.startswith(correct_answer + "."))
        print(f"Correct answer: {correct_option}")

final_score = (correct_answers_count / total_questions) * 100

print(f"\nTotal questions: {total_questions}")
print(f"Correct answers: {correct_answers_count}")
print(f"Wrong answers: {wrong_answers_count}")
print(f"Final Score: {final_score}%")


