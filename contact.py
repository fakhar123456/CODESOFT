
def main():
    print("\n")
    print("                 📖 🅲 🅾 🅽 🆃 🅰 🅲 🆃   🅱 🅾 🅾 🅺 ☎️               \n--------------------------------------")
    print(" 🟡 To add the contacts to contact book, Enter 1.\n 🟡 To View the contacts from contact book, Enter 2.\n 🟡 To Search the contacts from contact book, Enter 3.\n 🟡 To update the contacts in contact book, Enter 4.\n 🟡 To delete the contacts in contact book, Enter 5.\n")
    inst = int(input(" Enter the instruction number: "))
    if inst == 1:
        add_contacts()     
    if inst == 2:
        get_all_contacts()
    if inst == 3:
        search_contact()
    if inst == 4:
        update_contacts()
    if inst == 5:
        delete_contact()






def add_contacts():
    with open("contact.txt", "a") as edit:
        n = input("Put contact informaion here: ")
        n = n + "\n"
        edit.write(n)
    main()

def search_contact():
    with open("contact.txt") as search:
        q = input("Put the conatct name to search: ")
        for contacts1 in search:
            if q in contacts1:
                print(contacts1)
    print("\n")
    main()

def get_all_contacts():
    with open("contact.txt","r") as check_list:
        for contacts6 in check_list:
            contacts6 = contacts6.rstrip()
            print(contacts6)
    print("\n")        
    main()


def update_contacts():
    with open("contact.txt") as update:
        u = input("Enter the contact to be edited:")
        for contacts3 in update:
            contacts3=contacts3.rstrip()
            if u in contacts3:
                print(contacts3)
                string = contacts3.split(" ")
                v = input("The info to be replaced: ")
                k = input("Enter desired change: ")
                string[string.index(v)]= k
                m = ""
                for i in string:
                    string1 = m + i +" "
                    m = string1

    with open("contact.txt") as updated_list:
        final = []
        for contats in updated_list:
            contats = contats.rstrip()
            if u not in contats:
                final.append(contats)
    final.append(m)    

    with open("contact.txt","w") as updated_list:
        for i in final:
            ab = i + "\n"
            updated_list.write(ab)
    print("\n")
    main()


def delete_contact():
    with open("contact.txt") as delete:
        flst=[]
        u = input("Enter the contact to be deleted:")
        print("The contact of ",u," is to be deleted.")
        for contacts3 in delete:
            contacts3=contacts3.rstrip()
            if u not in contacts3:
                flst.append(contacts3)
    
    with open("contact.txt","w") as uplist:
        for i in flst:
            fl = i + "\n"
            uplist.write(fl)
    main()
    print("\n")

main()