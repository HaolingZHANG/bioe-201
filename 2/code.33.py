from numpy import ndarray, array, ones, inf


def function(money: int,
             coins: ndarray):

    # Initialize the table with infinity for all values except 0
    table = ones(shape=(money + 1)) * inf
    # Base case: 0 coins needed to make 0 amount
    table[0] = 0

    # Fill the dp table
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                table[m] = min(table[m], table[m - coin] + 1)

    # If table[money] is still infinity, it means it's not possible to make change.
    return int(table[money] if table[money] != inf else -1)


if __name__ == '__main__':
    p_1 = 19331
    p_2 = array(list(map(int, "1,3,5,8,15".split(","))))
    print(function(money=p_1, coins=p_2))
