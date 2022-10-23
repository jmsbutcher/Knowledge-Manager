# 9/28/22


def print_banner_line(message, length):
    if (len(message) > length):
        print(message)
        return
    result = ""
    low_index = int((length - len(message))/2)
    high_index = int((length + len(message))/2)
    j = 0
    for i in range(length):
        if i >= low_index and i < high_index:
            result += message[j]
            j += 1
        else:
            result += '-'
    print(result)
