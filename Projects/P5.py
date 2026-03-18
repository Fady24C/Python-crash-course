from random import randint

words = ["w", "e", "a", "r", "s", "t", "o", "n", "g"]
rand_1=randint(0,len(words)-1)
Mycomp = words[rand_1]

limit=3
while (limit > 0) :
    print("---------------------------------------------------")
    print(f"⚠️  You have {limit} chances‼️‼️")
    You= input("Enter char from your guess for this sentence 'We are strong'???: ")
    if You.lower() != Mycomp:
        print("You are wrong‼️‼️")
        limit-=1
    else:
        print("You wins🏆🥇🏆")
        quit()

print(f"You lose😭😭😭 because the guess is {Mycomp}")
