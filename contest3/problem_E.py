s = input()

def check(s):
    s = s.strip()
    chars = set('0123456789+-*() ')
    if s[0] in "+-*" or s[-1] in "+-*" or "**" in s or not set(s).issubset(chars):
        return "WRONG"
    try:
        return eval(s)
    except:
        return "WRONG"

print(check(s))
