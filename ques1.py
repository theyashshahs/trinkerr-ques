def digitsum(num: int):
    sq_sum = 0

    if num < 9:
        return -1

    i = 0
    while num > 0 and num > 9:
        sq_sum = 0
        i += 1
        while num > 0:
            sq_sum = sq_sum + (num % 10) ** 2
            num = num // 10

            if sq_sum == 1:
                break

        num = sq_sum

    return i


if __name__ == "__main__":
    num = int(input())
    print(digitsum(num))
