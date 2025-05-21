# Multiple Choice Questions

print("Welcome to the program!")

# Get user's name
name = input("What's your name? ")

print(f"Hello, {name}! Let's start the quiz.")

# Questions, options, and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Paris", "C) London", "D) Rome"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A) Leonardo da Vinci", "B) Michelangelo", "C) Raphael", "D) Caravaggio"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Saturn", "C) Jupiter", "D) Uranus"],
        "answer": "C"
    }
]

# Initialize score
score = 0

# Ask questions
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    answer = input("Choose your answer (A/B/C/D): ").upper()
    
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer is {q['answer']}")

# Print final score
print(f"\nQuiz over, {name}! Your final score is {score} out of {len(questions)}")
