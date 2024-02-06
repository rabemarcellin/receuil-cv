import views.introduce as introduceview
from .quick_reply.send_options import send_options
from instance import query

def get_started(sender_id):
    next_options = ["whoiam", "start"]
    send_options(sender_id, options=next_options)

def self_presentation(sender_id):
    next_options = ["ready", "stop"]
    introduceview.introduce(sender_id)
    send_options(sender_id, options=next_options)


