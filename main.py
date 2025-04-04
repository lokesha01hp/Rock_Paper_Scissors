import random

l=["R","P","S"]
def playgame():
        user=input("Enter your choice, Rock(r) or Paper(p) or Scissor(s) or (c) to quit :").upper()
        computer=random.choice(l)
        if user =="C":
              print("Not enjoying the Game???")
              return -1
        if user == computer:
            print("Draw match")

        if check_win(user,computer):
            return "You won the battle"
        else:
            return "Computer won the match!!!"

def check_win(user1,computer1):
    if (user1 == "R" and computer1 == "S") or (user1 == "S" and computer1 == "P") or (user1 == "P" and computer1 == "R"):
        return True

print(playgame())

