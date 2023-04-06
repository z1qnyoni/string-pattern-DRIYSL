# python3
# Daniels Raivo Ivanovs 211RMB021

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()
    
    if input_type == 'I':
        text = input().rstrip()
        pattern = input().rstrip()
    elif input_type == 'F':
        file = input().rstrip()
        with open(file, 'r') as f:
            text = f.readline().rstrip()
            pattern = f.readline().rstrip()
    else:
        print("Invalid input type, Try Again!!")
        return None
            
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    
    if len(output) > 0:
        print(' '.join(map(str, output)))
    else:
        print(-1)

        

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    t = len(text)
    p = len(pattern)
    p_hash = hash(pattern)
    t_hash = hash(text[:p])
    occurrences = []
    
    for i in range(t - p + 1):
        if p_hash == t_hash:
            if text[i:i+p] == pattern:
                occurrences.append(i)
        if i < t - p:
            t_hash = t_hash - ord(text[i]) + ord(text[i + p])

    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
