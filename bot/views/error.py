from instance import chat
from .quick_reply.send_options import send_options


def send_error(sender_id, error_text):
    chat.send_text(sender_id, error_text)    
    chat.send_text(sender_id, "Récommencer: ")
    # todo: do some options
        