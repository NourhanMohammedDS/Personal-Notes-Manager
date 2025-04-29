import datetime
notes = []

#function to display the main menu

def show_menu():
    print("\n ====Personal Notes Manager=====")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Exit")

def add_note():
    note = input("Enter your Note :  ")
    time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    notes.append(f"{time} - {note}")
    print("Note Added Successfully !")

def view_notes():
    if not notes:
        print("No notes Avaiable.")
    else:
        print("---All Notes----")
        for i,note in enumerate(notes,1):
            print(f"{i}. {note}")

def search_notes():
    keyword = input("Enter keyword to search : ").lower()
    found = False
    for note in notes:
        if keyword in note.lower():
            print(note)
            found = True
    if not found:
        print("No Maching Notes")

#Main program

while True:
    show_menu()
    choice = int(input("choose an option (1-4)"))

    if choice == 1:
        add_note()
    elif choice ==2:
        view_notes()
    elif choice ==3:
        search_notes()
    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")


