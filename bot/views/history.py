from instance import query

def set_action_history(sender_id, action):
    query.set_temp(sender_id, "last_action", action)
