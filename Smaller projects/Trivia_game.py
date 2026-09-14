import random

qs = {
    "How many disciples did Jesus have?": "12",
    "What did Jesus turn into wine?": "Water",
    "Is abortion wrong?": "Yes",
    "How many men did Samson end with a donkey bone?": "2000",
    "What apostle started the catholic church?": "Peter",
    "Is the Universe expanding?": "Yes",
    "Does the Universe have a beginning?": "Yes",
    "In how many days does it say that God created everything?": "6"
}

def python_trivia():
    qs_list = list(qs.keys())
    total_questions = 5
    score = 0
    
    sel = random.sample(qs_list, total_questions)
    for ind, question in enumerate(sel, 1):
        user = input(f"{ind}. {question}: ").lower().strip()
        if user == qs[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer is {qs[question]}.")
        
    
    print(f"You got {score} answers correct out of {total_questions} questions")
    

python_trivia()