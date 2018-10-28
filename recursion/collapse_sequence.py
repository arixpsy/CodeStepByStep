# def collapse_sequences(s, c):
#     if c + c not in s:
#         return s
#     else:
#         s = s.replace(c+c, c)
#         if c + c not in s:
#             return s
#         else:
#             return collapse_sequences(s, c)

def collapse_sequences(s,c):
    if len(s) < 2:
        return s
    else:
        if s[0] == c:
            if s[1] == c:
                return collapse_sequences(s[1:],c)
            else:
                return c + collapse_sequences(s[1:],c)
        else:
            return s[0] + collapse_sequences(s[1:],c)

print(collapse_sequences("aabaaccaaaaaada", 'a'))
print('expected result: abaccada')

print(collapse_sequences("mississssipppi", 's'))
print("expected result: misisipppi")

print(collapse_sequences("babbbbebbbxbbbbbb", 'b'))
print("expected result: babebxb")

print(collapse_sequences("palo alto", 'o'))
print("expected result: palo alto")

print(collapse_sequences("tennessee", 'x'))
print("expected result: tennessee")

print(collapse_sequences("", 'x'))
print('expected result: ')