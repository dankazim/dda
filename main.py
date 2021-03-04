from datetime import datetime
TimeToString = datetime.now().strftime("%d/%m/%Y %H:%M")


notes = {"Mar 2 ": {"Date": "march 4", "Content": "Working on Note Keeper", "Labels": "Programming, testing, default"}}
notes_template = ["Date", "Title", "Descriptions", "Labels"]


def displayNotes():
  for key in notes:
    print(f'{key}: {notes[key]}')

def updateNote():
  addNote()
  notes[title] = {notes_template[0]: TimeToString, notes_template[2]: labels, notes_template[3]: labels}
  
def deleteNote(title):
  notes.pop(title)

def addNote():
  title = str(input("Title: "))
  descriptions = str(input("Description: "))
  labels = str(input("Label: "))
  notes[title] = {notes_template[0]: TimeToString, notes_template[2]: descriptions, notes_template[3]: labels}
  return title, descriptions,labels


  
def processInput():
  if option ==1:
    addNote()
    print("a new note was created")
  elif option ==2:
    displayNotes()
  elif option ==3:
    updateNote()
  elif option ==4:
    deleteNote
    
while True:
  print("\nWhat would you like to do?\n1: Create a new note.\n2: List all notes.\n3: Update a note.\n4: Remove a note")
  option = int(input("Your choice(1,2,3 or 4): "))
  processInput()


