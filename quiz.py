# Define the initial questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    }
]

# Function to display a question and get the user's answer
def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").upper()
    while answer not in ["A", "B", "C", "D"]:
        answer = input("Invalid input. Please enter A, B, C, or D: ").upper()
    return answer

# Function to evaluate the answer and provide feedback
def evaluate_answer(question, answer):
    if answer == question["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The correct answer is {question['answer']}.")
        return False

# Function to add a new question
def add_question():
    question_text = input("Enter the question: ")
    options = []
    for option in ["A", "B", "C", "D"]:
        option_text = input(f"Enter option {option}: ")
        options.append(f"{option}. {option_text}")
    correct_answer = input("Enter the correct answer (A, B, C, or D): ").upper()
    while correct_answer not in ["A", "B", "C", "D"]:
        correct_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

    questions.append({
        "question": question_text,
        "options": options,
        "answer": correct_answer
    })
    print("Question added successfully!")

# Main quiz function
def quiz():
    score = 0
    for question in questions:
        answer = ask_question(question)
        if evaluate_answer(question, answer):
            score += 1
        print()  # Print a blank line for better readability
    
    print(f"Your final score is {score} out of {len(questions)}.")

# Function to display the main menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Take the Quiz")
        print("2. Add a New Question")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
