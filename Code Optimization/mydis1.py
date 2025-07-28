import dis


def list_comp(n):
    return [x**2 for x in range(n)]


def for_loop(n):
    result = []
    for x in range(n):
        result.append(x**2)
    return result


bob = dis.dis(list_comp)
print(f'Disassembly of list_comp: {bob}')
joe = dis.dis(for_loop)
print(f'Disassembly of for_loop: {joe}')
