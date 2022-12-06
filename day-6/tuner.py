def find_marker(string, num_of_unique_chars):
    marker = -1
    for i in range(len(string)):
        group = string[i:i+num_of_unique_chars]
        if len(set(group)) == num_of_unique_chars:
            marker = i+num_of_unique_chars
            break
    return marker


with open("input.txt", 'r') as file:
    content = file.read().strip()

    print("Start of packet:", find_marker(content, 4))
    print("Start of message:", find_marker(content, 14))
    
