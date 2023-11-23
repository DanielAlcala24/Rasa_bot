from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nombre = tracker.get_slot("nombre")
        correo = tracker.get_slot("correo")
        edad = tracker.get_slot("edad")
        nacimiento = tracker.get_slot("nacimiento")
        numero = tracker.get_slot("numero")
        horario = tracker.get_slot("horario")
        estudio = tracker.get_slot("estudio")
        constancia = tracker.get_slot("constancia")
        rfc = tracker.get_slot("rfc")

        dispatcher.utter_message(text=f"""{nombre}, tus datos han sido enviados: correo: {correo}, edad: {edad}, fecha de nacimiento: {nacimiento},
                                 numero telefónico: {numero}, horario: {horario}, ¿se encuentra estudiando?: {estudio}, constancia: {constancia}, 
                                 rfc: {rfc}""")

        return []
