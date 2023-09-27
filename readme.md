# Projet MLOps
## Membres
- Samuel Bonnet
- Stanley Schillaci
## Installation
- `pip install -r requirements.txt`
- `python3 app.py`
## Documentation

### Utilisation de l'API

Notre application offre une API simple à utiliser pour la correction grammaticale de textes. Voici comment utiliser l'API :

#### Requête POST

Vous pouvez envoyer une requête POST à l'adresse `http://localhost:5000/correct` pour obtenir une correction grammaticale pour votre texte. La requête doit être au format JSON et contenir deux champs : "string" et "email".

- `string` (obligatoire) : Cette chaîne de caractères contient le texte que vous souhaitez corriger grammaticalement.

- `email` (obligatoire) : Vous devez spécifier votre adresse e-mail, afin que nous puissions verifier que vous êtes bien un utilisateur autorisé à utiliser notre API.

Exemple de requête JSON :
```json
{
    "string": "Ho ar yu ?",
    "email": "user@host.fr"
}
```
Dans un terminal :
`curl -X POST -H "Content-Type: application/json" -d '{"string":"...", "email":"..."}' http://localhost:5000/correct`

#### Réponses possibles
L'API renverra les réponses suivantes en fonction des situations :

- Si la requête est valide et que l'adresse e-mail est correcte, l'API renverra une réponse JSON contenant la chaîne corrigée :

```json
{
    "corrected_string": "How are you?"
}
```

- Si la requête est valide mais l'adresse e-mail n'est pas correcte (ne se termine pas par "epita.fr"), l'API renverra une réponse d'erreur avec un message explicatif :

```json
{
    "error": "Invalid email address"
}
```

- Si la requête est incorrecte (par exemple, le champ "string" est manquant), l'API renverra une réponse d'erreur avec un message explicatif :

```json
{
    "error": "Missing 'string' field in the request JSON"
}
```

- Si la requête contient des champs supplémentaires non autorisés, l'API renverra une réponse d'erreur avec un message explicatif :

```json
{
    "error": "Unexpected field 'foo' in the request JSON"
}
```

### Utilisation de l'interface

Utiliser par exemple l'application [Insomnia](https://insomnia.rest/)
- Envoyer la requête POST à l'adresse `http://localhost:5000/correct` avec le contenu suivant :
```json
{
    "string": "...",
    "email": "...@..."
}
```