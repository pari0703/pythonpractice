def split_and_join(line):
    words = line.split(" ")
    l='-'.join(words)
    return l
if __name__ == '__main__':
    line=input().strip()
    print(split_and_join(line)) 