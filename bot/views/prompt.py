from datetime import datetime
from instance import chat, query
from controllers.helper import action as set_action

def prompt(sender_id, text, action):
    chat.send_text(sender_id, text)
    query.set_action(sender_id, set_action(action))

def prompt_date(sender_id, text, action):
    now = datetime.now()
    
    for message in [
        text,
        "Entrer sous format: JJ/MM/AAAA",
        f"Par exemple: {now.strftime('%d/%m/%Y')}"
    ]:
        chat.send_text(sender_id, message)
    query.set_action(sender_id, set_action(action))

def prompt_academic_levels(sender_id, action):
    query.set_action(sender_id, action=set_action(action))