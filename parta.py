# Reverse Function CSE 5408, lab 4 
def reverse_str(str):  
    Rstr = ""   # defines Empty String  
    for i in str:  #for loop 
        Rstr = i + Rstr  
    return Rstr # Returns reversed string  
     
word = input ("Enter a Word:")        
print("Word:",word)  
print("Reverse Word:",reverse_str(word))  