"""
Simple short-term memory wrapper.
"""

class ShortTermMemory:
    def __init__(self, limit=50):
        self.limit = limit
        self.items = []

    def add(self, item: str):
        self.items.append(item)
        if len(self.items) > self.limit:
            self.items.pop(0)

    def get_all(self):
        return self.items
