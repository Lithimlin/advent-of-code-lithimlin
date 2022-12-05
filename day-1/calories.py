with open("input.txt", 'r') as file:
    content = file.read().strip()
    lists = content.split("\n\n")
    lists = [[int(num) for num in l.split("\n")] for l in lists]

    sums = [sum(l) for l in lists]
    print("Maximum calories:", max(sums))
    print("Sum of top three:", sum(sorted(sums)[-3::]))
