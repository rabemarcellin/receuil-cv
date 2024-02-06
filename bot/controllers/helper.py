import requests
import os
from ampalibe import Payload
from ampalibe.ui import Button, Type
from .command.data import commands
from .action.data import actions

def get_private_file(messenger_id):
    try:
        current_dir = os.getcwd()
        private_folder= os.path.join(current_dir, 'assets', 'private')

        if not os.path.exists(private_folder):
            os.makedirs(private_folder)
        file = os.path.join(private_folder, f"{messenger_id}.json")
        return file
    except:
        return None

def command(key):
    return commands.get(key, None)

def action(key):
    return actions.get(key, None)

def set_menu(menus):
    '''
    create valid buttons menu for messenger.
    @param menu list[[title: str, cmd: str]]
        title: title of the menu button
        cmd: command key to execute on submit menu button
    '''
    persistent_menu = []
    for menu in menus:
        title, cmd = menu
        persistent_menu.append(
            Button(
                type=Type.postback,
                title=title,
                payload=Payload(
                    command(cmd)
                )
            )
        )
    return persistent_menu

def is_valid_file(url):
    """
    Verify if user file uploaded is in format PDF or Image only
    @returns
        status: bool - Say that file is in the valid format or not
        format_type: str | None - Return the format of the file, get None if invalid 
    """
    try:
        # Send a HEAD request to get the headers without downloading the entire file
        response = requests.head(url)

        # Check the Content-Type header
        content_type = response.headers.get('Content-Type', '').lower()

        # Return the determined file type
        if 'pdf' in content_type:
            return True, "PDF"
        elif 'image' in content_type:
            return True, "image"
        else:
            return None

    except requests.exceptions.RequestException as e:
        return None