#!/usr/bin/python3

from tkinter import *

""" CODESOFT INTERNSHIP PYTHON PROJECT 
        TO_DO LIST PROJECT """
root = Tk()
root.title("MY Todo List Application")
root.geometry("400x500")
root.config(bg='Blue')

"""Create a label for the application"""
label = Label(root, bg='Blue', font=("Comic Sans MS", 15), text='Tasks are Here :)')
label.place(x=100, y=5)

"""Create a listbox widget to display all tasks"""
tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=15, width=30)
tasks.place(x=35, y=40)

"""Create a scrollwheel for viewing tasks"""
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=325, y=40, height=303)
tasks.config(yscrollcommand=scroller.set)

"""Fill Listbox or tasks field with tasks"""
with open('tasks.txt', mode='r+', encoding='utf-8') as tasks_file:
    for task in tasks_file:
        tasks.insert(END, task.strip('\n'))

"""Create a textfield for user to type tasks"""
new_entry = Entry(root, width=35)
new_entry.place(x=45, y=380)

def add_task(entry, listsbox):
    """
    this function adds a tasks to the task listbox which it got from the entry field
    """
    new_task = entry.get()
    listsbox.insert(END, new_task)

    with open('tasks.txt', mode='a', encoding='utf-8') as tasks_file:
        tasks_file.write(f"\n{new_task}")

def delete_task(all_tasks):
    """
    This function deletes a selected task from the tasks lists or listbox
    """
    selected_task = all_tasks.get(ACTIVE)
    all_tasks.delete(ACTIVE)

    with open('tasks.txt', mode='r+', encoding='utf-8') as tasks_file:
        lines = tasks_file.readlines()
        tasks_file.seek(0)
        tasks_file.truncate()

        new_lines = [line.strip('\n') for line in lines if line.strip('\n') != selected_task]

        tasks_file.write("\n".join(new_lines))

"""create buttons for adding and deleting tasks"""
add_button = Button(root, text="ADD TASK", width=10, bg="Green", font=('Helvetica', 12), command=lambda: add_task(new_entry, tasks))
add_button.place(x=45, y=430)

del_button = Button(root, text="DELETE TASK", width=10, bg="Red", font=('Helvetica', 12), command=lambda: delete_task(tasks))
del_button.place(x=200, y=430)

root.update()
root.mainloop()
