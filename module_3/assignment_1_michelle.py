"""
Assignment #1 (Module 3): Built-in types and functions

Begin by executing this script from the command line by typing
    `$ python assignment_1.py`


This script will print out all the questions and the returned value. This
script must execute without error.

Each question is a fill-in-the-blank and ends with a blank
`return` statement. Provide the answer to the question following
the return statement.

Sample question:

    def question():
        '''What is 2 + 2?'''
        return

    Answer:
        return 2 + 2

Note: the assignment is an evaluation of the usage of built-in types and
      functions. In the example above, return the equation 2 + 2, not the
      number 4.

Some questions have variables in them, and will need manipulation. In that
case, perform whatever transformations to the variable, and make sure that
it is returned.

Example:
    def question():
        '''Do something to variable x and return.'''
        x = 'a variable'
        ... code that does stuff to x ...
        return x
"""


def question_1():
    """Return a tuple containing a single item."""
    my_tuple = (1)
    return my_tuple


def question_2():
    """Return a list of strings."""
    list_of_strings = ['Strings', 'are', 'fun']
    return list_of_strings


def question_3():
    """Return a list of floats."""
    list_of_floats = [1.0,2.0,3.0]
    return list_of_floats


def question_4():
    """
    Return the following list in reverse order, using the sort
    built-in function.
    """
    numbers = [10, 20, 30, 40, 100]
    numbers.sort(reverse=True)

    return numbers



def question_5():
    """
    Using the append built-in function, add the number 200 to the
    following list, and return.
    """
    numbers = [197, 198, 199]
    numbers.append(200)
    return numbers


def question_6():
    """
    Using a built-in function, insert the value `banana` after `orange`
    and return.

    """
    fruits = ['orange', 'tomato']
    fruits.insert(1,'banana')
    return fruits




def question_7():
    """
    Using a built-in function, remove the value 2 from the following list
    and return.
    """
    numbers = [1, 2, 3, 4, 5]
    numbers.pop(1)
    return numbers


def question_8():
    """
    Using the slice function, return the last element from the following list.
    """
    words = ['fizz', 'buzz', 'foo', 'bar']
    bar = slice(3,4)

    return words[bar]


def question_9():
    """
    Using the slice function, return the value 'c' from the following list.
    """
    letters = ['a', 'b', 'c', 'd', 'e']
    c = slice(2,3)
    return letters[c]


def question_10():
    """
    Using the slice function, return the first two element in the list.
    """
    letters = ['a', 'b', 'c', 'd', 'e']
    x = slice(0,2)

    return letters[x]


def question_11():
    """Return the sum of 2 and 3 (use addition)."""
    return 2 + 3


def question_12():
    """Return the difference of 100 and 1 (use subtraction)."""
    return 100 - 1


def question_13():
    """Return the product of 7 and 5 (use multiplication)."""
    return 7 * 5


def question_14():
    """Return the quotient of 10 and 3 (use division)."""
    return 10 / 3


def question_15():
    """
    What is the data type of the value returned by: 4 / 2? Return the data
    type. Example if your answer is "string" or "list", then return the data
    type like this: `return str` or `return list`.
    """
    return float


def question_16():
    """What is the data type of number 9?"""
    return int


def question_17():
    """What is the data type of the number 3.0?"""
    return float


def question_18():
    """What is 4 to the power of 3?"""
    return 4 ** 2


def question_19():
    """Return the variable `value` as an integer."""
    value = 1 / 3

    return int(value)


def question_20():
    """Return the variable `value` as a float."""
    value = 2

    return float(value)


def question_21():
    """Return a string containing single quotes."""
    return "This is a string containing a 'single quote' string"


def question_22():
    """Return a string containing double quotes."""
    return "This is a string containing a \"double quote\" string"


def question_23():
    """Return a string that spans multiple lines."""
    return "\n Line 1 \n Line 2 \n Line 3"


def question_24():
    """
    Using a built-in function, return the following text
    as all uppercase.
    """
    text = 'The quick brown fox jumps over the lazy dog'
    return text.upper()


def question_25():
    """
    Using a built-in function, return the following text as
    title case (i.e. every word starts with a capital letter).
    """
    text = 'The quick brown fox jumps over the lazy dog'
    return text.title()


def question_26():
    """
    Return a string containing the backslash character.
    """
    return "This is a string containing a \\ character"


def question_27():
    """Return a string containing both single and double quotes."""
    return "This a string with both 'single' and \"double\" quotes"


def question_28():
    """
    Return a dictionary containing the three most populous
    Canadian provinces. Use their code as the key, and the
    full name as the value. Example "AB" - "Alberta"
    """
    the_dict = {"ON": "Ontario", "QC": "Quebec", "BC": "British" +
    " Columbia"}
    return the_dict


def question_29():
    """
    Return the value of the key "c" from the dictionary by
    using the key as the index.
    """
    my_dict = {'a': 3, 'b': 2, 'c': 7}
    return my_dict['c']


def question_30():
    """
    Extend and return the following dictionary by adding the following
    key/value pair: b, 10.
    """
    my_dict = {'a': 1}
    my_dict.update({'b':10})
    return my_dict


def question_31():
    """
    Return the unique values from the following list.
    """
    my_list = [1, 2, 2, 1, 3, 3, 2]

    return set(my_list)


if __name__ == '__main__':
    for num in range(1, 32):
        func = eval(f'question_{num}')  # pylint: disable=eval-used
        question = ' '.join(func.__doc__.split())
        print(f'Question {num}: {question}')
        print(f'    {func()}\n\n')
