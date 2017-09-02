"""
Welcome to Challege One!
Please follow the instructions in the docstrings of each Task method.
"""

stringToBeReversed = 'you_need_to_reverse_this_string'
unorderedList = ['Hello', 'World', 'Cisco', 'Jam' , 'Spark', 'Bot', 'Challenge',
                 'Put', 'This', 'List', 'In', 'Alphabetical', 'Order']
possible_palindromes = ["M3o2m", "N4au5ruan9", "12Hag3ig5ah", "Ai5bohp8hobia", "Ta89cocat", "7Racecar09", "Suc90cus",
               "Pip8pip", "Civ34ic9", "Ma8ma", "Kay8ak", "0I2g3ig54i", "Deta8rtrated"]

def main():
    reversedString = taskOne_reverse_string(stringToBeReversed)
    print("Task 1: Printing Reversed String: " + reversedString)

    sortedList = taskTwo_sort_list(unorderedList)
    print("Task 2: Printing Sorted List: " + str(sortedList))

    sortedFilteredPalindromes = taskThree_filter_palindromes(possible_palindromes)
    print("Task 3: Printing Filtered Palindromes: " + str(sortedFilteredPalindromes))

def taskOne_reverse_string(stringToBeReversed):
    """
    Write a method that will reverse a string passed in as a parameter,
    and return it.
    You must use a for or while loop.
    No points for reversedString[::-1]
    And no Googling the answer.
    """
    
    reversedString = ""

    for i in range(-1, -len(stringToBeReversed) - 1, -1):
        reversedString += stringToBeReversed[i]

    return reversedString

def taskTwo_sort_list(unorderedList):
    """
    Write a method that will sort a list of words into alphabetical order,
    and returns the list.
    Hint: Use your sorting algorithm knowledge.
    No points for using .sorted()
    No googling the answer.
    HINT: Compare one string to another and store one in a temp var
    """
    
    # Insertion sort

    for i in range(1, len(unorderedList)):
        j = i
        while j > 0 and unorderedList[j - 1] > unorderedList[j]:
            temp = unorderedList[j]
            unorderedList[j] = unorderedList[j - 1]
            unorderedList[j - 1] = temp
            j -= 1
    return unorderedList

def taskThree_filter_palindromes(possible_palindromes):
    """
    Write a method that removes the numbers from the strings
    in the method parameter list. Filter which of the strings
    are palindromes.
    No googling the answer.
    HINT: Use your solution from taskOne_reverse_string to check for Palindromes
    HINT: Use your solution from taskTwo_sort_list to sort the list.
    """

    # This next line should remove the numbers.
    possible_palindromes = list(map(lambda x: filter_numbers(x), possible_palindromes))

    # Converting to string using ''.join() - see https://stackoverflow.com/a/5618893
    palindromes = \
        list(
    	    map(
    	        lambda x: ''.join(x), # Convert from a list of lists to a list of strings.
    	        list(filter(lambda x: is_palindrome(''.join(x).lower()), possible_palindromes))
    	    )
        )
    return palindromes

def filter_numbers(string_to_filter):
	return list(filter(lambda x: x.isnumeric() == False, list(string_to_filter)))

def is_palindrome(string_to_check):
	return string_to_check == taskOne_reverse_string(string_to_check)

if __name__ == '__main__':
    main()
