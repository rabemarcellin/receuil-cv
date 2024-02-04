import ampalibe
from instance import chat
from .helper import command, action
from views.get_started import get_started
from views.prompt import prompt


chat.get_started()

@ampalibe.command(command("root"))
def main(sender_id, cmd, **ext):
    #todo: voir dans les historiques, et récuperer les anciens données de l'utilisateur
    # fournies dans les 7 dernières jours
    # Les présenter, et leur demander ensuite de continuer avec ses données ou bien de 
    # revenir au tout début
    get_started(sender_id)

@ampalibe.command(command("start"))
def start(sender_id, cmd, **ext):
    '''
    start records user information that are:
        - name
        - first name(not required)
        - birthday
        - academic levels(fr: niveau d'études)
        - speciality
        - last_occupation(last experience)
        - cv(as PDF or image format)
    '''
    # prompt user name
    prompt(sender_id, text="Entrer votre nom: ", action="setname")

@ampalibe.command(command("stopalrecords"))
def stop_al_records(sender_id, cmd, **ext):
    # remove persistent menu, 
    menus = [
        ["Quitter", "exit"] # al for academic levels/ means stop academic level records
    ]
    chat.persistent_menu(sender_id, menus, composer_input_disabled=False)
    # todo: prompt speciality
    prompt(sender_id, text="Quelle est votre spécialité ?", action="setspeciality")