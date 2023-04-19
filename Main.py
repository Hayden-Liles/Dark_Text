import tkinter
import customtkinter

ctk = customtkinter

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("800x800")

# button = CTK.CTkButton(master=app, text="Button")
# button.place(relx=.5, rely=.95, anchor=tkinter.CENTER)



entry = ctk.CTkEntry(master=app, placeholder_text="Type here...", width=600, height=45, border_width=2, corner_radius=10)
entry.place(relx=.5, rely=.95, anchor=tkinter.CENTER)

def get_text(event=None):
    text = entry.get()
    print(text)

entry.bind('<Return>', get_text)



app.mainloop()