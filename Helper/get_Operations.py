import types

def capitalize_Strings(input):
    if isinstance(input, types.StringType):
        output = input.upper()
    if isinstance(input, types.ListType):
        output = [s.upper() for s in input]
    return output