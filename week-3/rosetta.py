def encode(input_string):
    if not input_string:
        return []

    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q


def main():
    string = 'hello world'
    encoded_string = encode(string)
    print(encoded_string)

    decoded_string = decode(encoded_string)
    print(decoded_string)


if __name__ == '__main__':
    main()