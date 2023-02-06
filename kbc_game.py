

# welcome to the game
print("*_ Welcome to KBC _*")

# getting user data

name = input("*** Enter your name : ")
age = int(input("*** Enter your age : "))
mobile_no = int(input("*** Enter your mobile no : "))
address = input("*** Enter your address : ")
print()

print("*** Please kindly read instructions !!!")
print("# Instructions : you have to write answers of a question\nor write its option number,any other thing considered as wrong answer")

print()

# getting user choice to play game

isPlay = input("*** Do you want to play KBC Game (y/n) : ")
isPlay = isPlay.lower()

# setting default difficulty
difficulty = "easy"

# winning amount
rupees = 0

# main game

if (isPlay == "yes" or isPlay == "y"):
    print("Select difficulty : ")
    print(" * Easy")
    print(" * Medium")
    print(" * Hard")
    print(" : ", end="")
    difficulty = input()
    difficulty = difficulty.lower()
    print()
    
    if (difficulty == "easy" or difficulty == "e" or difficulty == "1"):
        # easy level difficulty game

        # easy question 1 for rs 5000
        
        print("Q1. In the game of ludo the discs or tokens are of how many colours?")
        print()
        print("1) one\t\t\t", end="")
        print("2) two")
        print("3) three\t\t", end="")
        print("4) four")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "four" or choice == '4'):
            print()
            
            print("Congratulations!!! you won 5000 rs")
            rupees = 5000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # easy question 2 for rs 10000
        
        print("Q2. Which of these terms can only be used for women?")
        print()
        print("1) Dirghaayu\t\t", end="")
        print("2) Suhagan")
        print("3) Chiranjeevi\t\t", end="")
        print("4) Sushil")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "suhagan" or choice == '2'):
            print()
        
            print("Congratulations!!! you won 10000 rs")
            rupees = 10000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # easy question 3 for rs 20000
        
        print("Q3. Current Railway Minister of India is?")
        print()
        print("1) Mamta Banarjee\t\t", end="")
        print("2) Ram Vilash")
        print("3) Ashwini Vaishnaw\t\t", end="")
        print("4) Piyush Goyal")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "ashwini vaishnaw" or choice == '3'):
            print()
            
            print("Congratulations!!! you won 20000 rs")
            rupees = 20000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # easy question 4 for rs 40000
        
        print("Q4. Which god is also known as ‘Gauri Nandan’?")
        print()
        print("1) Agni\t\t", end="")
        print("2) Indra")
        print("3) Hanuman\t", end="")
        print("4) Ganesha")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "ganesha" or choice == '4'):
            print()
            
            print("Congratulations!!! you won 40000 rs")
            rupees = 40000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()
        # easy question 5 for rs 80000
        
        print("Q5. Which city is known as Pink City in India?")
        print()
        print("1) Banglore\t\t", end="")
        print("2) Maysore")
        print("3) Jaipur\t\t", end="")
        print("4) Kochi")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "jaipur" or choice == '3'):
            print()
            
            print("Congratulations!!! you won 80000 rs")
            rupees = 80000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

    
    # medium level game
    elif (difficulty == "medium" or difficulty == "m" or difficulty == "2"):
        
        # medium question 1 for rs 5000
        print("Q1. Which former Indian President died as a result of a road accident?")
        print()
        print("1) Rajendra Prasad\t\t\t", end="")
        print("2) Faqruddin Ali Ahmed")
        print("3) Giani Zail Singh\t\t\t", end="")
        print("4) R.Venkatraman")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "giani zail singh" or choice == '3'):
            print()
            
            print("Congratulations!!! you won 5000 rs")
            rupees = 5000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # medium question 2 for rs 10000
        
        print("Q2. Who was the first Indian woman to win a medal in the Olympics?")
        print()
        print("1) PT Usha\t\t\t", end="")
        print("2) Kunjarani Devi")
        print("3) Bachendri Pal\t\t", end="")
        print("4) Karnam Malleswari")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "karnam malleswari" or choice == '4'):
            print()
            
            print("Congratulations!!! you won 10000 rs")
            rupees = 10000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # medium question 3 for rs 20000
        
        print("Q3. The National Stadium in Delhi was earlier known by the name?")
        print()
        print("1) Irwin Stadium\t\t", end="")
        print("2) Mountbatten Stadium")
        print("3) Wellington Stadium\t\t", end="")
        print("4) Canning Stadium")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "irwin stadium" or choice == '1'):
            print()
            
            print("Congratulations!!! you won 20000 rs")
            rupees = 20000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # medium question 4 for rs 40000
    
        print("Q4. Which James Bond movie was shot in the Indian city of Udaipur?")
        print()
        print("1) Diamonds Are Forever\t\t", end="")
        print("2) License to Kill")
        print("3) Live and Let Die\t\t", end="")
        print("4) Octupussy")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "octupussy" or choice == '4'):
            print()
            
            print("Congratulations!!! you won 40000 rs")
            rupees = 40000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # medium question 5 for rs 80000
        # print(Fore.CYAN)
        print("Q5. Which Indian city hosts Indian movie industry?")
        print()
        print("1) Goa\t\t\t", end="")
        print("2) Mumbai")
        print("3) Chennai\t\t", end="")
        print("4) Calcutta")
        print()
        choice = input(" : ")
        choice = choice.lower()
        if (choice == "mumbai" or choice == '2'):
            print()
            
            print("Congratulations!!! you won 80000 rs")
            rupees = 80000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")
            
        # Hard level game start here!!!
    elif (difficulty == "hard" or difficulty == "h" or difficulty == "3"):
        # Hard question 1 for rs 5000
        
        print("Q1. In soccer, which part of midfielders body should not touch the ball?")
        print()
        print("1) Feet\t\t\t", end="")
        print("2) Chest")
        print("3) Hands\t\t", end="")
        print("4) Head")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "hands" or choice == '3'):
            print()
            
            print("Congratulations!!! you won 5000 rs")
            rupees = 5000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # Hard question 2 for rs 10000
        
        print("Q2. Which of these holy sites is located on an islet off the coast of Worli in Mumbai?")
        print()
        print("1) Nizamuddin Dargah\t\t", end="")
        print("2) Panchmai Pir")
        print("3) Hazi Ali\t\t\t", end="")
        print("4) Bande Nawaz Dargah")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "hazi ali" or choice == '3'):
            print()
            
            print("Congratulations!!! you won 10000 rs")
            rupees = 10000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # Hard question 3for rs 20000        
        
        print("Q3. What is celebrated on September 27 every year?")
        print()
        print("1) National Integration Day\t\t", end="")
        print("2) Teachers’ Day")
        print("3) International Literacy Day\t\t", end="")
        print("4) World Tourism Day")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "world tourism day" or choice == '4'):
            print()
            
            print("Congratulations!!! you won 20000 rs")
            rupees = 20000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # Hard question 4 for rs 40000
        
        print("Q4. The International Literacy Day is observed on?")
        print()
        print("1) Sep 8\t\t", end="")
        print("2) Nov 28")
        print("3) May 2\t\t", end="")
        print("4) Sep 22")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "sep 8" or choice == '1'):
            print()
            
            print("Congratulations!!! you won 40000 rs")
            rupees = 40000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")

        print()

        # Hard question 5 for rs 80000
        # print(Fore.CYAN)
        print("Q5. The wife of which of these famous sports persons was once captain of Indian volleyball team?")
        print()
        print("1) K.D.Jadav\t\t\t", end="")
        print("2) Dhyan Chand")
        print("3) Prakash Padukone\t\t", end="")
        print("4) Milkha Singh")
        print()
        choice = input(" : ")
        choice = choice.lower()

        if (choice == "milkha singh" or choice == '4'):
            print()
            # print(Fore.YELLOW)
            print("Congratulations!!! you won 80000 rs")
            rupees = 80000
        else:
            print("Sorry!!! you lose")
            exit("Better luck next time!!!")
    else:
        print("Invalid difficulty")
     
    

    # print(Fore.GREEN)
    print()
    print("*** Mr.", name)
    print(f"*** Congratulations !!! you won {rupees}")
    print("* Thanks for playing *")