name1 = input("Enter player 1: ")
print("Hello, " + name1 + ".")

name2 = input("Enter player 2: ")
print("Hello, " + name2 + ".")

score = 0
score1 = 0
score2 = 0
strScore1 = ""
strScore2 = ""

print("Enter score (-1 to end)\n")
while score != -1:
    score = input(name1 + ": ")
    if score == "-1":
        break
    score = int(score)
    score1 += score
    score = 0
    strScore1 = str(score1)
    print(name1 + " total score: " + strScore1)

    score = input(name2 + ": ")
    if score == "-1":
        break
    score = int(score)
    score2 += score
    score = 0
    strScore2 = str(score2)
    print(name2 + " total score: " + strScore2)

if score1 > score2:
    print(name1 + " WINS!!!  Total Score: " + strScore1)
else:
    print(name2 + " WINS!!!  Total Score: " + strScore2)

