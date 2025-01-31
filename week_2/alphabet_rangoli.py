def rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    # Create the top part of the rangolis
    rows = []
    for i in range(size):
        row = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        rows.append(row.center(4*size - 3, '-'))
    
    # Create the bottom part of the rangoli by reversing the top part
    result = rows[::-1] + rows[1:]
    
    # Joining the rows with newline character
    return '\n'.join(result)
def print_rangoli(size):
    print(rangoli(size))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)