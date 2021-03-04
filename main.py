from datetime import datetime
TimeToString = datetime.now().strftime("%d/%m/%Y %H:%M")

notes ={'Date': '04/03/2021 14:55', 'Label': 'test', 'Descriptions': 'testing my small notebook'}

def linebreak_b():
  print("============================================")
  
def linebreak_t():
  print("____________________________________________")
  print("")

def displayNotes():
    if notes =={}:
      print("---------Please create new notes--------")
    else:
      for key in notes:
        print(f'{key}: {notes[key]}')
      
def deleteNote():
  if notes !={}:
    title = str(input("Title of notes to be deleted: "))
    notes.pop(title)
  else:
    print("----You dont have any notes to be delete----")

def add_or_update():
  title = str(input("Title: "))
  labels = str(input("Label: "))
  descriptions = str(input("Description: "))
  notes[title]= {"Date": TimeToString, "Label": labels,"Descriptions": descriptions}

def processInput():
  if option ==1:
    linebreak_t()
    add_or_update()
    linebreak_b()
    print("-----------A new note was created-----------")
    linebreak_b()

  elif option ==2:
    linebreak_t()
    displayNotes()
    linebreak_b
   
  elif option ==3:
    linebreak_t()
    add_or_update()
    linebreak_b()
    print("------------A  note was updated-------------")
    linebreak_b()

  elif option ==4:
    linebreak_t()
    deleteNote()
    linebreak_b()
    print("-----------A  note was deleted--------------")
    linebreak_b()
  else:
    linebreak_b()
    print("<<<<<<<<<<<<< invalid input >>>>>>>>>>>>>>>>")

while True:
  try:
    print("\nWhat would you like to do?\n1: Create a new note.\n2: List all notes.\n3: Update a note.\n4: Remove a note")
    option = int(input("Your choice(1,2,3 or 4): "))
    processInput()
  except ValueError:
    linebreak_b()
    print("Please follow input instruction, number only")
    linebreak_b()
    