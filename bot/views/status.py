from instance import chat
from controllers.helper import set_menu


def upload_profile_success(sender_id):
    menus = [
        ["Qui suis-je", "whoiam"],
        ["Ajouter mon profil", "start"]
    ]
    chat.persistent_menu(sender_id, menu=set_menu(menus))
    text = """Profile enregistrée\n\nOn vous recontactera plus tard pour un poste qui vous conviendra."""
    chat.send_text(sender_id, text=text)

def exit(sender_id, status="exit"):
    text="Merci d'être passer utiliser nos services, ce fut un plaisir. 🙂😊"
    if status == "stop":
        text = "Merci d'être passer, ce fut un plaiser. 🙂😊"
    chat.send_text(sender_id, text=text) 