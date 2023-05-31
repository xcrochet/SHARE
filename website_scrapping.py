import requests
from bs4 import BeautifulSoup

# URL de la page Wikipedia
url = "https://fr.wikipedia.org/wiki/Python_(langage)"

# Envoie une requête HTTP à l'URL
response = requests.get(url)

# Parse le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Cherche tous les titres de sections (balises 'h2') dans le contenu HTML
section_headers = soup.find_all('h2')

# Ouvre un fichier texte en mode écriture
with open("scraping_website_logs.txt", "w", encoding="utf-8") as f:
    # Écrit le contenu HTML brut dans le fichier texte
    f.write(str(soup.prettify()))

    # Pour chaque titre de section, écrit le texte du titre dans le fichier texte
    for header in section_headers:
        f.write(header.text + "\n")

print("Fin de l'extraction des informations.")
