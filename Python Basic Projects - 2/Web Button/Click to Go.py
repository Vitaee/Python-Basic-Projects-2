import tkinter as tk
import webbrowser as wb

def open_page(page):
    wb.open(page)

window = tk.Tk()
button = tk.Button(
    text='facebook',
    command=lambda *a: open_page('http://www.facebook.com.tr'))
button.pack()

button1 = tk.Button(
        text = 'google',
        comman = lambda *a: open_page("http://www.google.com.tr"))
button1.pack()

window.mainloop()