to_do = []

def add():
    print("\n")
    task=input("Add the task: ")
    no_task = str(len(to_do)+1)
    work = no_task + ". " + task + "❌ "
    to_do.append(work)
    main()

def delete():
    print("\n")
    delt = input(" ⚠️ If you DO NOT want to delete any work from TO-Do list Enter 0 \n ⚠️ If you want to CLEAR all the content in TO-DO list Enter 00 \n ⚠️ If you want to delete specific task , Enter task number\n")
    if delt == "0":
        main()
    elif delt == "00":
        to_do.clear()
        main()
    else :
        no_work_delt = int(delt)-1
        to_do.remove(to_do[no_work_delt])

        for index in range(len(to_do)):
            if (index >= no_work_delt):
                string=to_do[index]
                [N,W] =string.split(".")
                M = str(int(N)-1)
                to_do[index] = M + "." + W
    main()

def done():
    print("\n")
    compl_task = int(input("Enter the task Number Which has been Completed: "))-1
    strng = to_do[compl_task]
    [dn,nm] = strng.split("❌")
    up_task = dn + " ✅"
    to_do[compl_task]= up_task
    main()


def view():
    print("\n")
    for i in to_do:
        print(i)
    main()



def main():
    print("\n")
    print("\n")
    print("➕  TO ADD the task Enter 0: ")
    print("📋  TO VIEW the list Enter 1: ")
    print("⛔  To DELETE the task Enter 2: ")
    print("✅  TO mark the COMPLETED task Enter 3: ")

    n = int(input("What to do: "))
    
    if n == 0:
        add()
    elif n == 1:
        view()
    elif n == 2 :
        delete()
    elif n == 3:
        done()    
main()


