answers = {
    "wa'": "one",
    "cha'": "two",
    "wej": "three",
    "loS": "four",
    "vagh": "five",
    "jav": "six",
    "Soch": "seven",
    "chorgh": "eight",
    "Hut": "nine",
    "maH": "ten",
}
score = 0
print("Enter the corresponding English number word (ex: 'one', 'two', 'three', etc.)")
for i in answers:
    Answer = input(f"What is the equivalent of {i}: ")
    if Answer == answers[i]:
        print("Correct")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {answers[i]}")
if score/len(answers) >= .9:
    grade = "A"
elif score/len(answers) >= .8:
    grade = "B"
elif score/len(answers) >= .7:
    grade = "C"
elif score/len(answers) >= .6:
    grade = "D"
else:
    grade = "F"
print(f"Your final score is {score}/{len(answers)}")
print(grade)