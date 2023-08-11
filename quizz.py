import random
import time


# Define the quiz questions and answers
quiz = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "Madrid", "Rome", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the largest continent in the world?",
        "answers": ["Asia", "Africa", "North America", "South America"],
        "correct_answer": "Asia"
    },
    {
        "question": "What is the smallest country in the world?",
        "answers": ["Monaco", "San Marino", "Liechtenstein", "Vatican City"],
        "correct_answer": "Vatican City"
    },
    {
        "question": "What is the highest mountain in the world?",
        "answers": ["K2", "Mount Everest", "Makalu", "Cho Oyu"],
        "correct_answer": "Mount Everest"
    },
    {
        "question": "What is the currency of Japan?",
        "answers": ["Yen", "Dollar", "Pound", "Euro"],
        "correct_answer": "Yen"
    }
]

# Define a function to randomize the order of the answer choices
def randomize_answers(answers):
    randomized_answers = answers.copy()
    random.shuffle(randomized_answers)
    return randomized_answers

# Define a function to administer the quiz
def administer_quiz():
    score = 0
    user_answers = []

    # Loop through each question in the quiz
    for i, question in enumerate(quiz):
        # Print the question number and the question
        print("Question", i+1, ":", question["question"])

        # Randomize the order of the answer choices
        randomized_answers = randomize_answers(question["answers"])

        # Print the answer choices
        for j, answer in enumerate(randomized_answers):
            print(j+1, ":", answer)

        # Get the user's answer
        user_answer = int(input("Enter your answer (1-4): "))
        user_answers.append( randomized_answers[int(user_answer)-1])
        
        # Check if the user's answer is correct
        if randomized_answers[int(user_answer)-1] == question["correct_answer"]:
            # Increment the score if the answer is correct
            score += 1
            
    # Print the user's final score
    print("You scored", score, "out of", len(quiz))
 
    # Save user's answers and score in a file
    with open("quiz_results.txt", "a") as f:
        f.write("Quiz results:\n\n")
        f.write("Date: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
        for i, question in enumerate(quiz):
            f.write("Question " + str(i+1) + ": " + question["question"] + "\n")
            f.write("User's answer: " +  user_answers[i] + "\n")
            f.write("Correct answer: " + question["correct_answer"] + "\n\n")
        f.write("User's score: " + str(score) + "/" + str(len(quiz)))
    
     
# Call the administer_quiz() function to start the quiz
administer_quiz()
