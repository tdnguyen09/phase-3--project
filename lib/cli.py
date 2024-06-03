from helpers import retrieve_albums, add_album, delete_album, update_album

def main():
    while True:
        print("Album Management CLI")
        print("1. Retrieve all students")
        print("2. Add a new album")
        print("3. Delete an album")
        print("4. Update the information of an album")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            retrieve_albums()
        elif choice == "2":
            add_album()
        elif choice == "3":
            delete_album()
        elif choice == "4":
            update_album()
        elif choice == "5":
            print("Exiting the application")
            break
        else:
            print("Error. Please enter the number between 1 and 5.")

if __name__== "__main__":
    main()
    

    
