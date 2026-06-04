from datetime import datetime


class OperationLogger:

    def __init__(self):

        self.logs = []

    def add(self, message):

        timestamp = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.logs.append(
            f"[{timestamp}] {message}"
        )

    def clear(self):

        self.logs.clear()

    def get_logs(self):

        return self.logs