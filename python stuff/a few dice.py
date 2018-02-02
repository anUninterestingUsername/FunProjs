import random
class Dice:
    def __init__(s,number=2,sides=6):
        s.sides=sides
        s.dices=[]
        total=0
        for i in range(number):
            s.dices.append(random.randint(1,s.sides))
            total+=s.dices[i]
        s.total=total
    def roll(s):
        total=0
        for i in range(len(s.dices)):
            s.dices[i]=random.randint(1,s.sides)
            total+=s.dices[i]
        s.total=total
        return total
    def __str__(s):
        st="Roll: "
        for i in s.dices:
            st+=str(i)+","
        st=st[0:-3]
        st+=" Total:"+str(s.total)
        return st
    def __gt__(s, o):
        if s.total>o.total:
            return True
        return False
    def __lt__(s,o):
        if s.total<o.total:
            return True
        return False
