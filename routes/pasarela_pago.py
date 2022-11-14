
"""en proceso de desarrollo"""
# SDK de Mercado Pago
import mercadopago
from models.doc import docs
# Agrega credenciales
sdk = mercadopago.SDK("PROD_ACCESS_TOKEN")
          
# Crea un ítem en la preferencia
preference_data = {
    "items": [
        {
            "name": {{docs.doc_name}},
            "author": {{docs.author}},
            "type":{{docs.doc_type}},
            "units": {{docs.units}},
            "unit_price": {{docs.doc_value}}
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
