import urllib.parse
import os
import module

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_url(url):
    url = url.replace("https://www.google.com/maps/dir/", '')
    
    i = 0
    while url[i] != "@":
        i += 1

    i -= 1        
    
    return url[:i]

def keep_cleaning(url):
    url = url.replace("+", " ")
    url = url.replace("/", " -> ")
    return url

while True:
    clear_console()
    # mapUrl = input("URL: ")
    mapUrl = module.copy_from_clipboard()

    mapUrl = clean_url(mapUrl)
    mapUrl = keep_cleaning(mapUrl)
    
    module.copy_to_clipboard(f"Sathva asennukset\nAjoreitti: {urllib.parse.unquote(mapUrl)}")

    print("\n")
    print(f'Sathva asennukset \nAjoreitti: {urllib.parse.unquote(mapUrl)}')

    input("\nEnter to continue")