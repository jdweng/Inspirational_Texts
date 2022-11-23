#Josh Wenger
#Project 2: Inspirational Text
#10/14/22

#Used Daniel Showalter's Project 2 template

#This code reads a text file and allows the user to search for a word/phrase and count the occurances of it, see it in context within the file, perform a search and replace,
#encode the whole text, search for the text on the internet to find where it is from, and email themselves either a chunk of random text or a chunk of text containing a keyword.


from random import randint
import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser

#Read text file
print('Welcome to the InspirationalTextMachine™!')
while True:
    file = input("Please enter the name of the text file you would like to use:\n")
    try:
        with open(file, 'r+') as f:
            text = f.read()
            break
    except:
        print("Make sure the file ends in '.txt' and is saved in the same folder as this file.\n")

#Functions
#Option 1: Counting
def counttext():
    while True:
        sens = input('Would you like your search to be case-sensitive? (y/n)\n')
        if sens == 'y':
            search_count = input('What word/phrase would you like to count?\n')
            print(text.count(search_count))
            break
        elif sens == 'n':
            search_count = input('What word/phrase would you like to count?\n')
            print(text.lower().count(search_count.lower()))
            break
        else:
            print("Please input 'y' or 'n'.")
            continue

#Option 2: Context
def context():
    while True:
        search_context = input('What word/phrase would you like context for?\n')
        try:
            index = text.index(search_context)
            if index - 20 >= 0:
                print(text[index-20:index+100])
                break
            elif index - 20 < 0:
                print(text[0:index+100])
                break
        except:
            print("That word/phrase is not in the text. Please enter a valid word/phrase.\n")
            continue

#Option 3: Search and Replace
def search_replace(text):
    search_replace_old = input('What word/phrase would you like to replace?\n')
    search_replace_new = input('What would you like to replace it with?\n')
    return text.replace(search_replace_old, search_replace_new)

#Option 4: Encode
def charshift(char, shift):
    abcs = 'qwertyuiopasdfghjklzxcvbnm'
    char = char.lower()
    try:
        if char in abcs:
            if 97 <= (ord(char)+shift) <= 122:
               return chr(ord(char)+shift)
            elif (ord(char)+shift) > 122:
                return chr(ord(char)+shift-26)
            elif (ord(char)+shift) < 97:
                return chr(ord(char)+shift+26)
        elif char not in abcs:
            return char
    except:
        print('Incorrect item class.')

   
def ceaser(text, shift):
    shiftedlyst = [charshift(x, shift) for x in text]
    shiftedstr = "".join(shiftedlyst)
    return shiftedstr

def encode():
    shift = randint(1,25)
    with open('encoded_'+file, 'w+') as f:
        f.write(ceaser(text, shift))
    print('The new encoded file has been created. It is called: encoded_'+file)

#Option 5: Internet Search
def search_internet():
    webbrowser.open('https://www.google.com/search?q=' + text)
    
#Option 6: Email
#Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
def sendEmail(sender, sendee, header, body, password):
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(sender, password)
    msg = MIMEMultipart()
    msg['From']= sender
    msg['To']= sendee
    msg['Subject']= header
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()

def email_context(index):
    if index - 20 >= 0:
        return text[index-20:index+100]
    elif index - 20 < 0:
        return text[0:index+100]
        
def get_input_send_email():
    while True:
        email_choice = input('Would you like to:'
                         '\n1. Email a chunk of text containing a specific word'
                         '\n2. Email a random chunk of text\n')
        if email_choice == '1' or email_choice == '2':
            break
        else:
            print("Please enter '1' or '2' to select your option")
            continue

    if email_choice == '1':
        while True:
            email_search = input('What keyword would you like to be in the email?\n')
            try:
                index = text.index(email_search)
                break
            except:
                print('That keyword is not in the text. Please enter a valid keyword.')
                continue
        email_text = email_context(index)

    elif email_choice == '2':
        index = randint(0,len(text)-1)
        email_text = email_context(index)
            
    while True:
        email = input("Please enter your email:")
        try:
            sendEmail("pythonatemu@outlook.com", email, "Inspirational Text", email_text, "1qazse4r")
            print("Email sent successfully.")
            break
        except:
            print("Please enter a valid email.")
            continue



#Menu starts here
function = ''
while function != '7':
    print('\n1. Count how many times a word/phrase appears'
          '\n2. Give context for a word/phrase (case-sensitive)'
          '\n3. Search and replace (case-sensitive)'
          '\n4. Encode the text'
          '\n5. Search the internet to find where the text is from'
          '\n6. Email me some text'
          '\n7. Quit')
    function = input('What would you like to do?\n')
    if function == '1':
        counttext()
    elif function == '2':
        context()
    elif function == '3':
        #I settled on doing this outside of a function to ensure that the text saved will be saved globally.
        with open (file, 'w+') as f:
            f.write(search_replace(text))
            f.seek(0)
            text = f.read()
        print('The search and replace has been completed.')
    elif function == '4':
        encode()
    elif function == '5':
        search_internet()
    elif function == '6':
        get_input_send_email()

print("Thanks for using the InspirationalTextMachine™. Goodbye!")
                     
        
