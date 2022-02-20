from tkinter import *
import pyperclip
import json
from tkinter import messagebox
from code import Code
code = Code()

class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        self.canvas = Canvas(height=200, width=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)
        #labels
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(row=2, column=0)
        self.password_label = Label(text="Password:")
        self.password_label.grid(row=3, column=0)
        #entries
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()
        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, )
        self.email_entry.insert(0, "isselmou@gmail.com")
        self.password_entry = Entry(width=35)
        self.password_entry.grid(row=3, column=1)
        #buttons

        self.generate_password_button = Button(text="Generate Password", command=self.insert_password, width=20)
        self.generate_password_button.grid(row=3, column=2)

        self.add_button = Button(text="Add", width=30, command=self.save)
        self.add_button.grid(row=4, column=1, )

        self.search_button = Button(text="search", width=20, command=self.search)
        self.search_button.grid(row=1, column=2)

        self.window.mainloop()

    ####################
    def insert_password(self):
        self.password = "".join(code.password_shuffle())
        self.password_entry.insert(0, self.password)
        pyperclip.copy(self.password)

    def save(self):
        website = self.website_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            #pass
        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                self.website_entry.delete(0, END)
                self.password_entry.delete(0, END)

    def search(self):
        website = self.website_entry.get()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Opps", message="sorry website not found :(")

        else:
            if website in data:
                messagebox.showinfo(website,
                                    message=f"email: {data[website]['email']}\n password: {data[website]['password']}")
            else:
                messagebox.askokcancel(title="Opps", message="sorry website not found :(")
