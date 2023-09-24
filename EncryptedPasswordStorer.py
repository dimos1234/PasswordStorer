import random
import getpass
import os

lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
allAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+\'\";:/?.>,<[]{}`~"


def passwordGenerator(strength):

  password = ""

  if strength in "low Low l weak Weak w W L".split():
    passLength = random.randint(5, 9)

    for i in range(passLength):
      index = random.randint(0, len(lowerAlpha) - 1)
      password += lowerAlpha[index]

  elif strength in "medium Medium m M".split():
    passLength = random.randint(8, 12)

    for i in range(passLength):
      index = random.randint(0, len(alpha) - 1)
      password += alpha[index]

  elif strength in "high High strong Strong s S h H".split():
    passLength = random.randint(9, 15)

    for i in range(passLength):
      index = random.randint(0, len(allAlpha) - 1)
      password += allAlpha[index]
  else:
    print("\nPlease choose weak (w), medium (m), or strong (s)\n")
    return None

  return password


def karakaEncription(word):
  reversedWord = word[::-1]
  reversedWord = reversedWord.replace("a", "0", -1)
  reversedWord = reversedWord.replace("e", "1", -1)
  reversedWord = reversedWord.replace("i", "2", -1)
  reversedWord = reversedWord.replace("o", "3", -1)
  reversedWord = reversedWord.replace("u", "4", -1)
  reversedWord += "aca"
  return reversedWord


def karakaUnencription(word):
  word = word.replace("aca", "", -1)
  word = word.replace("0", "a", -1)
  word = word.replace("1", "e", -1)
  word = word.replace("2", "i", -1)
  word = word.replace("3", "o", -1)
  word = word.replace("4", "u", -1)
  reversedWord = word[::-1]
  return reversedWord


def writeToFile(text):
  f = open("passwords.txt", "a")
  f.write(text)
  f.close()


def readFile():
  f = open("passwords.txt", "r")
  for line in f:
    stripLine = line.strip()

    if len(stripLine) == 0:
      print("\n")
    elif stripLine[-1] == "p":
      lisStripline = list(stripLine)
      lisStripline.pop()
      print(karakaUnencription("".join(lisStripline)))
    elif stripLine[-1] == "n":
      lisStripline = list(stripLine)
      lisStripline.pop()
      print("".join(lisStripline))
  f.close()


def changeEntrancePass(newEntrancePass):
  f = open("userpassword.txt", "w")
  f.write(karakaEncription(newEntrancePass))
  f.close()


print(
    "Welcome to the password storer!\n====================================================\n\n"
)

while True:
  entrancePass = getpass.getpass(
      'Please enter password to access program (the starting password is "password"): '
  )
  stripLine = ""
  f = open("userpassword.txt", "r")
  for line in f:
    if line.strip() != None:
      stripLine = line.strip()
  if entrancePass == karakaUnencription(stripLine):
    os.system("clear")
    break
  else:
    f.close()

while True:
  os.system("clear")
  storeOrAdd = input(
      "Would you like to generate a password (g), add a password (a), change you entrance password (c), or read your passwords (r)?\n"
  )

  if storeOrAdd in "generate Generate g G".split():
    os.system("clear")
    while True:
      strength = input(
          "How strong would you like your password?\nweak (w), medium (m), or strong (s): "
      )
      if (passwordGenerator(strength) == None):
        continue
      break
    password = passwordGenerator(strength)
    os.system("clear")
    print("\n\nYour password is: " + password)
    input("\nPress Enter to continue: ")

  elif storeOrAdd in "add Add a A".split():
    os.system("clear")
    password = getpass.getpass(
        "Enter the password you would you like to add (text will not show): ")

    os.system("clear")
    nameYesNo = input("is there a name to go with it?\n")
    if nameYesNo in "y Y yes Yes yeah Yeah ye Ye".split():
      os.system("clear")
      name = input("Enter the name to go with the password: ")
      if name == "c":
        pass
      else:
        writeToFile(name + "n" + "\n")

    if password == "c":
      pass
    else:
      os.system("clear")
      proceed = input("Proceeding to write: " + password +
                      "\n\nWould you like to continue? (y/n)\n")
      if proceed in "n N no No".split():
        pass
      else:
        writeToFile(karakaEncription(password) + "p" + "\n\n")
        os.system("clear")

  elif storeOrAdd in "r R read Read".split():
    os.system("clear")
    readFile()
    input("\n\n\nPress enter to continue:")

  elif storeOrAdd in "c C Change change".split():
    os.system("clear")
    newEntrancePass = getpass.getpass(
        "please enter the new entrance password: ")
    confirmChange = input("Changing entrance password to: " + newEntrancePass +
                          "\nWould you like to continue? (y/n)\n")
    if confirmChange in "y Y yes Yes".split():
      changeEntrancePass(newEntrancePass)
      os.system("clear")
    else:
      pass

  os.system("clear")
  useAgain = input("Would you like to make another action?\n")
  if useAgain in "y Y yes Yes ye Ye yah Yah Yeah yeah".split():
    continue
  else:
    break
