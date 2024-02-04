from instance import chat, query
from controllers.helper import action as set_action
introduce_text = """Hello, je suis Receuil CV. Un bot messenger
qui va vous guider dans vos recherches d'emploie. Nous allons parcourir
ensemble un ensemble de chemin pour vous créer un profil de consultant
d'entreprise à votre domaine.
"""

def introduce(sender_id):
    chat.send_text(sender_id, introduce_text)

def academic_levels(sender_id, action):
    chat.send_text(
        sender_id, 
        """Nous allons maintenant, vous demander un à un, message par message, votre niveau d'études
        et votre spécialité.

        Par exemple: Master II en comptabilité générale, Université d'Antananarivo.
        """
    )
    chat.send_text(sender_id, """Vous trouverez sur une option "OK pour NA" dans menu une fois tout ceci faite.""")
    chat.send_text(sender_id, "N.B: 1 niveau d'étude = 1 message")
    query.set_temp(sender_id, "prompt_academic_levels", True)
    query.set_action(sender_id, set_action(action))