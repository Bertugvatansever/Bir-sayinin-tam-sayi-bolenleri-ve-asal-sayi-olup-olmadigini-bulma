# Tam bölünenleri Yazdırma 
sayı=int(input("İstediğiniz sayıyı giriniz."))
kalansızbölen=[]
bölen=1
for i in range(sayı):
    
        if(sayı % bölen==0):
        
            kalansızbölen.append(bölen)
        
        bölen+=1

print(kalansızbölen)
# Asal olup olmadığını belirleme
def Asal_mi(sayı):
    i=2
    if(sayı==1):
        return False
    elif(sayı==2):
        return True
    else:
        while(i<sayı):
            if(sayı%i==0):
                return False
            i+=1
            return True            
Asal_mi(sayı)

