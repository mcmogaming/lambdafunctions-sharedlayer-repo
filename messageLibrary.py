#This is a mock todo library

def replace_letters(message,  letter_replacement):
    letter_target = 'a'
    letter_replacement = 'z'
        
    for i in range(0, len(message)):
        if message[i] == letter_target:
            message[i] = letter_replacement
    
    return message
        
        