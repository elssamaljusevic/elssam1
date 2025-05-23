# Application Streamlit : Espaces de Coworking à Paris
  
Ce site a pour objectif de visualiser les espaces de coworking situés à Paris à partir des données publiques disponibles sur le site [leportagesalarial.com](https://www.leportagesalarial.com/coworking/).
  
Il permet de mettre en œuvre les compétences suivantes :

- Scraping web avec `requests`, `PyQuery` et `BeautifulSoup`

- Visualisation cartographique avec `Folium`
- Création d’une interface web avec `Streamlit`
- Analyse statistique (répartition géographique)

---

## Structure du projet

| Fichier | Rôle |
|--------|------|
| `scraper.py` | Extrait les données des espaces de coworking depuis le site web |
| `clean_data.py` | Géocode les adresses et ajoute les colonnes latitude / longitude |
| `application.py` | Affiche la carte interactive, la barre de recherche et les graphiques |
| `requirements.txt` | Liste des bibliothèques nécessaires à l'exécution |
| `coworking_data.csv` | Fichier final avec les données enrichies (généré automatiquement) |

---

## Exécution

### 1. Installation des dépendances

Exécutez :

pip install -r requirements.txt
### 2. Extraction des données

Lancez le script de scraping pour récupérer les adresses des coworkings :


python scraper.py

### 3. Géocodage des adresses

Ajoute les coordonnées GPS pour chaque adresse :


python clean_data.py


### 4. Démarrage de l’application

Lancez Streamlit pour afficher la carte et les statistiques :


streamlit run application.py

---

## 📊 Fonctionnalités de l’application

- **Barre de recherche** : permet de filtrer par nom ou adresse
- **Carte interactive** : chaque coworking est un point cliquable avec lien
- **Statistiques** : graphique de répartition par arrondissement
- **Coordonnées GPS** : géocodage automatique des adresses

---

## Technologies utilisées

- Python 3
- Streamlit
- Folium
- Geopy
- Pandas
- PyQuery / Requests
- Matplotlib
"# elssamaljusevic" 
#   e l s s a m 1  
 