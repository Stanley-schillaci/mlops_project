# Projet MLOps
## Membres
- Samuel Bonnet
- Stanley Schillaci
## Installation
- `pip install -r requirements.txt`
- `python3 app.py`
## Utilisation de l'API
- `curl -X POST -H "Content-Type: application/json" -d '{"string":"...", "email":"..."}' http://localhost:5000/correct`
## Utilisation de l'interface
Utiliser par exemple l'application [Insomnia](https://insomnia.rest/)
- Envoyer la requête POST à l'adresse `http://localhost:5000/correct` avec le contenu suivant :
```json
{
    "string": "...",
    "email": "...@..."
}
```
