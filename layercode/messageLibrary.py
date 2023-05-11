#This is a mock todo library

#Constant for test

# class messageLibrary():
 
name = "Message Library"

def replace_letters(message):
    letter_target = 'a'
    letter_replacement = 'test6'
    result = ""
    for i in range(0, len(message)):
        if message[i] == letter_target:
            result += letter_replacement
        else:
            result += message[i]
    return result
            
            