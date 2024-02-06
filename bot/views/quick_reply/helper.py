import random
from random import randint
from ampalibe import Payload
from ampalibe.ui import QuickReply
from controllers.helper import command as create_command

def create_option(title, name:str | None=None,  command:str | None=None, **kwargs):
    return QuickReply(
        title=title,
        payload=Payload(
            create_command(title if not command else command),
            **kwargs
        ),
        name=title if not name else name,
        ref=f"{randint(0, 1000000)}"
    )