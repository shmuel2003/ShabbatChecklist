class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {"task": self.description, "done": self.done}

    @staticmethod
    def from_dict(data):
        return Task(data["task"], data["done"])
