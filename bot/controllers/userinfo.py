import ampalibe
from controllers.helper import action, set_menu
from schemas.user import User
from views.prompt import prompt, prompt_date, prompt_academic_levels
from views.error import send_error
import views.introduce as introduceviews
from views.menu import add_menu


user = None

@ampalibe.action(action("setname"))
def set_username(sender_id, cmd, **ext):
    global user
    name = cmd
    user = User(name)
    # next step: get user first name
    prompt(sender_id, text="Entrer votre prénom: ", action="setfirstname")

@ampalibe.action(action("setfirstname"))
def set_firstname(sender_id, cmd, **ext):
    global user
    first_name = cmd
    next_text = "Entrer votre date de naissance"
    next_action = "setbirthday"
    ok = user.set_name(first_name=first_name)
    if not ok:
        send_error(sender_id, error_text="Entrer un format valide.")   
        next_text = "Entrer votre prénom"  
        next_action = "setfirstname"   
    # next step: get user birthday
    prompt_date(sender_id, text=next_text, action=next_action)

@ampalibe.action(action("setbirthday"))
def set_birthday(sender_id, cmd, **ext):
    global user
    birthday = cmd
    next_text = ""
    next_action = "setacademiclevels"
    ok = user.set_birthday(birthday)
    if not ok:
        send_error(sender_id, error_text="Entrer un format valide.")   
        next_text = "Entrer votre date de naissance"
        next_action = "setbirthday"   
        return prompt_date(sender_id, text=next_text, action=next_action)
    
    # next step: get user academic levels
    introduceviews.academic_levels(sender_id, action=next_action)

@ampalibe.action(action("setacademiclevels"))
def set_academic_levels(sender_id, cmd, **ext):
    global user
    level = cmd
    academic_level_action = "setacademiclevels"
    menus = [
        ["OK pour NA", "stopalrecords"] # al for academic levels/ means stop academic level records
    ]
    user.add_academic_level(level)
    persistence_menu = set_menu(menus)
    add_menu(sender_id, persistence_menu)
    prompt_academic_levels(sender_id, action=academic_level_action)
