from url_parse_backend import pretty_parse
import validators
import tkinter
from tkinter import ttk

def on_button_click():
    try:
        url = main_window.clipboard_get()
    except Exception as err:
        return None
    
    if not validators.url(url):
        label.config(text='copy a valid URL')
        return None
    
    label.config(text=pretty_parse(url))
    button.config(text='parse again')

main_window = tkinter.Tk()
main_window.title("URL Parser")

frame = ttk.Frame(master=main_window, padding=20)
frame.grid(row=0)

label = ttk.Label(master=frame, text="Copy URL to parse")
label.grid(row=1)

button = ttk.Button(master=frame, text="parse", command=on_button_click)
button.grid()

main_window.mainloop()