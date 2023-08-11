from random import randint
from tkinter import *

#generate the GUI
root = Tk()



def dummyCase(string, key):
    #the actual point of this program
    #is probably the easiest part of it
    #probably cuz the keyGen does most of the heavy lifting
    dummyString = ""
    for char, keyDex in zip(string, key):
        #basically uses the key as a choice, if the key is 0
        #even if it is already, make it lowercase
        #do the same with 1 for uppercase
        if keyDex == "0":
            #could have easily done it with a list instead of a string tbh
            #im not changing it cuz the functionality is the same and it 
            #doesnt really make much difference to me
            newChar = char.lower()
            dummyString += newChar
        elif keyDex == "1":
            newChar = char.upper()
            dummyString += newChar
        else:
            dummyString += char
    return dummyString


def repeatKey(sentence):
    choiceOfMask = randint(0, 1)
    if choiceOfMask == 1:
        key = "01"
    else:
        key = "10"
    keyGen = ""#generate empty string for key
    string_length = len(sentence)    
    i = 0
    j = 0
    while j < string_length:
        char_in_sentence = sentence[j]
        #use the length of the original 
        #sentence as the base for repetition
        if char_in_sentence.isalpha() == True:
            keyGen += key[i % len(key)]            
        else:
            keyGen += " "   
            i +=1         
        #i use two different variables so that if the character is not alpha
        #when i skip that iteration the next one does not give the same mask
        i +=1
        j +=1
    return keyGen



def buttonAction():#when i press the button, this code runs
    inputText = inputField.get()
    scrambledText = dummyCase(inputText, repeatKey(inputText))
    myLabel = Label(root, text=scrambledText)
    myLabel.pack()



inputField = Entry(root, width=40)#the textBox
inputField.pack()#pace the text box on the screen


scrambleButton = Button(root, text= "SCRAMBLE", command=buttonAction)
#the button that scrambles the text
scrambleButton.pack()



###Command Line Testing### 
#message = "thIs Is hoW i TyPe - r3p34t pl"
#print("Message: ", message)
#print("Key:     ", repeatKey(message))
#print("DummyCase: \n",dummyCase(message, repeatKey(message)))




#keeps the GUI running
root.mainloop()