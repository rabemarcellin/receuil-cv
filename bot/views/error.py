from instance import chat, query
from controllers.helper import action as set_action


def send_error_input(sender_id, error_text, action):
    chat.send_text(sender_id, error_text)    
    chat.send_text(sender_id, "Récommencer: ")
    # next: return to the action that trigger input error
    query.set_action(sender_id, set_action(action))
        