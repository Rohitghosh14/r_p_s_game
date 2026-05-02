# import random


# user_win = 0 
# pc_win = 0
# draw_match = 0

# op = ["rock","paper","scissors"]        #---->#rock = 0,paper = 1,scissors = 2



# while True:
#     user_input = input("Enter (rock/paper/scissors)or(exit/x)!!: ").lower()
#     if user_input in ["exit", "x"]:
#         break
#     elif user_input not in op:
#         print("Please enter a valid input!!")
#         continue
    
#     random_num = random.randint(0,2)        #--->0,1,2
#     #rock = 0
#     #paper = 1
#     #scissors = 2
#     computer_choice = op[random_num]        #--->0,1,2
#     print("computer_pick--->",computer_choice)

#     #win situation:
#     if user_input == "rock" and computer_choice == "scissors":
#         print("you win!!")
#         user_win+=1
#         print(f"user win ---->{user_win} times!!")
#         continue
#     if user_input == "paper" and computer_choice == "rock":
#         print("you win!!")
#         user_win+=1
#         print(f"user win ---->{user_win} times!!")
#         continue
#     if user_input == "scissors" and computer_choice == "paper":
#         print("you win!!")
#         user_win+=1
#         print(f"user win ---->{user_win} times!!")
#         continue

#     #draw situation:
#     if user_input == "scissors" and computer_choice == "scissors":
#         print("draw!!....play again XD")
#         draw_match += 1
#         print(f"draw match ---->{draw_match} times!!")
#         continue
#     if user_input == "paper" and computer_choice == "paper":
#         print("draw!!....play again XD")
#         draw_match += 1
#         print(f"draw match ---->{draw_match} times!!")
#         continue
#     if user_input == "rock" and computer_choice == "rock":
#         print("draw!!....play again XD")
#         draw_match += 1
#         print(f"draw match ---->{draw_match} times!!")
#         continue

#     #loss situation:
#     if user_input == "paper" and computer_choice == "scissors":
#         print("OH you loss!! \nXD\nbetter-luck next time!!")
#         pc_win +=1
#         print(f"computer win ---->{pc_win} times!!")
#         continue
#     if user_input == "scissors" and computer_choice == "rock":
#         print("OH you loss!! \nXD\nbetter-luck next time!!")
#         pc_win +=1
#         print(f"computer win ---->{pc_win} times!!")
#         continue
#     if user_input == "rock" and computer_choice == "paper":
#         print("OH you loss!! \nXD\nbetter-luck next time!!")
#         pc_win +=1
#         print(f"computer win ---->{pc_win} times!!")
#         continue

# print("bye!!see you next time!!")







import random

win_situation = {
    "r" : "s",
    "s" : "p",
    "p" : "r"

}

choises = ["r","s","p"]
win,points,losse = 0,0,0
start = input("PLAY?\nplease Enter [Y]----->START!! : ").upper()
if start == "Y":
    def game(win_situation,choises):
        global win,points,losse
        while True:
            user_input = input("Enter your choice[R-rock/p-paper/s-scissors] of (Q/q)-(for EXIT) points!!(w): ").lower()
            if user_input == "q":
                print("SEE YOU SOON!!")
                break
            if user_input == "w":
                print("match win = ",win)
                print("points:-",points)
                print("Match losses:- ",losse)
            if user_input not in choises:
                print("please enter a valid op(r,p,s)!!")
                continue
            #draw situation:-
            pc_choice = random.choice(choises)
            if user_input == pc_choice:
                print("its Draw!!")
                points+=2.5
            #win situation:-
            elif win_situation[user_input] == pc_choice:
                print("you win!!")
                win+=1
                points+=5
            #lose situation:-
            elif win_situation[pc_choice] == user_input:
                print("you losses!!")
                losse+=1
                points-=5
            


    if __name__ == "__main__":
        game(win_situation,choises)

else:
    quit()
            


