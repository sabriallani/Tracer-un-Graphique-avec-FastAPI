
# API FastAPI pour Générer des Graphiques

Cette API permet de tracer des graphiques à partir d'une liste de valeurs fournies par l'utilisateur. Les graphiques sont générés à l'aide de Matplotlib et affichés sur une page HTML.

## Fonctionnalités

- **Page de formulaire** : Entrez une liste de valeurs séparées par des virgules.
- **Génération de graphique** : Les valeurs fournies sont tracées sous forme de graphique.
- **Affichage de graphique** : Le graphique généré est affiché sur une page avec l'image.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants :
- [Python 3.8+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/) (`pip install fastapi`)
- [Uvicorn](https://www.uvicorn.org/) (`pip install uvicorn`)
- [Matplotlib](https://matplotlib.org/) (`pip install matplotlib`)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/sabriallani/fastapi-plotting-api.git
   cd fastapi-plotting-api
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

## Structure du Projet

- `main.py` : Fichier principal contenant l'API FastAPI.
- `static/` : Dossier pour stocker les fichiers statiques (images des graphiques).
  
## Utilisation

1. Assurez-vous que le dossier `static` existe, sinon, créez-le :
   ```bash
   mkdir static
   ```

2. Lancez l'application FastAPI :
   ```bash
   uvicorn main:app --reload
   ```

3. Ouvrez votre navigateur et accédez à l'URL suivante pour accéder à la page de soumission des valeurs :
   ```
   http://127.0.0.1:8000/plot
   ```

4. Entrez une liste de valeurs séparées par des virgules (ex : `1, 2, 3, 4, 5`) et cliquez sur "Tracer". Le graphique correspondant sera généré et affiché.

## Exemples

### Exemple d'Entrée

Liste de valeurs : `1, 3, 2, 5, 7`

### Exemple de Résultat

![Graphique généré](static/plot.png)

## Gestion des Erreurs

- Si des valeurs non valides sont fournies, un message d'erreur s'affichera demandant de fournir une liste correcte de nombres.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
