from numpy import ndarray, array, zeros, max


def function(length: int,
             width: int,
             down_matrix: ndarray,
             right_matrix: ndarray) \
        -> int:
    # Initialize the grid for dynamic programming.
    matrix = zeros(shape=(length + 1, width + 1), dtype=int)

    # Initialize the first column using Down matrix.
    for location in range(1, length + 1):
        matrix[location][0] = matrix[location - 1][0] + down_matrix[location - 1][0]

    # Initialize the first row using Right matrix.
    for location in range(1, width + 1):
        matrix[0][location] = matrix[0][location - 1] + right_matrix[0][location - 1]

    # Fill the rest cells of the grid using dynamic programming.
    for i in range(1, length + 1):
        for j in range(1, width + 1):
            matrix[i][j] = max([matrix[i - 1][j] + down_matrix[i - 1][j], matrix[i][j - 1] + right_matrix[i][j - 1]])

    return matrix[length, width]


if __name__ == '__main__':
    p_1 = 15
    p_2 = 13
    p_3 = array([
        list(map(int, "0 1 4 3 4 1 4 1 3 0 0 4 3 3".split(" "))),
        list(map(int, "0 0 0 4 0 4 3 2 0 2 2 3 2 3".split(" "))),
        list(map(int, "4 0 3 1 0 4 1 1 0 3 2 0 2 2".split(" "))),
        list(map(int, "1 3 0 3 1 4 1 0 2 3 0 2 4 1".split(" "))),
        list(map(int, "2 1 1 3 2 0 1 1 1 0 3 2 1 1".split(" "))),
        list(map(int, "2 3 1 0 1 1 1 2 2 3 2 1 0 4".split(" "))),
        list(map(int, "2 3 2 4 1 1 4 1 2 0 3 1 3 1".split(" "))),
        list(map(int, "4 3 2 3 0 1 0 2 3 3 2 4 4 4".split(" "))),
        list(map(int, "3 0 1 0 0 3 3 2 4 3 4 0 3 1".split(" "))),
        list(map(int, "4 0 2 3 3 2 4 2 1 4 1 3 2 3".split(" "))),
        list(map(int, "4 2 4 2 3 3 2 0 4 3 3 1 2 2".split(" "))),
        list(map(int, "1 3 2 3 1 4 4 0 2 4 0 4 2 2".split(" "))),
        list(map(int, "0 2 3 4 4 1 0 1 0 4 4 2 2 0".split(" "))),
        list(map(int, "3 0 4 2 1 3 4 1 1 0 1 2 3 1".split(" "))),
        list(map(int, "1 2 4 1 1 4 0 3 0 3 1 3 3 2".split(" ")))
    ])

    p_4 = array([
        list(map(int, "1 1 0 2 3 3 2 4 1 0 2 4 3".split(" "))),
        list(map(int, "4 2 3 0 4 3 3 1 0 2 1 0 0".split(" "))),
        list(map(int, "1 4 4 3 0 3 1 3 1 1 2 3 3".split(" "))),
        list(map(int, "4 1 3 1 0 4 3 4 4 0 1 0 0".split(" "))),
        list(map(int, "3 2 3 1 3 4 0 3 0 3 1 1 1".split(" "))),
        list(map(int, "3 0 2 0 1 1 1 2 2 2 1 3 1".split(" "))),
        list(map(int, "3 2 4 2 1 3 2 1 0 0 0 3 2".split(" "))),
        list(map(int, "2 0 2 4 0 2 3 2 1 0 3 1 1".split(" "))),
        list(map(int, "3 0 0 1 3 3 0 3 0 4 3 2 3".split(" "))),
        list(map(int, "2 0 2 4 3 0 2 2 3 0 0 0 3".split(" "))),
        list(map(int, "4 3 4 0 0 3 1 0 0 2 4 1 2".split(" "))),
        list(map(int, "4 3 1 3 2 0 4 3 3 0 3 3 0".split(" "))),
        list(map(int, "1 4 2 3 1 4 3 0 1 3 4 4 0".split(" "))),
        list(map(int, "1 4 4 4 2 4 4 0 0 0 4 0 1".split(" "))),
        list(map(int, "2 0 2 0 4 3 4 3 1 1 4 4 2".split(" "))),
        list(map(int, "2 4 2 0 1 3 3 1 1 2 1 0 2".split(" ")))
    ])
    print(function(p_1, p_2, p_3, p_4))
