import oop


def main():  # Main function
    """
    Main function initializes data from file, creates PathFinder object, and uses the class to find the longest path for

    the object created

    :return: Displays the desired information
    """

    pathfinder_list, bool_pf_list, n_rows, cols = read_data_from_file('sam_1.txt')  # Reads data from file and returns
    # the appropriate variables
    passage_seeker = oop.PathFinder(pathfinder_list, bool_pf_list, n_rows, cols)  # Sends data to class
    # to be initialized
    passage_seeker.find_longest_path_length()  # Finds the longest path
    pf_str = 'Map dimensions:\nNumber of columns: {:d}\nNumber of rows: {:d}\n\nLength of the longest "A" path: {:d}'
    print(pf_str.format(cols, n_rows, passage_seeker.get_max_path()))  # prints the display


# Use open(), readline() and/or readlines() functions to read the following from
# the input file:
# - length and width of the map;
# - the characters to be stored in the map.
# Create the map using the data read from the input file.
# Note: you may need to use strip and split functions.
# The next part is OPTIONAL but might be helpful to use.
# Declare and initialize a Boolean list with similar dimensions to the map; this
# list can be used to keep track of the A's in the input file that have already
# been counted in the path of A's being 'discovered' in the program.
# Parameter to function: input file name.
def read_data_from_file(filename):
    """
    Reads the input file determines the length and width of the map and the characters to be stored in the map.

    Declare and initialize a Boolean list with similar dimensions to the map this list can be used to keep track of the

    A's in the input file that have already

    been counted in the path of A's being 'discovered' in the program.

    :param filename: The provided file

    :return: pathfinder_list, bool_pf_list, n_rows, m_cols
    """
    pathfinder_list = []  # Creates an empty list
    bool_pf_list = []

    with open(filename, 'r') as input_file:  # Opens file and starts reading from it
        first_row = input_file.readline()  # Read the line in the file
        m_cols, n_rows = first_row.split(' ')  # Assigns the number of columns and rows given by the file
        m_cols = int(m_cols)
        n_rows = int(n_rows)
        for n in range(n_rows):  # iterates through the file for each row
            row_val = input_file.readline()  # Reads a single line
            row_val = row_val.rstrip('\n')
            col_list = list(row_val)  # Turns string into a list
            pathfinder_list.append(col_list)  # Appends col_list making a 2d list
            bool_pf_list.append([False] * m_cols)  # Creates a 2d list of exacts size with all false values

    return pathfinder_list, bool_pf_list, n_rows, m_cols


main()
