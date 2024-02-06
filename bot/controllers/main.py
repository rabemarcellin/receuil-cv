import ampalibe
from instance import chat
from .helper import command, set_menu
from views.get_started import get_started, self_presentation
from views.prompt import prompt
from views.status import exit as exitstatusview
from views.introduce import prevent_exit
from views.history import set_action_history
from .user import continue_prompt

chat.get_started()

@ampalibe.command(command("root")) 
def main(sender_id, cmd, **ext):
    #todo: voir dans les historiques, et récuperer les anciens données de l'utilisateur
    # fournies dans les 7 dernières jours
    # Les présenter, et leur demander ensuite de continuer avec ses données ou bien de 
    # revenir au tout début
    menus = [
        ["Qui sommes-nous ?", "whoiam"],
        ["Ajouter mon profil", "start"]
    ]
    chat.persistent_menu(sender_id, menu=set_menu(menus), composer_input_disabled=False)
    get_started(sender_id)

@ampalibe.command(command("whoiam"))
def who_i_am(sender_id, cmd, **ext):
    self_presentation(sender_id)

@ampalibe.command(command("exit"))
def exit(sender_id, cmd, **ext):
    if not ext.get("stop", None):
        prevent_exit(sender_id)
    else:
        exitstatusview(sender_id, status="stop")
        menus = [
            ["Qui sommes-nous ?", "whoiam"],
            ["Ajouter mon profil", "start"]
        ]
        chat.persistent_menu(sender_id, menu=set_menu(menus), composer_input_disabled=False)

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
    set_action_history(sender_id, "name")
    menus = [
        ["Quitter", "exit"] 
    ]
    chat.persistent_menu(sender_id, menu=set_menu(menus), composer_input_disabled=False)
    # prompt user name
    prompt(sender_id, text="Entrer votre nom: ", action="setname")

@ampalibe.command(command("stopalrecords"))
def stop_al_records(sender_id, cmd, **ext):    
    # todo: prompt speciality
    menus = [
        ["Quitter", "exit"] 
    ]
    chat.persistent_menu(sender_id, menu=set_menu(menus), composer_input_disabled=False)
    prompt(
        sender_id, 
        text="""Quelle est votre spécialité ?\n\nExemple: Expert comptable""",
        action="setspeciality"
    )
    set_action_history(sender_id, "speciality")


@ampalibe.command(command("confirmexit"))
def confirm_exit(sender_id, cmd, **ext):
    exitstatusview(sender_id)
    menus = [
        ["Qui sommes-nous ?", "whoiam"],
        ["Ajouter mon profil", "start"]
    ]
    chat.persistent_menu(sender_id, menu=set_menu(menus), composer_input_disabled=False)

@ampalibe.command(command("cancelexit"))
def continue_profile_registration(sender_id, cmd, **ext):
    continue_prompt(sender_id)