MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

CHARACTER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9', ', ', '.', '?', '/', '-', '(', ')']

# this function takes in characters in the alphabet and converts it to morse code
def encrypt(message):
  morse_message = ''
  for letter in message.upper():
    if letter == " ":
      morse_message += " "
    else: 
      # utilizes the dictionary for simple conversions 
      morse_message += MORSE_CODE_DICT[letter] + " "
  return morse_message

# this function takes in morse code and converts it to characters in the alphabet
def decrypt(message):
  result = ''
  message = message.split(" ")
  for morse_code in message: 
    if morse_code == "":
      result += " "
    else:
      for letter in CHARACTER:
        if MORSE_CODE_DICT[letter] == morse_code:
          result += letter
  return result

start = True
while start:
  # user can either input characters in the alphabet or morse code to encrypt or decrypt
  user_choice = input("Do you want to [e]ncrypt, [d]ecrypt, or [q]uit?: ")
  if user_choice == 'e':
    message = input("Please enter the message you would like to encrypt: ")
    encryption = encrypt(message)
    print(encryption)
  elif user_choice == 'd':
    message = input("Please enter the message you would like to decrypt: ")
    decryption = decrypt(message)
    print(decryption)
  # ends loop
  elif user_choice == 'q':
    start = False