import ampalibe
import json
import os
from .helper import action, set_menu, is_valid_file, get_private_file
from schemas.user import User
from views.prompt import prompt, prompt_date, prompt_academic_levels
from views.error import send_error_input as send_error
import views.introduce as introduceviews
from views.menu import add_menu
from views.status import upload_profile_success
from services.xano import create_profile_service
from instance import query
from views.history import set_action_history

user = None

def load_temp(messenger_id):
    try:
        global user
        file = get_private_file(messenger_id)
        with open(file, "r") as file_temp:
            temp_data = json.load(file_temp)
            if not user:
                if temp_data.get('messenger_id', None) and temp_data.get('name', None):
                    user = User(messenger_id=temp_data['messenger_id'], name=temp_data['name'])
                else:
                    return None
            else:
                if temp_data.get('first_name', None):
                    ok = user.set_name(first_name=temp_data['first_name'])
                    if not ok:
                        return None
                    
                if temp_data.get('birthday', None):
                    ok = user.set_birthday(temp_data['birthday'])
                    if not ok:
                        return None
                    
                if temp_data.get('academic_levels', None):
                   for level in temp_data['academic_levels']:
                        ok = user.add_academic_level(level)
                        if not ok:
                            return None
                        
                if temp_data.get('speciality', None):
                    ok = user.set_speciality(temp_data['speciality'])
                    if not ok:
                        return None

                if temp_data.get('last_occupation', None):
                    ok = user.set_last_occupation(temp_data['last_occupation'])
                    if not ok:
                        return None
                    
                if temp_data.get('cv_url', None):
                    ok = user.upload_cv(temp_data['cv_url'])
                    if not ok:
                        return None
                    
            return user
    except:
        return None

def update_temp(messenger_id):
    global user
    temp_data = {}
    file = get_private_file(messenger_id)
    
    if user.get_messenger_id():
        temp_data['messenger_id'] = user.get_messenger_id()

    if user.name:
        temp_data['name'] = user.name
    
    if user.first_name:
        temp_data['first_name'] = user.first_name

    if len(user.academic_levels) > 0:
        temp_data['academic_levels'] = user.academic_levels

    if user.speciality:
        temp_data['speciality'] = user.speciality

    if user.last_occupation:
        temp_data['last_occupation'] = user.last_occupation

    if user.cv_url:
        temp_data['cv_url'] = user.cv_url

    with open(file, "w") as file_temp:
        json.dump(temp_data, file_temp, indent=4)

def del_user_temp(messenger_id):
    file = get_private_file(messenger_id)
    try:
        os.remove(file)
        return True
    except FileNotFoundError:
        print("File temp not found")
        return False
    except:
        return None
    
def continue_prompt(sender_id):
    last_action = query.get_temp(sender_id, 'last_action')

    match last_action:
        case "name":
            # if last action is set to name and not user
            # means user accept to start register profile but doesn't provide any information yet
            prompt(sender_id, text="Entrer votre nom: ", action="setname")
            pass
        
        case "first_name":
            prompt(sender_id, text="Entrer votre prénom: ", action="setfirstname")
            pass
        
        case "birthday":
            next_text="Entrer votre date de naissance"
            next_action="setbirthday"
            prompt_date(sender_id, text=next_text, action=next_action)
            pass

        case "academic_levels":
            next_action="setacademiclevels"
            prompt(sender_id, text="Entrer votre niveau d'études", action="setacademiclevels")
            pass
        
        case "speciality":
            next_input_text =  "Veuillez saisir votre spécialité ?"
            next_action = "setspeciality"
            # next step: get the last occupation / experience of the user
            prompt(sender_id, text=next_input_text, action=next_action)
            pass
        
        case "last_occupation":
            next_input_text = "Raconter votre dernière expérience professionnelle(intitulé du poste, fonction, compétences acquises, etc): " 
            next_action = "setlastoccupation"
            # next step: get the last occupation / experience of the user
            prompt(sender_id, text=next_input_text, action=next_action)
            pass

        case "cv":
            next_input_text = """Mettre votre CV en pièce jointe.\n\nN.B: Sous format image ou PDF."""
            next_action = "uploadcv"
            # next step : upload CV
            prompt(sender_id, text=next_input_text, action=next_action)
            pass
        
        case _ :
            send_error(sender_id, "Oh, il y a un problème sur cette action")
            return None
# helpers    
def get_user(messenger_id):
    global user
    return user if user else load_temp(messenger_id)

def create_user(messenger_id, name):
    global user
    user = User(messenger_id, name)
    return user

@ampalibe.action(action("setname"))
def set_username(sender_id, cmd, **ext):
    name = cmd
    create_user(messenger_id=sender_id, name=name)
    # next step: get user first name
    prompt(sender_id, text="Entrer votre prénom: ", action="setfirstname")
    update_temp(sender_id)
    set_action_history(sender_id, "firstname")
    

@ampalibe.action(action("setfirstname"))
def set_firstname(sender_id, cmd, **ext):
    user = get_user(sender_id)
    first_name = cmd
    next_text = "Entrer votre date de naissance"
    next_action = "setbirthday"
    ok = user.set_name(first_name=first_name) 
    if not ok:
        next_text = "Veuillez entrer un prénom correct: "  
        next_action = "setfirstname"   
    # next step: get user birthday
    prompt_date(sender_id, text=next_text, action=next_action)
    update_temp(sender_id)
    set_action_history(sender_id, "birthday")

@ampalibe.action(action("setbirthday"))
def set_birthday(sender_id, cmd, **ext):
    user = get_user(sender_id)
    birthday = cmd
    next_text = ""
    next_action = "setacademiclevels"
    ok = user.set_birthday(birthday)
    if not ok:
        next_text = "Entrer votre date de naissance"
        next_action = "setbirthday"   
        return prompt_date(sender_id, text=next_text, action=next_action, retrying=True)
    
    # next step: get user academic levels
    introduceviews.academic_levels(sender_id, action=next_action)
    update_temp(sender_id)
    set_action_history(sender_id, "academic_levels")

@ampalibe.action(action("setacademiclevels"))
def set_academic_levels(sender_id, cmd, **ext):
    user = get_user(sender_id)
    level = cmd
    academic_level_action = "setacademiclevels"
    menus = [
        ["S'arrêter", "stopalrecords"], # al for academic levels/ means stop academic level records
        ["Quitter", "exit"], 
    ]
    user.add_academic_level(level)
    persistence_menu = set_menu(menus)
    add_menu(sender_id, persistence_menu)
    prompt_academic_levels(sender_id, action=academic_level_action)
    update_temp(sender_id)

@ampalibe.action(action("setspeciality"))
def set_speciality(sender_id, cmd, **ext):
    user = get_user(sender_id)
    speciality = cmd
    next_input_text = "Raconter votre dernière expérience professionnelle(intitulé du poste, fonction, compétences acquises, etc): " 
    next_action = "setlastoccupation"
    ok = user.set_speciality(speciality)
    if not ok:
        next_input_text =  "Veuillez saisir votre spécialité ?"
        next_action = "setspeciality"
    # next step: get the last occupation / experience of the user
    prompt(sender_id, text=next_input_text, action=next_action)
    update_temp(sender_id)
    set_action_history(sender_id, "last_occupation")

@ampalibe.action(action("setlastoccupation"))
def set_last_occupation(sender_id, cmd, **ext):
    user = get_user(sender_id)
    last_occupation = cmd 
    next_input_text = """Mettre votre CV en pièce jointe.\n\nN.B: Sous format image ou PDF."""
    next_action = "uploadcv"
    ok = user.set_last_occupation(last_occupation)
    if not ok:
        next_input_text = "Veuillez saisir votre dernière expérience professionnelle(intitulé du poste, fonction, compétences acquises, etc)."
        next_action = "setlastoccupation"
    # next step : upload CV
    prompt(sender_id, text=next_input_text, action=next_action)
    update_temp(sender_id)
    set_action_history(sender_id, "cv")

@ampalibe.action(action("uploadcv"))
def upload_cv(sender_id, cmd, **ext):
    user = get_user(sender_id)
    cv_url = cmd
    if is_valid_file(cv_url):
        user.upload_cv(cv_url)
        update_temp(sender_id)

        if user.is_ready():
            # todo: save to db
            status = create_profile_service(user)
            if status == "OK":
                upload_profile_success(sender_id)
                # remove the file temp maintaining user info
                del_user_temp(sender_id)
                query.del_temp(sender_id, 'last_action')
        else:
            print("profile is not ready yet")
            print(user.parse())

    else:
        next_action = "uploadcv"
        send_error(sender_id, "Les fichiers valides sont les fichiers image(png, jpg, etc) et PDF.", action=next_action)


    