"""
This is a program for storing book information:
Title; Author
Year; ISBN

The user can (by pressing the button):
View all records, Search an record, Add a new record,
Update selected records, Delete selected records or Close the program
"""

from tkinter import *
from backend import Database

database = Database("books.db")


class Window:
    def __init__(self, window):

        # Title
        l1 = Label(window, text="    Title:")
        l1.grid(row=0, column=0)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        # Author
        l2 = Label(window, text="  Author:")
        l2.grid(row=0, column=2)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        # Year
        self.l3 = Label(window, text="    Year:")
        self.l3.grid(row=1, column=0)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        # ISBN
        self.l4 = Label(window, text="      ISBN:")
        self.l4.grid(row=1, column=2)

        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        # List of books
        self.list1 = Listbox(window, height=8, width=30)
        self.list1.grid(row=3, column=0, rowspan=6, columnspan=2)

        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=3, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons
        self.b1 = Button(window, text="View All", width=12, command=self.view_command)
        self.b1.grid(row=3, column=3)

        self.b2 = Button(window, text="Search Entry", width=12, command=self.search_command)
        self.b2.grid(row=4, column=3)

        self.b3 = Button(window, text="Add Entry", width=12, command=self.add_command)
        self.b3.grid(row=5, column=3)

        self.b4 = Button(window, text="Update Selected", width=12, command=self.update_command)
        self.b4.grid(row=6, column=3)

        self.b5 = Button(window, text="Delete Selected", width=12, command=self.delete_command)
        self.b5.grid(row=7, column=3)

        self.b1 = Button(window, text="Close", width=12, command=window.destroy)
        self.b1.grid(row=8, column=3)

        window.wm_title("Bookstore")

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            print(self.list1.get(index))
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(), self.year_text.get(), self.isbn_text.get(), self.author_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


window = Tk()
Window(window)
window.mainloop()