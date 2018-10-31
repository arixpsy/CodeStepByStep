def repeat_string(string, num):
    if num < 0:
        raise ValueError()
    if num == 0:
        return ''
    if num == 1:
        return string
    else:
        return repeat_string(string, num-1) + string
