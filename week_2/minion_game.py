def minion_game(string):
    k1=0
    k2=0
    vowels = 'AEIOU'
    length=len(string)
    for i in range(length):
        if string[i] in vowels:
            k1+=length-i
        else:
            k2+=length-i
    if k1>k2:
       print("Kevin",k1)
    elif k1<k2:
       print("Stuart",k2)
    else:
        print("Draw")

if __name__ == '__main__':
    string = input()
    minion_game(string) 