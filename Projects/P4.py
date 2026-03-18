Question={
    "What is owner of Tesla?":"Elon Mask",
    "What is owner of OpenAI?":"Sam Altiman",
    "What is owner of Face book?":"Mark Zong",
    "What is owner of Apple?":"Tim cook",
    "What is owner of Microsoft?":"Bill Gates",
    "What is owner of Alpha?":"Sundar Pichai",
    "What is owner of SpaceX ?":"Elon Mask",
}

print("(: Wecome to Quiz :)")

status=input("Are you ready to start ??? (yes/ no)\n")
if status.lower() != "yes":
    quit()

print("(: Let's Go -> :)")

Num_correct=0

for k,v in Question.items():
    ans=input(k+" ")
    if (ans.lower() == v.lower()):
        print("=> 🤩 Your answer are correct")
        Num_correct+=1
    else:
        print("=> 😞 Your answer are wrong")   

if Num_correct >= (len(Question) / 2):
    print(f"=> 🫡  You passed because you got { ( Num_correct / (len(Question)) ) * 100 }%")

else:
    print(f"=> 😭  You failed because you got { ( Num_correct / (len(Question)) ) * 100 }%")

print( "=>🧜 Nums of correct answers "+ str(Num_correct) + " from "+ str(len(Question)) )
