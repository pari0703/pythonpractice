def swap_case(s):
    sp=""
    for char in s:
        if char.islower():
            sp+=char.upper()
        elif char.isupper():
            sp+=char.lower()
        else:
            sp+=char
        
    return sp


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)