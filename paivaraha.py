from datetime import datetime
import os
import win32clipboard

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def copy_to_clipboard(string):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(string)
    win32clipboard.CloseClipboard()


now = datetime.now()
date = now.strftime("%d.%m").lstrip("0").replace(".0", ".")

while True:
    clear_console()
    kaupunki = input("Kaupunki: ") 
    string = f"Lähtö kotoa: {date} klo 7.55\nPaluu kotiin: {date} klo 16.00\nTyömatka {kaupunki}\nAsiakas Sathva"
    copy_to_clipboard(string)
    print(f"Lähtö kotoa: {date} klo 7.55")
    print(f"Paluu kotiin: {date} klo 16.00")
    print(f"Työmatka {kaupunki}")
    print("Asiakas Sathva")
    input("Enter to continue")