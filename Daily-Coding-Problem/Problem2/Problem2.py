def encode(text):  # encode function
    encoded: str = ""
    if not text:  # Start with recursion
        return ""
    if len(text) == 1:
        return text + "1"
    counter = 1
    i = 1
    while i < len(text):  # Iterate over the input string and keep a current count
        if text[i] == text[i - 1]:
            counter = counter + 1
        else:
            encoded = encoded + str(counter) + text[i - 1]  # The encounter of a different string is appended to the
            counter = 1                                     # counter and the result string (encoded)
        i = i + 1
    encoded = encoded + str(counter) + text[i - 1]
    return encoded


def decode(text):  # Decode function
    if not text:  # Recursion
        return ""
    else:
        count = text[0]
        character = text[1]
        return character * int(count) + decode(text[2:])


if __name__ == "__main__":  # Driver function
    print("The encode version of AAAABBBCCDAA is:")
    print(encode("AAAABBBCCDAA"))
    print("The decode version of 1a2b3c is:")
    print(decode("1a2b3c"))
