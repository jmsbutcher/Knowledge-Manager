# 9/28/22


def print_banner_line(message, length=50):
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
    result += ""
    print(result)


class PrefixNotFoundException(Exception):
    """ Raise when prefix not found in string """
    def __init__(self, prefix, target_string):
        self.message = "{} not found in {}.".format(prefix, target_string)
        super().__init__(self.message)


def extract_trailing_int(target_string, prefix=""):
    """ 
    Return the last full integer after the [prefix] in the string [s].
    Return None if last character isn't an integer. 
    
    Example:
        s = "New Document34"
        prefix = "New Document"
        Returns: 34
    """
    if prefix in target_string:

        int_suffix_str = ""
        index = len(target_string)
        while index > 0:
            index -= 1
            c = target_string[index]
            if c.isdigit():
                int_suffix_str = c + int_suffix_str
            else:
                break
        if len(int_suffix_str) > 0:
            return int(int_suffix_str)
        else:
            return None
    else:
        raise PrefixNotFoundException(prefix, target_string)


if __name__ == "__main__":
    print(extract_trailing_int("New Document 123", ""))
