from create_s import create
from read_s import read
from update_s import update
from delete_s import delete

def inquiry():
    selection = input("Enter your choice C/R/U/D ")
    selection = selection.lower()
    def exit_message():
        print("Thank you see you again !")
    if selection == "c":
        contd = create()
        inquiry() if contd else exit_message()
    elif selection == "r":
        id = input("Enter the student id ")
        contd = read(id)
        inquiry() if contd else exit_message()
    elif selection == "u":
        id = input("Enter the student id ")
        to_change = input("Enter the info you want to change ")
        if to_change in ["name", "age"]:
            changed_data = input(f"Enter the new {to_change} ")
            contd = update(id, to_change, changed_data)
            inquiry() if contd else exit_message()
        else:
            print("Invalid key")
            inquiry()
    elif selection == "d":
        id = input("Enter the student id ")
        contd = delete(id)
        inquiry() if contd else exit_message()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    inquiry()