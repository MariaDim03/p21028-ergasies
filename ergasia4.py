import random
xartia=[]
figures=["J", "Q", "K"]
xarti=[i for i in range(1, 11)] + figures
color=["H", "S", "C", "D"]
paixnidia=0
print ("First 100 rounds!")
while paixnidia<100:
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    wins_p1=0
    wins_p2=0
    draws=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        #arxizw to moirasma
        #print (player1)
        for card in player1:
            if card[0] in figures:   
                sum1=sum1=10
            else:
                sum1=sum1+card[0]
        print(sum1)
    #pairnw periptwseis   
    if sum1>21:
        print("P2 wins!")
        wins_p2=wins_p2+1
    else:
        print("P2 joins the game")
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            #mpainei o deyteros paikths
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2=card[0]
            print(sum2)
        #pairnw periptwseis kai briskw to plhthos twn nikwn kathe paikth me to wins-...
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            wins_p1=wins_p1+1
        elif sum2>sum1:
            print("P2 wins!")
            wins_p2=wins_p2+1
        else:
            print("draw!")
            draws=draws+1
print ("P1 has", wins_p1, "wins, P2 has", wins_p2, "wins and the draws are", draws, "for the first 100 games!")

print ("Another 100 rounds")
paixnidia=0
while paixnidia<100:
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    sum1=0
    wins_p1=0
    wins_p2=0
    draws=0
    while sum1<16:
        sum1=10
        player1.append(xartia.pop())
        #print (player1)
        for card in player1:
            #bazw proypoueseis gia to prwto fyllo
            if paixnidia==1:
                sum1=sum1+10
            else:
                if card[0] in figures:   
                    sum1=sum1=10
                else:
                    sum1=sum1+card[0]
        print(sum1)
    if sum1>21:
        print("P2 wins!")
        wins_p2=wins_p2+1
    else:
        print("P2 joins the game")
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            #print (player2)
            for card in player2:
                #bazw proypoueseis gia to prwto fyllo
                if paixnidia==1:
                    if card[0] in figures:
                        player2.append(xartia.pop())
                    else:
                        sum2=sum2+card[0]
                else:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2=card[0]
            print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            wins_p1=wins_p1+1
        elif sym2>sum1:
            print("P2 wins!")
            wins_p2=wins_p2+1
        else:
            print("draw!")
            draws=draws+1
print ("P1 has", wins_p1, "wins, P2 has", wins_p2, "wins and the draws are", draws, "for the first 100th games!")


         
