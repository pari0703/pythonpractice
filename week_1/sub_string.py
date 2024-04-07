def count_substring(string, sub_string):
    l1 = len(string)
    l2 = len(sub_string)
    count=0
    for i in range(0, l1):
        k = string[i:i+l2]
        if k == sub_string:
           count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)