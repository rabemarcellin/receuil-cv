from instance import chat
import views.introduce as introduceview
from .quick_reply.send_options import send_options


def get_started(sender_id):
    next_options = ["start", "exit"]
    introduceview.introduce(sender_id)
    send_options(sender_id, options=next_options)
