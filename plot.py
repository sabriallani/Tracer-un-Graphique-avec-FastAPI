from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import matplotlib.pyplot as plt
import os

app = FastAPI()

# Assurez-vous que le dossier "static" existe avant de le monter
if not os.path.exists("static"):
    os.makedirs("static")

# Configurer un dossier pour les fichiers statiques (pour stocker les images de graphiques)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/plot", response_class=HTMLResponse)
async def plot_form():
    print("Serving form for plotting...")  # Log pour vérifier que la route est atteinte
    # Page HTML pour envoyer des données à tracer
    return """
    <html>
        <head>
            <title>Tracer un Graphique</title>
        </head>
        <body>
            <h1>Tracer un Graphique avec FastAPI</h1>
            <form action="./plot" method="post">
                <label for="values">Entrez une liste de valeurs (séparées par des virgules) :</label><br>
                <input type="text" id="values" name="values"><br><br>
                <input type="submit" value="Tracer">
            </form>
        </body>
    </html>
    """

@app.post("/plot", response_class=HTMLResponse)
async def create_plot(values: str = Form(...)):
    try:
        print(f"Received values: {values}")  # Log des valeurs reçues
        # Convertir la chaîne de caractères en une liste de valeurs
        values_list = [float(v.strip()) for v in values.split(",")]

        # Créer un graphique avec matplotlib
        plt.figure()
        plt.plot(values_list, marker="o")
        plt.xlabel("Index")
        plt.ylabel("Valeur")
        plt.title("Graphique des Valeurs Entrées")

        # Sauvegarder le graphique sous forme d'image
        plot_path = "static/plot.png"
        plt.savefig(plot_path)
        plt.close()

        print(f"Graph saved at: {plot_path}")  # Log pour vérifier que l'image est sauvegardée

        # Retourner la page HTML avec le graphique affiché
        return f"""
        <html>
            <head>
                <title>Résultat du Graphique</title>
            </head>
            <body>
                <h1>Graphique Généré</h1>
                <img src="/static/plot.png" alt="Graphique">
                <br><br>
                <a href="/plot">Revenir en arrière</a>
            </body>
        </html>
        """
    except ValueError:
        print("Erreur : Valeurs non valides fournies")  # Log en cas d'erreur de conversion
        return """
        <html>
            <head>
                <title>Erreur</title>
            </head>
            <body>
                <h1>Erreur : Veuillez entrer des valeurs valides séparées par des virgules.</h1>
                <a href="/plot">Revenir en arrière</a>
            </body>
        </html>
        """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
