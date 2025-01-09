import tkinter as tk
from tkinter import simpledialog

def add_note():
    # Create a new window for the sticky note
    note_window = tk.Toplevel(root)
    note_window.title("Sticky Note")
    note_window.geometry("200x200")

    # Text widget to write the note
    text_widget = tk.Text(note_window, wrap=tk.WORD)
    text_widget.pack(expand=True, fill=tk.BOTH)

    # Close button
    def close_note():
        note_window.destroy()

    close_button = tk.Button(note_window, text="Close", command=close_note)
    close_button.pack()

# Main application window
root = tk.Tk()
root.title("Sticky Notes")
root.geometry("300x200")

# Add button to create a new sticky note
add_button = tk.Button(root, text="Add Note", command=add_note)
add_button.pack(pady=20)

# Start the application
root.mainloop()
