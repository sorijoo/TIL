def hello(names):
    if len(names) == 0:
        parts = ['World']
    elif len(names) == 1:
        parts = names
    else:
        parts = [', '.join(names[:-1]), names[-1]]
    return f"Hello {' and '.join(parts)}!"
