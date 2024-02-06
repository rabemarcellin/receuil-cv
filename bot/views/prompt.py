from datetime import datetime
from instance import chat, query
from controllers.helper import action as set_action
        
def prompt(sender_id, text, action):
    chat.send_text(sender_id, text)
    query.set_action(sender_id, set_action(action))

def prompt_date(sender_id, text, action, retrying=False):
    now = datetime.now()
    tips = f"""Entrer sous format: JJ/MM/AAAA\n\nPar exemple: {now.strftime('%d/%m/%Y')}"""

    if retrying:
        tips = f"""Veuillez le faire sous format JJ/MM/AAAA\n\nPar exemple: {now.strftime('%d/%m/%Y')}"""
        chat.send_text(sender_id, tips)
        chat.send_text(sender_id, "Recommencer: ")
    else: 
        chat.send_text(sender_id, text)
        chat.send_text(sender_id, tips)
    query.set_action(sender_id, set_action(action))

def prompt_academic_levels(sender_id, action):
    query.set_action(sender_id, action=set_action(action))