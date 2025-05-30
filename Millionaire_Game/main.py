questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Elephant", "Whale", "Giraffe", "Rhino", 2],
    ["Who wrote 'Harry Potter'?", "J.R.R. Tolkien", "J.K. Rowling", "Mark Twain", "Charles Dickens", 2],
    ["What is the smallest prime number?", "0", "1", "2", "3", 3],
    ["Which language is used for web development?", "Python", "HTML", "C++", "Java", 2],
    ["What does CPU stand for?", "Central Processing Unit", "Control Power Unit", "Computer Primary Unit", "Central Print Unit", 1],
    ["Which gas do plants use to make food?", "Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen", 3],
    ["Which country is known for the Great Wall?", "India", "Japan", "China", "Korea", 3]
]

prizes =[1000000, 320000, 450000, 400000, 500000, 2000000, 3000000, 4000000, 6000000]

i=0
for question in questions:
    
     print(question[0])
     print(f"a.{question[1]}")
     print(f"b.{question[2]}")
     print(f"c.{question[3]}")
     print(f"d.{question[4]}")

     a= int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
     if(question[5]==a):
          print("Correct Answer")
     else:
       print(f"Incorrect, the correct answer was {question[5]}")
       print("Better luck next time!")
       break
   
     print(f"You won {prizes[i]}")
     i+=1