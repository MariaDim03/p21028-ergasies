fin=open("keimeno.txt","r")
#ftiaxnw lista me kathe xarakthra
list(fin)
f=[]
sum=0
sum_zygwn=0
sum_pol3=0
sum_pol5=0
sum_pol7=0
i=1
for i in fin:
    #metatrepw se dyadiko
    fin[i]=bin(fin[i])
    #frontixw oi dyadikoi poy exoyn ligotera stoixeia apo 7 na symplhrwthoyn sthn arxh me mhdenika me to if
    if len(fin[i])<7:
        x=7-len(fin[i])
        fin[i]=x*[0]+fin[i]
    #krataw 2 prwta kai dyo teleytaia stoixeia gia kathe arithmo
    fin[i]=fin[:2, 6:]
    #metatrepw se dekaeksadiko
    fin[i]=hex(fin[i])
    #metatrepw se dekadiko ksana gia na brw ta pososta alla krataw kai thn lista me toys dekaeksadikoys
    f[i]=fin[i]
    f[i]=int(f[i],10)
    #prwta briskw to plhthos olwn twn arithmwn
    sum=sum+1
    if f[i]%2==0:
        sum_zygwn=sum_zygwn+1
    if f[i]%3==0:
        sum_pol3=sum_pol3+1
    if f[i]%5==0:
        sum_pol5=sum_pol5+1
     if f[i]%7==0:
        sum_pol7=sum_pol7+1  
#briskw pososta 
pos_z=(sum_zygwn/sum)*100        
pos_3=(sum_pol3/sum)*100
pos_5=(sum_pol5/sum)*100
pos_7=(sum_pol7/sum)*100
print ("Ta pososta poy zhtoyntai einai antistoixa", pos_z, pos_3, pos_5, pos_7)