from collections import deque


class ChatMemory:
    def __init__(self, max_size=10):
        self.history = deque(maxlen=max_size)

    def add_message(self, message):
        self.history.append(message)

    def get_history(self):
        return list(self.history)


chat_memory = ChatMemory()