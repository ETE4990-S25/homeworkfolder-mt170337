# maggie and alex code

import os
import hashlib

def menu():
    while True:
        try:                                           #this part allows the user to input directory 
                                                       #for duplicates, else it will exit
            print("\n--- File Duplicate Finder ---")
            print("1. Enter directory to search")
            print("2. Exit")

            choice = str(input("Choose an option: "))

            if choice == "1":
                directory = input("input directory: ")

                for set_of_duplicates in find_duplicates(directory):
                    print("these are duplicates: ")
                    for duplicate_file in set_of_duplicates:
                        print(duplicate_file)

            else:
                print('exiting duplicate file finder')
                break

        except KeyboardInterrupt: # this breaks the loop if for some reason the while loop doesn't break
            break




def find_duplicates(directory): #this uses checksum to see if the same files are found, and redirects them to 
                                #the main to be printed for the user to see the duplicates if found
    dict_of_files= {}
    duplicates = []

    for dirpath, subdir, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(dirpath,file)
            file_checksum = get_checksum(file_path)

            if file_checksum in dict_of_files:
                dict_of_files[file_checksum].append(file_path)
            else:
                dict_of_files[file_checksum] = [file_path]

        

    for file_list in dict_of_files.values():
        if len(file_list) > 1:
            duplicates.append(file_list)

    return duplicates

    # search os.walk(directory):
    # use a dictionary to store file names and paths
    # compare files with the same name

def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


if __name__ == "__main__":
    menu()