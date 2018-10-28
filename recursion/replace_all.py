def replace_all(text, c, t):
    if text == '':
        return text
    if len(text) == 1:
        if text == c:
            return t
        else:
            return text
    else:
        if text[0] == c:
            return t + replace_all(text[1:],c,t)
        else:
            return text[0] + replace_all(text[1:],c,t)
