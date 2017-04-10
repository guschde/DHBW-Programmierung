#!/usr/bin/python3
# encoding=utf-8
import ToDoItem
'''

Implementierung einer einfachen ToDo Liste

'''
pathtonotes = "./data/todo.tasks"


# Datei auslesen
def read_data_from_file(path):
    f = open(path)
    tasks = []
    for lines in f:
        t = lines.rstrip().split(";")
        tasks.append(ToDoItem.ToDoItem(t[0],t[1]))
    return tasks


# Datei schreiben
def write_data(path, tasks, append):
    # Zeilenweise schreiben
    if append == True:
        f = open(path, 'a')
    else:
        # ersetzen
        f = open(path, 'w')
    task = ""
    for t in tasks:
        task += t.export()
    f.write(task)
    f.close()


# Tabelle ausgeben
def print_data(data):
    print("NR\tTermin \t \t Aufgabe")
    print("_______________________________________")
    for i in range(len(data)):
        print(i, " ", end="")
        data[i].display()
        print("_______________________________________")


# Datenreihe löschen
def delete_data(id):
    data = read_data_from_file(pathtonotes)
    data.remove(data[id])
    write_data(pathtonotes, data, False)

def edit_task(id):
    data = read_data_from_file(pathtonotes)
    taskname = str(input("Bitte neue Tätigkeit angeben: "))
    taskdate = str(input("Bitte neues Datum angeben: "))
    data[id] = ToDoItem.ToDoItem(taskdate,taskname)
    write_data(pathtonotes, data, False)


# Menüpunkt hinzufügen
def write_new_task():
    temp = ToDoItem.ToDoItem("","")
    temp.setTaskname(str(input("Bitte Tätigkeit angeben: ")))
    temp.setTaskdate(str(input("Bitte Datum angeben: ")))

    write_data(pathtonotes, [temp], True)

def edit_existing_task():
    print_data(read_data_from_file(pathtonotes))
    taskedit = int(input("Bitte ID angeben: "))
    edit_task(taskedit)

# Menüpunkt löschen
def delete_task():
    print_data(read_data_from_file(pathtonotes))
    taskdel = int(input("Bitte ID angeben: "))
    delete_data(taskdel)


# Hauptfunktion
def main_function():
    while True:


        userinput = str(input("Neu Notiz hinzufügen (n), Notiz löschen (l), Programm beenden (q), Notiz bearbeiten (b): "))
        userinput = userinput.lower()
        if userinput == "q":
            exit()
        elif userinput == "n":
            write_new_task()
        elif userinput == "l":
            delete_task()
        elif userinput == "b":
            edit_existing_task()
        else:
            print("Bitte korrekten Wert angeben!")
        print_data(read_data_from_file(pathtonotes))



main_function()
