import pandas as pd
import matplotlib.pyplot as plt

# URL du fichier CSV en ligne
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Utilisation de pandas pour lire le fichier CSV à partir de l'URL
donnees = pd.read_csv(url)

# Affichage des premières lignes du DataFrame
print(donnees.head())

# Création d'un histogramme pour visualiser l'âge des passagers
plt.hist(donnees['Age'].dropna(), bins=30)
plt.xlabel('Age')
plt.ylabel('Fréquence')
plt.title('Distribution des âges des passagers du Titanic')
plt.show()
