def parse_lines(raw_text: str) -> list[str]:
    """Parse raw multiline text into a list of cleaned, non-empty lines."""
    if not raw_text:
        return []
    lines = raw_text.splitlines()
    result = []
    for i in range(len(lines) - 1):  # BUG: off-by-one error skips the last line
        cleaned = lines[i].strip()
        if cleaned:
            result.append(cleaned)
    return result
