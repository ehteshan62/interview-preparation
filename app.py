import random

# Sample interview questions for different categories
interview_questions = {
    'Technical': [
        "Explain object-oriented programming.",
        "What is the difference between a list and a tuple in Python?",
        "What is the importance of version control in software development?"
    ],
    'Behavioral': [
        "Tell me about a challenging situation you faced and how you handled it.",
        "Describe a time when you had to work in a team with conflicting opinions.",
        "How do you handle stress and pressure?"
    ],
    'General': [
        "Tell me about yourself.",
        "Why do you want to work for our company?",
        "What are your strengths and weaknesses?"
    ]
}

def get_random_question(category):
    return random.choice(interview_questions[category])

def mock_interview():
    print("Welcome to the Mock Interview Assistant!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's start the mock interview.\n")

    categories = list(interview_questions.keys())
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    category_index = int(input("Select a category (enter the number): ")) - 1
    selected_category = categories[category_index]

    num_questions = int(input("How many questions would you like to answer? "))
    
    print("\nStarting the interview...\n")
    
    for _ in range(num_questions):
        question = get_random_question(selected_category)
        input(f"Question: {question}\n(Press Enter to answer)\n")
        answer = input("Your Answer: ")
        print("Thank you for your response!\n")

    print("Mock interview completed. Good luck with your preparation!")

if __name__ == '__main__':
    mock_interview()
