# SDK de Mercado Pago
import mercadopago
from models.doc import docs
# Agrega credenciales
sdk = mercadopago.SDK("TEST-4380247365218310-113004-fa931dc5daae26734502e0d1b04a7862-620160466")
          
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