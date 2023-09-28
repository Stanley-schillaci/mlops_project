from flask import Flask, request, jsonify
import re  # Pour la validation de l'e-mail
import torch
from transformers import BartTokenizer, BartForConditionalGeneration

app = Flask(__name__)

model_name = 'pszemraj/bart-base-grammar-synthesis'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Fonction de validation de l'e-mail
def is_valid_email(email):
    # Utilisation d'une expression régulière simple pour vérifier si l'e-mail se termine par "epita.fr"
    return re.search(r'@epita\.fr$', email) is not None

def correct_text(input_text):
    inputs = tokenizer(input_text, return_tensors='pt')
    generated_ids = model.generate(**inputs)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

@app.route('/correct', methods=['POST'])
def correct():
    try:
        data = request.get_json()
        email = data.get('email', '')

        # Vérifiez d'abord l'e-mail
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email address"}), 400  # Spécifiez le code d'erreur HTTP 400
        
        # Vérifiez la présence du champ "string" dans la requête JSON
        if 'string' not in data:
            return jsonify({"error": "Missing 'string' field in the request JSON"}), 400  # Spécifiez le code d'erreur HTTP 400
        
        # Vérifiez qu'il n'y a pas de champs supplémentaires dans la requête JSON
        allowed_fields = ['string', 'email']
        for field in data:
            if field not in allowed_fields:
                return jsonify({"error": f"Unexpected field '{field}' in the request JSON"}), 400  # Spécifiez le code d'erreur HTTP 400
        
        input_text = data['string']

        # Ensuite, effectuez la correction de texte
        corrected_text = correct_text(input_text)
        response = {"corrected_string": corrected_text}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Spécifiez le code d'erreur HTTP 500 pour les erreurs internes du serveur

if __name__ == '__main__':
    app.run(debug=True)
