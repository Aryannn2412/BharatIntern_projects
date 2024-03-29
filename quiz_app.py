def run_quiz(questions):
    score = 0

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        
        for j, option in enumerate(question['options'], 1):
            print(f"{j}. {option}")

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == question['correct_answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['correct_answer']}\n")

    print(f"You scored {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_questions = [
        {
            'question': 'What is the capital of India?',
            'options': ['Mumbai', 'Chennai', 'Delhi', 'Bihar'],
            'correct_answer': 'Delhi'
        },
        {
            'question': 'which Animal is knows as king of the jungle',
            'options': ['deer', 'Lion', 'Monkey', 'Elephant'],
            'correct_answer': 'Lion'
        },
        {
            'question': 'What is the name of shape with equal sides and vertices?',
            'options': ['Rectangle', 'Square', 'Triangle', 'Circle'],
            'correct_answer': 'Square'
        }
    ]

    run_quiz(quiz_questions)
