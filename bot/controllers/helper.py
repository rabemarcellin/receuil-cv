from ampalibe import Payload
from ampalibe.ui import Button, Type
from .command.data import commands
from .action.data import actions

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