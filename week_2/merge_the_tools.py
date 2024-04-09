def merge_the_tools(s, k):
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    
    for substring in substrings:
        seen = {}
        merged_substring = ''
        for char in substring:
            if char not in seen:
                seen[char] = True
                merged_substring += char
        print(merged_substring)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    