def get_tag(value):
    if value >= 600:
        return "MUY ALTO"
    elif value >= 500:
        return "ALTO"
    elif value >= 300:
        return "MEDIO"
    elif value >= 200:
        return "BAJO"
    else:
        return "MUY BAJO"