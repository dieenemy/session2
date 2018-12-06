print("Answer the following algebra question: ")

p_list = [
    {
        "questions" : {"1" : "If x = 8, then what is the value of 4(x + 3) ?"},
        "answers" : {
            "1. " : 35,
            "2. " : 36,
            "3. " : 40,
            "4. " : 44
        },
        "correct" : 4
},
{
        "questions" : {
            "1" : "Estimate this answer (exact calculation not needed): ",
            "2" : "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?",
        },
        "answers" : {
            "1. " : "About 55",
            "2. " : "About 65",
            "3. " : "About 75",
            "4. " : "About 85"
        },
        "correct" : 2
}
]
correct_answers = 0
for x in p_list:
    questions = x["questions"]
    answers = x["answers"]
    correct = x["correct"]
    for v in questions.values():
        print(v)
    for k,v in answers.items():
        print(k,v)
    n = int(input("Your choice: "))
    if n ==  correct:
        correct_answers += 1
        print("bingo")
    else:
        print(":(")
print("Your correctly answer", correct_answers, "out of 2 question")

    

  
