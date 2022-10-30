liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print("ilk hali listenin" , liste)

def duzlestir(aList): 
	result = [] 
   
	for entry in aList: 
        
		if type(entry) == list:
			result+=duzlestir(entry) 
		else: 
			result.append(entry) 
	return result[::-1]
 


analiste = duzlestir(liste)
print("fonksiyondan çıkan hali" , analiste)

cevir = analiste[4:8]


cevrildi = cevir[::-1]



guncell =  analiste +cevrildi

del guncell[4:7]


guncell.pop(4)

print("soruda istenen hali", guncell)


