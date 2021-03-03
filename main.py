list_note = {"Mar 2 ": {"Content": "Working on Note Keeper", "Labels": "Programming, testing, default"}, "Mar 3": {"Content": "Respiratory", "Labels": "Biology, Systolic, Balloon, default"}}
detail_note = ["Title", "Content", "Labels"]


line = "============================="

def show_notes():
  print("\nList of all notes:")
  for i in list_note:
    print(f"\nTitle: {i}\n{line}")
    view_note(i)

def view_note(title = ""):
  if len(title) < 1:
    title = str(input("Enter the title: "))
  # print(list_note[title])
  for k, v in list_note[title].items():
    print(f"{k}: {v}")  


def create_update_note():
  temp = []
  print("")
  for i in range(0, 3):
    # print(f"Enter {detail_note[i]}: ")
    temp.append(str(input(f"Enter the {detail_note[i]}: ")))
  title, content, labels = temp
  # title = "Mac 4"; content = "Watching youtube video"; labels = "YouTube, Google"
  list_note[title] = {detail_note[1]: content, detail_note[2]: labels}
  print(f"{title} has been added/updated!")
  

def del_note():
  title = str(input("Enter the title: "))
  list_note.pop(title)
  print(f"{title} has been deleted!")


def menu_option(selection):
  menu = {
    'C': create_update_note, 
    'R': show_notes, 
    'U': create_update_note, 
    'D': del_note
    }
  menu.get(selection, "Invalid input")()

while True:
  print("\nWhat would you like to do?\nC: Create a note\nR: List title of notes; and show a note\nU: Update a note\nD: Remove a note")
  selection = str(input("Your input: "))
  menu_option(selection)



# create_update_note()
# show_notes()


