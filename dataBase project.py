while True:
    programType = input("Enter a type (read,r / write,w / z,to clear the file) or press ENTER to exit:")


    def main():
        if programType.isalpha() or programType == "":
            if programType.upper() == "R":

                while True:
                    choice = input(
                        "\t\t   **please choose an "
                        "option**\n------------------------------------------------------\n1-print all usernames. "
                        "\t2-print a specific username.\n\t\t\t  or press ENTER to "
                        "return\n------------------------------------------------------\nEnter your option:")

                    def search():
                        userName = input("Enter the username, ID or section number: ")
                        if userName == "" or userName.isspace():
                            print("please enter a valid username or ID!")
                            search()

                        else:
                            readable_user_names = open("USERNAMES.txt", "r")
                            result = ""
                            found = False
                            line = 0
                            lines = readable_user_names.readlines()
                            for row in lines:
                                if row.find(userName) != -1:
                                    found = True
                                    result = result + lines[line]
                                    line += 1
                                else:
                                    line += 1

                            if not found:
                                print("\nUsername is not in the system!\n")
                            elif result != "":
                                print("-"*54)
                                print("%-20s%-24s%s" % ("Name","ID","Section"))
                                print("-"*54)
                                print(result)
                            readable_user_names.close()

                    if choice.isdigit() or choice == "":
                        if choice == "":
                            break
                        elif 0 < int(choice) < 3:
                            ReadableUserNames = open("USERNAMES.txt", "r")
                            if int(choice) == 1:
                                print("-"*54)
                                print("%-20s%-24s%s" % ("Name","ID","Section"))
                                print("-"*54)
                                print(ReadableUserNames.read())

                            else:
                                search()
                            ReadableUserNames.close()

                        else:
                            print("Error:wrong input!")

                    else:
                        print("Error:wrong input!")


            elif programType.upper() == "W":
                WritableUserNames = open("USERNAMES.txt", "a")

                while True:
                    try:
                        name = input("Enter your username: ")

                        if name.isalpha():
                            ID = input("Enter your ID: ")
                            if ID.isalnum() and len(ID) == 9:
                                sectionNumber = input("Enter your section number: ")
                                if len(sectionNumber) <= 2 and sectionNumber.isdigit():
                                    WritableUserNames.write("%-20s%-24s%s\n" % (name,ID,sectionNumber))
                                    break

                                else:
                                    raise TypeError
                            else:
                                raise TypeError
                        else:
                            raise TypeError
                    except TypeError:
                        print("ERROR:wrong input!")

                WritableUserNames.close()

            elif programType.upper() == "Z":
                while True:
                    approval = input("you will delete the file content permanently are you sure? (yes:y / no:n): ")
                    if approval.upper() == "Y":
                        password = input("please enter password to confirm the delete process: ")
                        if password == "Mohammad202152970#":
                            clearFile = open("USERNAMES.txt", "w")
                            clearFile.close()
                            print("file cleared successfully!")
                            break
                        else:
                            print("access denied [Wrong password!]")
                            break
                    elif approval.upper() == "N":
                        print("delete canceled!")
                        break
                    else:
                        print("ERROR:wrong input!")




            elif programType == "":
                print("-----EXITING-----\n  See you soon.")
                raise StopIteration

            else:
                raise TypeError
        else:
            raise TypeError


    try:
        main()
    except StopIteration:
        break
    except TypeError:
        print("ERROR:wrong input!")
