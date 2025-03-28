def swap_case(s: str) -> str:
    return s.swapcase()
    res = []
    for c in s:
        if c.islower():
            res.append(c.upper())
        elif c.isupper():
            res.append(c.lower())
        else:
            res.append(c)
    return "".join(res)
