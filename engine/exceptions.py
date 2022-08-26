class ActionError(Exception):
    def __init__(self, action: str):
        super().__init__(f"Invalid action: {action}")


class DB_Error(Exception):
    def __init__(self):
        super().__init__(f"Error with db")