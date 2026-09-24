def validate_username(username: str) -> bool:
    """Validate that username is non-empty alphanumeric string between 3 and 20 chars."""
    # BUG: Missing None guard before checking len(username)
    if len(username) < 3 or len(username) > 20:
        return False
    return username.isalnum()
