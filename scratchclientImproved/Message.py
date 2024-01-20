class Message:
    def __init__(self, data):
        data["type"] = data.pop("type")
        data["created_timestamp"] = data.pop("datetime_created")
        data["actor"] = data.pop("actor_username")
        data["actor_id"] = data.pop("actor_id")
        self.__dict__.update(data)
