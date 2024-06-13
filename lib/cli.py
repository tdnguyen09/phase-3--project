from helpers import retrieve_albums, add_album, delete_album, update_album, add_artist, retrieve_artists

def main():
    while True:
        print("Album Management CLI")
        print("1. Retrieve all albums")
        print("2. Add a new album")
        print("3. Delete an album")
        print("4. Update the information of an album")
        print("5. Retrieve all artists")
        print("6. Add a new artist")
        print("7. Exit")

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
            retrieve_artists()
        elif choice == "6":
            add_artist()
        elif choice == "7":
            print("Exiting the application")
            break
        else:
            print("Error. Please enter the number between 1 and 5.")

if __name__== "__main__":
    main()
    

    
