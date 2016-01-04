def try_get_input(input, name, default):
    try:
        return input[name]
    except AttributeError:
        return default
