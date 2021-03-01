

# This method determines which of the four values passed to it is the maximum.
# The four values passed represent the path lengths for the four paths of recursive calls from a specific character
# in the 2D list.
# Function parameters:
# a: The length returned from position [i-1, j].
# b: The length returned from position [i+1, j].
# c: The length returned from position [i, j-1].
# d: The length returned from position [i, j+1].
# Function return: Returns the Maximum of all lengths passed to it.
# '''
def find_max(a, b, c=0, d=0):
    """
    This method determines which of the four values passed to it is the maximum.

    The four values passed represent the path lengths for the four paths of recursive calls from a specific character

    in the 2D list.

    :param a: The length returned from position [i-1, j].

    :param b: The length returned from position [i+1, j].

    :param c: The length returned from position [i, j-1].

    :param d: The length returned from position [i, j+1].

    :return: Returns the Maximum of all lengths passed to it.
    """
    max_val = max(a, max(b, max(c, d)))
    return max_val


class PathFinder:
    def __init__(self, path_list, bool_list, rows, cols):  # Initializes data attributes needed for the class
        """
        Initializes data attributes needed for the PathFinder class

        :param path_list: A 2d list created from the given file used to determine the longest path using the A's

        available

        :param bool_list: A 2d list with the same dimensions as path_list, keeps track of which 'A' has already been

        visited

        :param rows: The total number of rows in each list

        :param cols: The total number of columns in each list
        """
        self.__path_list = path_list
        self.__bool_list = bool_list
        self.__rows = rows
        self.__cols = cols
        self.__max_path = 0

    # Resets the boolean list to all false values
    def reset_bool_list(self):
        """
        Resets the boolean list to all false values

        :return: A 2d list with all false values and the same dimensions as the path list
        """
        for n in range(self.__rows):
            for m in range(self.__cols):
                self.__bool_list[n][m] = False

    # Iterate through all the positions in the map (2-dimensional list);
    # at each position, call the recursive method findPathLengthRecursive(), and at
    # each position, update the maximum number of A's in the path so far.
    # Function return: The maximum number of A's in the path.
    # '''
    def find_longest_path_length(self):
        """
        Iterate through all the positions in the map (2-dimensional list);

        at each position, call the recursive method findPathLengthRecursive(), and at

        each position, update the maximum number of A's in the path so far.

        :return: The maximum number of A's in the path.
        """
        for n in range(self.__rows):
            for m in range(self.__cols):
                self.reset_bool_list()
                position_val = self.find_path_length_recursive(n, m)
                if self.__max_path < position_val:
                    self.__max_path = position_val

    # This method uses recursion to check the cells to the left, right, above and
    # below the current cell to determine if any of these is an 'A' that hasn't yet
    # been counted as part of the longest path of A's.
    # NOTE: Each 'A' in the path should be counted only once.
    # Function parameters:
    # n: The current row.
    # m: The current column.
    # Function return: Return either zero or the current length signifying the number of connected A's so far.
    # '''
    def find_path_length_recursive(self, n, m):
        """
        This method uses recursion to check the cells to the left, right, above and

        below the current cell to determine if any of these is an 'A' that hasn't yet

        been counted as part of the longest path of A's.

        NOTE: Each 'A' in the path should be counted only once.

        :param n: The current row.

        :param m: The current column.

        :return: Return either zero or the current length signifying the number of connected A's so far.
        """
        if (self.__path_list[n][m] == 'A') and (not self.__bool_list[n][m]):

            self.__bool_list[n][m] = True

            if n == 0 and m == 0:  # if element is the top left one
                path_length = 1 + find_max(self.find_path_length_recursive(n + 1, m),
                                           self.find_path_length_recursive(n, m + 1))
            elif (n == 0) and m == (self.__cols - 1):  # if element is the top right one
                path_length = 1 + find_max(self.find_path_length_recursive(n + 1, m),
                                           self.find_path_length_recursive(n, m - 1))
            elif n == (self.__rows - 1) and m == 0:  # if element is the bottom left one
                path_length = 1 + find_max(self.find_path_length_recursive(n - 1, m),
                                           self.find_path_length_recursive(n, m + 1))
            elif n == (self.__rows - 1) and m == (self.__cols - 1):  # if element is the bottom right one
                path_length = 1 + find_max(self.find_path_length_recursive(n - 1, m),
                                           self.find_path_length_recursive(n, m - 1))
            elif n == 0:  # if element is in the top row
                path_length = 1 + find_max(self.find_path_length_recursive(n, m - 1),
                                           self.find_path_length_recursive(n + 1, m),
                                           self.find_path_length_recursive(n, m + 1))
            elif m == 0:  # if element is in the first column
                path_length = 1 + find_max(self.find_path_length_recursive(n + 1, m),
                                           self.find_path_length_recursive(n - 1, m),
                                           self.find_path_length_recursive(n, m + 1))
            elif m == (self.__cols - 1):  # if element is in the last column
                path_length = 1 + find_max(self.find_path_length_recursive(n + 1, m),
                                           self.find_path_length_recursive(n - 1, m),
                                           self.find_path_length_recursive(n, m - 1))
            elif n == (self.__rows - 1):  # if element is in the bottom row
                path_length = 1 + find_max(self.find_path_length_recursive(n - 1, m),
                                           self.find_path_length_recursive(n, m - 1),
                                           self.find_path_length_recursive(n, m + 1))
            else:
                path_length = 1 + find_max(self.find_path_length_recursive(n + 1, m),
                                           self.find_path_length_recursive(n - 1, m),
                                           self.find_path_length_recursive(n, m - 1),
                                           self.find_path_length_recursive(n, m + 1))
            return path_length
        else:
            return 0

    # Returns max_path data attribute to caller
    def get_max_path(self):
        """
        Returns max_path data attribute to caller

        :return: max_path
        """
        return self.__max_path
