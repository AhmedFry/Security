# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:04:22 2020

@author: FRy
"""

def Process(Type , operation , inputFile , outputFile):
    result = ""
    
    if (Type == 'shift'):
        Key = int(input("Enter the key : "))
        if (operation == 'encrypt'):
            F1 = open(inputFile , "r")
            Content = F1.read()
            F1.close()
            F2 = open(outputFile , "w")
            for i in range(len(Content)) :
                if (Content[i].isupper()) :
                    result += chr((ord(Content[i]) + Key-65) % 26 + 65)
                else :
                    result += chr((ord(Content[i]) + Key-97) % 26 + 97)
            F2.write(result)
            F2.close()
        elif(operation == 'decrypt') :
            F1 = open(inputFile , "r")
            Content = F1.read()
            F1.close()
            F2 = open(outputFile , "w")
            for i in range(len(Content)) :
                if (Content[i].isupper()) :
                    result += chr((ord(Content[i]) - Key-65) % 26 + 65)
                else :
                    result += chr((ord(Content[i]) - Key-97) % 26 + 97)
            F2.write(result)
            F2.close()
    elif (Type == 'affine'):
        a =int(input("Enter the first key : "))
        b =int(input("Enter the second key : ")) 
        if (operation == 'encrypt'):
            F1 = open(inputFile , "r")
            Content = F1.read()
            F1.close()
            F2 = open(outputFile , "w")
            for i in range(len(Content)) :
                if (Content[i].isupper()) :
                    result += chr((a *(ord(Content[i]) -65 ) +b ) % 26 + 65)
                else :
                    result += chr(( a *(ord(Content[i]) -97 ) + b) % 26 + 97)
            F2.write(result)
            F2.close()
        elif(operation == 'decrypt') :
            for i in range(26):
                if ((a * i) % 26) == 1 :
                        a_inv = i
            F1 = open(inputFile , "r")
            Content = F1.read()
            F1.close()
            F2 = open(outputFile , "w")
            for i in range(len(Content)) :
                if (Content[i].isupper()) :
                    result += chr((a_inv * ((ord(Content[i]) -65 ) - b )) %26 + 65)
                else :
                    result += chr((a_inv * ((ord(Content[i]) -97 ) - b )) %26 + 97)
            F2.write(result)
            F2.close()
    elif (Type == 'vigenere'):
        Key = str(input("Enter the key : "))
        if (operation == 'encrypt'):
            F1 = open(inputFile , "r")
            Content = F1.read()
            F1.close()
            num = (int((len(Content) / len(Key))+1)) * Key
            vKey = num[:len(Content)]
            print (vKey)
            F2 = open(outputFile , "w")
            for i in range(len(Content)) :
                if (Content[i].isupper()) :
                    result += chr(((ord(Content[i]) -65) +(ord(vKey[i].upper()) - 65 )) % 26 + 65)
                else :
                    result += chr(((ord(Content[i]) -97) +(ord(vKey[i].lower()) - 97 )) % 26 + 97)
            F2.write(result)
            F2.close()
        elif (operation == 'decrypt'):
            F1 = open(inputFile , "r")
            Content = F1.read()
            F1.close()
            num = (int((len(Content) / len(Key))+1)) * Key
            vKey = num[:len(Content)]
            print (vKey)
            F2 = open(outputFile , "w")
            for i in range(len(Content)) :
                if (Content[i].isupper()) :
                    result += chr(((ord(Content[i]) -65) - (ord(vKey[i].upper()) - 65 )) % 26 + 65)
                else :
                    result += chr(((ord(Content[i]) -97) - (ord(vKey[i].lower()) - 97 )) % 26 + 97)
            F2.write(result)
            F2.close()


        
        
        
        
        
        
Process ('vigenere','decrypt','F_input.txt','F_out.txt')

