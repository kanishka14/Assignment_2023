# program to find the biggest repeating substring in a string and the starting position of both sub-strings.
from itertools import combinations


def main(in_string):
    t = -1
    pos = []

    # finding all possible substrings
    sub_list = [in_string[x:y] for x, y in combinations(range(len(in_string) + 1), r=2)]
    # finding repeating substrings
    repeat_list = list(set(filter(lambda x: sub_list.count(x) > 1, sub_list)))
    res = max(repeat_list, key=len)

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
