"""BY Group 4: Dan M. Kazimoto, Hnin Wint Thu Aung, Nusara Boonma, Vichhagar Nhin """

from datetime import datetime
TimeToString = datetime.now().strftime("%d/%m/%Y %H:%M")

notes ={'John' :{'Date': '04/03/2021 14:55', 'Label': 'test', 'Descriptions': 'playing'}, 'Luke' :{'Date': '04/03/2021 14:55', 'Label': 'hahahah', 'Descriptions': 'dancing'}}

def linebreak_b():
  print("============================================")
  
def linebreak_t():
  print("____________________________________________")
  
def displayNotes():
  linebreak_t()
  print("-----------------List of Notes--------------")
  if notes =={}:
    print("---------Please create new notes----------")
  else:
    counter = 1
    for key in notes:
      if counter >1:
        print("")
      print(f'{counter}.{key}')

      counter +=1
      for subkey in notes[key]:
        print(f'  {subkey}: {notes[key][subkey]}')
        
  print("-------------------------------------------")       

def update_label(note_to_update):
  update = str(input(f"New Label for {note_to_update}:  "))
  notes[note_to_update]['Label'] = update
  linebreak_b()
  print(f"Label for {note_to_update} has been updated ")
  linebreak_b()

def update_description(note_to_update):
  update = str(input(f"New Descriptions for {note_to_update} "))
  notes[note_to_update]['Descriptions'] = update
  linebreak_b()
  print(f"Descriptions for {note_to_update} has been updated ")
  linebreak_b()

def update():
  displayNotes()
  linebreak_t()
  note_to_update = str(input("Title of notes to be updated: "))
  if note_to_update in notes:
    print(f"\nWhat do you want to update in {note_to_update}??\n1: The lable.\n2: The descriptions.")
    updateConfirmation = int(input("Your choice (1 or 2): "))
    update_menu(updateConfirmation, note_to_update)
  else:
    linebreak_b()
    print(f"The note, {note_to_update}, you are trying to update does not exist")
    linebreak_b()
  return note_to_update
  
def update_menu(updateConfirmation, note_to_update):
  menu_options ={
    1:update_label,
    2:update_description,
  }
  menu_options.get(updateConfirmation, "Invalid input")(note_to_update)

def delete():
  try:
    linebreak_t()
    if notes !={}:
      displayNotes()
      linebreak_t()
      print("--------------Delete Confirmation----------")
      note_to_delete = str(input("Title of notes to be deleted: "))
      notes.pop(note_to_delete)
      linebreak_b()
      print(f"-----the note,{note_to_delete}, has been deleted----")
      linebreak_b()
    else:
      linebreak_b()
      print("----You dont have any notes to be delete----")
      linebreak_b()
  except :
    linebreak_b()
    print(f"-------{note_to_delete} does not exist in notes------")
    linebreak_b()

def add():
  linebreak_t()
  print("--------------New Note Creation----------")
  title = str(input("Title: "))
  labels = str(input("Label: "))
  descriptions = str(input("Description: "))
  notes[title]= {"Date": TimeToString, "Label": labels,"Descriptions": descriptions}
 
  linebreak_b()
  print("-----------A new note was created-----------")
  linebreak_b()

def menu(option):
  menu_options ={
    1:add,
    2:displayNotes,
    3:update,
    4:delete
  }
  menu_options.get(option, "Invalid input")()

while True:
    print("\nWhat would you like to do?\n1: Create a new note.\n2: List all notes.\n3: Update a note.\n4: Remove a note")
    try:
      option = int(input("Your choice(1,2,3 or 4): "))
      menu(option)
    except ValueError:
      linebreak_b()
      print("-----invalid inputs, please follow instruction----")
      linebreak_b()



    