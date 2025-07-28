import dis


def dict_lookup(d, key):
    return d[key]


def dict_get(d, key):
    return d.get(key, None)


print(f'Disassemblinhg dict_loopup:')
dis.dis(dict_lookup)
print(f'Disassembling get:')
dis.dis(dict_get)
