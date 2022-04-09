def check(str1, str2):
    if sorted(str1) == sorted(str2):
        return True

    return False


if __name__ == "__main__":
    strings: list = input().split()

    res = []

    for str1 in strings:
        for str2 in strings:
            if str1 == str2:
                continue

            if check(str1, str2):
                res.append([str1, str2])
                continue

    print(res)
