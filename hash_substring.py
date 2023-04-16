# python3
# Daniels Raivo Ivanovs 211RMB021

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().strip().upper()
   


    if input_type == "I":
        pattern = input().strip()
        text = input().strip()
        return(input_type, pattern, text)

    elif input_type == "F":
        file_name = input().strip()
        with open(file_name) as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
            return(input_type, pattern, text)
        
    else:
        print("Invalid character, please try again")
        exit()
    
def print_occurrences(output):
    print(' '.join(map(str, output)))

        

def get_occurrences(input_type, pattern, text):
   # this function should find the occurances using Rabin Karp alghoritm 
    t = len(text)
    p = len(pattern)
    occurrences = []
    
    if input_type == "I":    
        for i in range(t - p + 1):
            if text[i: i + p] == pattern:
                occurrences.append(i)
    
    elif input_type == "F":    
        pattern_hash = sum(ord(pattern[i]) * pow(10, p - i - 1) for i in range(p))
        text_hash = sum(ord(text[i]) * pow(10, p - i - 1) for i in range(p))
        
        for i in range(t - p + 1):
            if text_hash == pattern_hash:
                if text[i:i + p] == pattern:
                    occurrences.append(i)
            
            
            if i < t -p:
                text_hash = (text_hash - ord(text[i]) * pow(10, p - 1)) * 10 + ord(text[i +p])
                
    return occurrences             
                
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
