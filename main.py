from datetime import datetime
TimeToString = datetime.now().strftime("%d/%m/%Y %H:%M")

notes ={}
def displayNotes():
    if notes =={}:
      print("----You dont have any notes----")
    else:
      for key in notes:
        print(f'{key}: {notes[key]}')
      
def deleteNote():
  title = str(input("Title of note to be deleted: "))
  notes.pop(title)

def addNote():
  title = str(input("Title: "))
  labels = str(input("Label: "))
  descriptions = str(input("Description: "))
  notes[title]= {"Date": TimeToString, "Label": labels,"Descriptions": descriptions}

def updateNote():
 
  title = str(input("title of note you want to update: "))
  labels = str(input("Label: "))
  descriptions = str(input("Description: "))
  notes[title]= {"Date": TimeToString, "Label": labels,"Descriptions": descriptions}

def processInput():
  if option ==1:
    addNote()
    print("-----a new note was created------")
  elif option ==2:
    displayNotes()
  elif option ==3:
    updateNote()
    print("------a  note was updated------")
  elif option ==4:
    deleteNote()
    print("------a  note was deleted-------")
    
while True:
  print("\nWhat would you like to do?\n1: Create a new note.\n2: List all notes.\n3: Update a note.\n4: Remove a note")
  option = int(input("Your choice(1,2,3 or 4): "))
  processInput()
  