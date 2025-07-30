print("Welcome to the KBC")
questions = [
    ["what is the capital of India?","Jaipur","Delhi","Mumbai","Bangalore",2],
    ["what is the capital of USA?","New York","Washington D.C.","Los Angeles","Chicago",1],
    ["Who invented the light bulb?","Thomas Edison","Nikola Tesla","Alexander Graham Bell","Albert Einstein",1],
    ["What is the largest ocean on Earth?","Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean",4],
    ["What is the smallest country in the world?","Vatican City","Monaco","San Marino","Liechtenstein",1],
    ["Who wrote the national anthem of India?","Rabindranath Tagore","Bankim Chandra Chatterjee","Sarojini Naidu","Vande Mataram",1],
    ["What is the largest planet in our solar system?","Earth","Mars","Jupiter","Saturn",3],
    ["What is the chemical symbol for gold?","Au","Ag","Fe","Hg",1],
    ["What is the capital of France?","Berlin","Madrid","Paris","Rome",2],
    ["What is the largest mammal?","Elephant","Blue Whale","Giraffe","Orca",2],
    ["What is the longest river in the world?","Amazon River","Nile River","Yangtze River","Mississippi River",2],
    ["Who painted the Mona Lisa?","Vincent van Gogh","Pablo Picasso","Leonardo da Vinci","Claude Monet",3],
    ["What is the hardest natural substance on Earth?","Diamond","Gold","Iron","Platinum",1],
    ["What is the capital of Japan?","Seoul","Beijing","Tokyo","Kyoto",3],
    ["Who discovered penicillin?","Marie Curie","Alexander Fleming","Louis Pasteur","Joseph Lister",2],
    ["What is the largest desert in the world?","Sahara Desert","Arabian Desert","Gobi Desert","Kalahari Desert",1],
    ["What is the main ingredient in guacamole?","Tomato","Avocado","Onion","Pepper",2]
]
stages= [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 40000000]
money=0
i=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question {i+1}: {question[0]}")
    print(f"1. {question[1]}       2. {question[2]}")
    print(f"3. {question[3]}       4. {question[4]}")
    answer = input("Enter your answer (1/2/3/4 or 0 to quit): ")
    if answer == "0":
        print("You chose to quit.")
        print ("You won", stages[i-1])
        break
    if answer == str(question[5]):
        print("Correct! you won", stages[i])
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
        elif(i==17):
            money=40000000
    else:
        print("Wrong!")
        print("You won", money)
        break
print("Thank you for playing KBC!")