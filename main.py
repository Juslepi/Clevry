import urllib.parse

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

mapUrl = input("URL: ")

mapUrl = clean_url(mapUrl)
mapUrl = keep_cleaning(mapUrl)

print("\n")
print(f'Sathva asennukset \nAjoreitti: {urllib.parse.unquote(mapUrl)}')

input("\n Enter to continue")