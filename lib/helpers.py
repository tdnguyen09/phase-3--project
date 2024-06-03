import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'db'))

from models import Album, Session
from datetime import datetime

def retrieve_albums():
    session = Session()
    albums = session.query(Album).all()
    if albums:
        for album in albums:
            print(album)
    else: 
        print('No data found.')
    session.close()

def add_album():
    session = Session()
    name = input("Enter album name: ")
    artist = input("Enter artist: ")
    release_date = input("Enter release date (DD-MM-YYYY): ")
    try:
        release_date = datetime.strptime(release_date, "%d-%m-%Y")
        new_album = Album(name=name, artist= artist, release_date=release_date)
        session.add(new_album)
        session.commit()
        print(f"Album {name} added successfully.")
    except ValueError:
         print(f"Invalid date format. Please enter the date in DD-MM-YYYY format.")
    
    session.close()

def delete_album():
    session = Session()
    name = input("Enter album name to delete: ")
    albums = session.query(Album).filter_by(name=name).all()
    if not albums:
        print('No data found.')
    elif len(albums) == 1:
        album = albums[0]
        session.delete(album)
        session.commit()
        print(f"Album {name} deleted successfully.")
    else:
        print(f'There are {len(albums)} with the name {name}.')
        confirm = input("Do you want to delete all of them? (yes/no): ").strip().lower()
        if confirm == "yes":
            for album in albums:
                session.delete(album)
            session.commit()
            print(f"All the albums with the name {name} deleted successfully. ")
        else:
            print("No albums were deleted.")
    session.close()

def update_album():
    session = Session()
    id = input("Enter id to update: ")
    album = session.query(Album).filter_by(id = id).first()
    if not album:
        print("No data found.")
    else:
        while True:
            print("Please select which options that you would like to update")
            print("1. Update name")
            print("2. Update artist")
            print("3. Update release date")
            print("4. Exit")

            option = input("Please select number from 1 to 3: ")
            
            if option == "1":
                new_name = input("Enter the new name: ")
                album.name = new_name
                session.commit()
                print(f"Album {id} updated successfully with the new name {new_name}")
                break
            elif option == "2":
                new_artist = input("Enter the artist: ")
                album.artist = new_artist
                session.commit()
                print(f"Album {id} updated successfully with the artist {new_artist}")
                break
            elif option == "3":
                new_release_date = input("Enter release date (DD-MM-YYYY): ")
                try:
                    new_release_date = datetime.strptime(release_date, "%d-%m-%Y")
                    album.release_date = new_release_date
                    session.commit()
                    print(f"Album {id} updated successfully with the new release date {new_release_date} ")
                    break
                except ValueError:
                    print(f"Invalid date format. Please enter the date in DD-MM-YYYY format.")
            elif option == "4":
                break
            else: 
                print("Please only select number from 1 to 4.")
    session.close()



