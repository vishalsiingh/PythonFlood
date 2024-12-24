from tkinter import Tk
from tkcalendar import Calendar

root = Tk()
root.title("Tkcalendar Example")
root.geometry("400x300")


calendar = Calendar(root, selectmode='day', year=2024, month=1, day=1)
calendar.pack(pady=20)


def show_date():
    selected_date = calendar.get_date()
    print(f"Selected Date: {selected_date}")


from tkinter import Button
Button(root, text="Get Date", command=show_date).pack(pady=10)


root.mainloop()
