if __name__ == '__main__':
    N = int(input())
    result = list()
    commands = list()
    while N > 0:
        commands.append(input())
        N -= 1
    for command in commands:
        if "append" in command:
            elems = command.split()
            result.append(int(elems[1]))
        elif "remove" in command:
            elems = command.split()
            for val in result:
                if val == int(elems[1]):
                    result.remove(val)
                    break
        elif "sort" in command:
            result.sort()
        elif "reverse" in command:
            result.reverse()
        elif "print" in command:
            print(result)
        elif "insert" in command:
            elems = command.split()
            i = int(elems[1])
            e = int(elems[2])
            result.insert(i, e)
        elif "pop" in command:
            result.pop()
        else:
            print("Error")
            