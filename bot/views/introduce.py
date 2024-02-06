from instance import chat, query
from .quick_reply.send_options import send_options
from controllers.helper import action as set_action
introduce_text = """Hello, je suis Receuil CV. Un bot messenger
qui va vous guider dans vos recherches d'emploie. Nous allons parcourir
ensemble un ensemble de chemin pour vous créer un profil de consultant
d'entreprise à votre domaine.
"""

def introduce(sender_id):
    chat.send_text(sender_id, introduce_text)

def prevent_exit(sender_id):
    options = ["confirmexit", "cancelexit"]
    chat.send_text(sender_id, "Nous sommes en train vous constituer un profil professionnel.")
    send_options(sender_id, options=options, title="Voulez-vous vraiment nous quitter ?")

def academic_levels(sender_id, action):
    chat.send_text(
        sender_id, 
        """Nous allons maintenant, vous demander un à un, message par message, votre niveau d'études et votre spécialité.
\nPar exemple: Master II en comptabilité générale, Université d'Antananarivo.
        """
    )
    chat.send_text(sender_id, """Voir menu(☰) et choisir "s'arrêter" pour terminer.""")
    chat.send_text(sender_id, "N.B: 1 niveau d'étude = 1 message")
    query.set_temp(sender_id, "prompt_academic_levels", True)
    query.set_action(sender_id, set_action(action))