def validate_username(username):
    if username is None:
        raise ValueError("Username cannot be None")
    if not isinstance(username, str):
        raise TypeError("Username must be a string")
    if len(username) < 3 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    return True
