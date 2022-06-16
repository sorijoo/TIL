def pascalize(s):
    if not s:
        return s
    return ''.join(_cap(x) for x in s.split('_'))


def _cap(s):
    return s[0].upper() + s[1:]
