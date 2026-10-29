# Caesar Cipher
# Create a program that implements a Cesar cipher, an encryption method
# that shifts letters in the alphabet to encode messages.

# Step 1
# Create a variable called shift and assign the value 5.
shift = 5

# Step 2
# Declare another variable called alphabet and assign the whole alphabets.
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Step 3
# Create a variable named shifted_alphabet and use slicing syntax to assign it
# the portion of alphabet that starts at the index of shift. 
# Then, call the built-in Print() function to print shifted_alphabet.
shifted_alphabet = alphabet[shift:]
print(shifted_alphabet)

# Step 4
# The result of the shifted alphabet starts at the letter f becuse shift
# has the value 5. However the first 5 letters of the alphabet are missing.
# So, we need to add them back at the end of the shifted alphabet.
# Modfiy the existing assignment of the shifted_alphabet variable.
# Reminder: sentence[start, stop] returns the characters of sentence from
# position start (included) to stop (excluded).
shifted_alphabet = alphabet[shift:] + alphabet[:shift]

# Step 5
# Remove the print (shifted_alphabet) call
# print(shifted_alphabet)

# Step 6
# Side note: str.maketrans() method takes two strings of equal length and returns
# a translation table that maps each character of the first string to the corresponding
# character of the second string. Each character in the translation table is stored
# as a Unicode ordinal, a number that uniquely identifies the character.
# For now create a translation table that maps the characters in alphabet to the
# characters in shifted_alphabet and assign it to a variable named translation_table.
translation_table = str.maketrans(alphabet, shifted_alphabet)

# Step 7
# Declare a variable named text and assign it the string hello world.
# This will be the message to encrypt.
text = "hello world"

# Step 8
# Side note: the translate() method takes as argument the translation table generated
# by str.maketrans(). It is called on a string and returns a copy of the original string
# where the characters have been replaced based on the translation_table.
# Call the translate() method on text passing in the translation_table as the argument
# and assign the result to a variable named encrpyed_text.
encrypted_text = text.translate(translation_table)

# Step 9
# Print encrypted_text to see the output
print(encrypted_text)

# Step 10
# The text variable has been encrypted, now make the code reusable so it can encrypt
# different messages. Create a function named caesar. Then, put all existing code within
# the function body. 
def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 5
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    text = 'hello world'
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)
    
# Step 11
# Current message to encrypt and the shift are still hardcoded. Give the function two
# parameters named text and shift, and delete the declarations of both variables from
# the caesar function body.
def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)

# Step 12
# Test the function by calling it with another string and another number as arguments.
# Assign the function call to a variable named encrypted_text.
encrypted_text = caesar("freeCodeCamp", 3)

# Step 13
# The current function should gives back None by default, test by print encrypted_text.
print(encrypted_text)

# Step 14
# Remove the print(encrypted_text) from the function and delete the declaration of the
# encrypted_text variable. Then, directly return text.translate(translation_table).
def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(translation_table)

# Step 15
# Side note: although the message is encrypted, the uppercase chars have been left 
# untouched. This happens because the translation table does no include uppercase letters.
# Update your str.maketrans() call by concatenating to each argument the uppercase
# version of the argument itself.
def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

# Step 16
# Add some validation. At the beginning of the function's body, create an if statement.
# Use True as the condition for now, and within the if statement body return the string
# "Shift must be an integer value".
def caesar(text, shift):
    if True:
       return "Shift must be an integer value." 
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

# Step 17
# Replace the condtion of the if statement with an isinstance() call. Pass in shift as the 
# first argument, and int as the second argument.
def caesar(text, shift):
    if isinstance(shift, int):
       return "Shift must be an integer value." 
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

# Step 18
# Side note: the not or ! operator reverse a boolean value.
# Use the not operator to fix the condition of the if statement so that the function
# returns "Shift must be an integer value." when shift is not an integer.
def caesar(text, shift):
    if not isinstance(shift, int):
       return "Shift must be an integer value." 
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Step 19
# Side note: in Python, bool is a subclass of int, where True behaves like 1 and False
# behaves like 0. This means that isinstance() treats Boolean values as integers.
# Use the or operator to add a second condition to your if statement that checks if shift
# is a Boolean with isinstance(shift, bool).
def caesar(text, shift):
    if not isinstance(shift, int) or isinstance(shift, bool):
       return "Shift must be an integer value." 
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Step 20
# A negative or null shift should not be accepted by your function. Therefore, after the first
# if statement, create another if statement that checks if shift is less than 1 and returns the
# string "Shift must be a positive integer.".
def caesar(text, shift):
    if not isinstance(shift, int) or isinstance(shift, bool):
       return "Shift must be an integer value." 
    if shift < 1:
        return "Shift must be a positive integer."
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Step 21
# Add a second to the if statement that checks if shift is greater than 25. Also, update
# the returned message to "Shift must be an integer between 1 and 25.".
def caesar(text, shift):
    if not isinstance(shift, int) or isinstance(shift, bool):
       return "Shift must be an integer value." 
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Step 22
# Side note: Python allows to specify a default value for the parameter in a function,
# creating a function that can be called with fewer or no arguments. Use a name parameter
# that has a default value.
# Add a third parameter named encrypt to your function and give it a default value of True.
def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int) or isinstance(shift, bool):
       return "Shift must be an integer value." 
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Step 23
# Use the parameter added to determine if the function should encrypt or not. Create an if
# statement that checks if encrpt is not truthy. Within the new if statement, set shift to
# - shift. This is necessary to enable the shift to take place in the opposite direction with
# respect to the encryption process.
def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int) or isinstance(shift, bool):
       return "Shift must be an integer value." 
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."
    if not encrypt:
        shift = - shift
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Step 24
# Declare two functions named encrypt and decrypt, both with thext and shift parameters.
# Use encrypt for encryption and decrypt for decryption, giving each action a descriptive name.
# From both new functions, return a caesar call that passes in text and shift. In decrypt, also
# pass False a the third argument
def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)

# Step 25 
# Test the encrypt function.
encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)

# Step 26
# test the decrpt function. Replace the value assigned to encrypted_text with the 
# following string, which represents a message to decrypt: Pbhentr vf sbhaq va hayvxryl cynprf.
# Then, declare a variable named decrypted_text and assign it a call to decrypt with 
# encrypted_text as its first argument and a shift of 13 as the second argument.
# Finally, print the decrypted_text on the terminal. With that, the Caesar cipher is complete.
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

# Final Code
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int) or isinstance(shift, bool):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
