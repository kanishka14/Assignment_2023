# program to find the biggest repeating sub-string in a string and the starting position of both sub-strings.

def main(in_string):
    n = len(in_string)
    t = -1
    ls = {}
    pos = []
    for i in range(n):
        for j in range(i, n):
            x = in_string[i:j + 1]
            if in_string.count(x) > 1:
                ls[(len(x))] = x

    # Gets the largest substring from the dictionary
    my_keys = list(ls.keys())
    my_keys.sort()
    sort_res = {i: ls[i] for i in my_keys}
    res = list(sort_res.values())[-1]

    # finds the staring positions of the repeating string
    while True:
        try:
            t = in_string.index(res, t + 1)
            pos.append(t + 1)
        except ValueError:
            break
    return f"Biggest Repeating string : {res}, Start Positions : {pos}"


if __name__ == '__main__':
    s = input("Enter the string:\n")
    print(main(s))
