fin=open("keimeno.txt","r")
fin.lower()
words=[]
#ftiaxnw lista me oles tis lekseis
for line in fin:
    line=line.strip()
    words += line.split()
from collections import Counter
Counter(words)
print ("Oi 10 dhmofilesteres lekseis einai:")
print (Counter[:10])
i=1
two=[]
for i in words:
    two[i]=words[:2]
    #pairnw ta dyo prwta pshfia apo thn lista words opoy periexei tis lekseis poy xwrisame
pl2=[]
#ftiaxnw pinaka gia to plhthos kathe dipshfioy syndyasmoy
for i in two:
    for j in two:
        if two[i]==two[j]:
            pl2[i]=pl2[i]+1
#kanw taksinomhsh ton pinaka toy plhthoys twn syndyasmwn gia na brw ta tria dhmofilestera 
k=1
for k in range:len((pl2)-1):
    for n in range(len(pl2)-1-k):
        if pl2[n]>pl2[n+1]:
            pl2[n], pl2[n+1]=pl2[n+1], pl2[n]
s=1
while s<=3:
    print pl2[s]
    s=s+1
#kanw to idio gia thn periptwsh twn syndyasmwn an tria
i=1
three=[]
for i in words:
    three[i]=words[:3]
pl3=[]
#ftiaxnw pinaka gia to plhthos kathe dipshfioy syndyasmoy
for i in three:
    for j in three:
        if three[i]==three[j]:
            pl3[i]=pl3[i]+1
#kanw taksinomhsh ton pinaka toy plhthoys twn syndyasmwn gia na brw ta tria dhmofilestera 
k=1
for k in range(len((pl3)-1):
    for n in range(len(pl3)-1-k):
        if pl3[n]>pl3[n+1]:
            pl3[n], pl3[n+1]=pl3[n+1], pl3[n]
s=1
while s<=3:
    print pl3[s]
    s=s+1
