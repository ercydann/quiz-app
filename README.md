# Python Quiz Game

A simple Python program that administers a quiz with multiple-choice questions. The program randomizes the order of answer choices, allows the user to answer each question, and provides a final score at the end of the quiz. User answers and quiz results are saved to a text file.

## Table of Contents

   -  Description
   -  Usage
   -  How It Works
   -  Sample Output
   -  License

## Description

This Python project implements a quiz game that presents the user with a set of multiple-choice questions. The questions are defined with associated answer choices, and the user's answers are compared against the correct answers to calculate the final score. The program also saves the user's answers and quiz results to a text file for future reference.

## Usage

1. Clone this repository to your local machine:
```bash
git clone https://github.com/ercydann/python-quiz-game.git
```	
2. Navigate to the project directory:
```bash	
cd python-quiz-game
```	
3. Run the quiz program:
```bash
python quiz_game.py
```
4. Follow the prompts to answer the quiz questions. After answering all questions, the program will display your final score and save the quiz results to a text file named quiz_results.txt.

## How It Works
The quiz game is implemented using Python and includes the following features:

- The quiz questions and answer choices are defined in the quiz list of dictionaries.
- The program randomizes the order of answer choices for each question using the randomize_answers function.
- The user's answers are collected and compared to the correct answers.
- The user's score is calculated based on the number of correct answers.
- The program saves the user's answers, correct answers, and final score to a text file.


## Sample Output
```yaml
Question 1: What is the capital of France?
1 : Madrid
2 : Paris
3 : Berlin
4 : Rome
Enter your answer (1-4): 2

Question 2: What is the largest continent in the world?
1 : Africa
2 : Asia
3 : North America
4 : South America
Enter your answer (1-4): 2

...
(Other questions and answers)
...

You scored 4 out of 5.
Quiz results saved to quiz_results.txt.
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.