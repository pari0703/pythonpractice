def mutate_string(string, position, character):
    s=list(string)
    s[position]=character
    s_new = ''.join(s)
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)