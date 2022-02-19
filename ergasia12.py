from urllib.request import Request, urlopen
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
url = "https://drand.cloudflare.com/public/latest"
i=0
A=[]
while i<100:
    #vriskw ton prwto gyrw ayths ths stigmhs
    a={"round":1662272,"randomness":"d6b15073fabe08ca870ac420538570485aa6d736067bef8a7b422db6cf148956","signature":"b4272efa27460fa3940bf9c499bd7a132858a1aa93f99657512022898dae9d488323ff72db26f94598d4afb0820a855b0787454b036359b92cd71a870865bdc06e1ceae6daaa0a3fb2092c64e7186dcd1b5b4dae3d43421a269316fbc70d60bb","previous_signature":"b767532aa1611e0b1fb1de4265067a5ff9bcafc60fdba1e4d573d972246d358c354db5a6e8fb13c6f81dfe87523ff319084235e47e1679b9e5c28330a81ff35832b50ef5f741e17e07b40731e457a37d63c811ffc92c6b585ec0fdd703b69ab2"}
    a.keys()
    #ypologizw poioys alloys gyroys tha xreiastw
    Round=a["round"]-i
    #briskw randomness kai to metatrepw
    A[Round]=a["randomness"]
    A[Round]=int(A,16)
    A[Round]=bin(int(A,16))
    #to kanw string
    str =''.join(A[Round])
#briskw ta mhdenika me synarthsh
def zeros(str, k):
    ans = 0
    curr = 0
    n = len(str)
    for i in str:
        if (i =='0'):
            curr+= 1
     
        else:
            curr = 0
        ans = max(ans, curr)
    if (ans == n):
        print(n * k)
        return
    else:
        pre = suff = 0
        for i in str:
            if(i =='0'):
                pre+= 1
            else:
                break
        for i in range(n-1, -1, -1):
                if(str[i]=='0'):
                    suff+= 1
                else:
                    break     
    if (k > 1):
        ans = max(ans, pre + suff)
        print(ans)
        return                   
print zeros(str, k)
#kanw to idio gia toys asoys
def aces(str, k):
    ans = 0
    curr = 0
    n = len(str)
    for i in str:
        if (i =='1'):
            curr+= 1
     
        else:
            curr = 0
        ans = max(ans, curr)
    if (ans == n):
        print(n * k)
        return
    else:
        pre = suff = 0
        for i in str:
            if(i =='1'):
                pre+= 1
            else:
                break
        for i in range(n-1, -1, -1):
                if(str[i]=='1'):
                    suff+= 1
                else:
                    break     
    if (k > 1):
        ans = max(ans, pre + suff)
        print(ans)
        return                   
 print aces(str, k)
