class HistoryManager:

    def __init__(self):

        self.undo_stack = []
        self.redo_stack = []

    def push(self, image):

        self.undo_stack.append(
            image.copy()
        )

        self.redo_stack.clear()

    def undo(self, current):

        if not self.undo_stack:
            return current

        self.redo_stack.append(
            current.copy()
        )

        return self.undo_stack.pop()

    def redo(self, current):

        if not self.redo_stack:
            return current

        self.undo_stack.append(
            current.copy()
        )

        return self.redo_stack.pop()

    def clear(self):

        self.undo_stack.clear()

        self.redo_stack.clear()