from itertools import permutations

def solve():
    letters = 'SENDMORY'
    digits = '0123456789'

    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue

        SEND = int(mapping['S'] + mapping['E'] + mapping['N'] + mapping['D'])
        MORE = int(mapping['M'] + mapping['O'] + mapping['R'] + mapping['E'])
        MONEY = int(mapping['M'] + mapping['O'] + mapping['N'] + mapping['E'] + mapping['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found:")
            print(mapping)
            print(f"SEND = {SEND}")
            print(f"MORE = {MORE}")
            print(f"MONEY = {MONEY}")
            return

solve()
