import random

def main():
#start a noble gas element guessing game
    print("Hello Boys!Guess the noble gas element from the periodic table.")
         
 #list down options, clues and messages for players if they guess it correct or not
    list = ["Nitrogen","Oxygen","Hydrogen","Iodine","Carbon"]
    x = random.choice(list)
    guess = None
        
    while x != guess:
            
            guess = str(input("Pick a noble gas element from the parodic table:"))
            if x == "Nitrogen":
                print("Clue: the chemical element with the symbol N and atomic number 7")
            elif x == "Oxygen":
                print("Clue: the chemical element with the symbol O and atomic number 8")
            elif x == "Hydrogen":
                print("Clue: the chemical element with the symbol H and atomic number 1")
            elif x == "Iodine":
                print("Clue: a chemical element with the symbol I and atomic number 53")
            elif x == "Carbon":
                print("Clue: a chemical element with the symbol C and atomic number 6")
           
            if x == guess:
                print ("Good job! You correct!")
            elif x != guess:
                print ("Oh no!, You Wrong")  
    
    
        
                
main()
            
            
           
          
           
    