def parse_lines(text):
    lines = []
    for line in text.splitlines():
        if line.strip():
            lines.append(line.strip())
    return lines