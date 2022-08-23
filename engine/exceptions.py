class ActionError(Exception):
    def __init__(self, action: str):
        super().__init__(f"Invalid action: {action}")