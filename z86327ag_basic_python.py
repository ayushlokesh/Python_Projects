"""
This is a stub for COMP16321 coursework 1.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.
"""

# ---Section 1 --- #

#(Question:a)
def read_file():#(s)
    """
        Read in the text file and save the paragraph to a single string

        :return: A text file paragraph as a string
    """

    #Your code here
    f=open("text.txt",'r')
    file_string=f.read()
    return(file_string)#(s)

# ---Section 2 --- #

#(Question:a)
def length_of_file():#(s)
    """
        Reports the length of the paragraph including numbers and whitespace
    
        :input_text: The text file paragraph as a string
        :return: An integer length of the file
    """
    input_text = read_file()#(s)

    #Your code here
    int_length_of_file=len(input_text)
    return(int_length_of_file)#(s)

#(Question:b)
def if_apple():#(s)
    """
        Reports a boolean True/False if the paragraph contains the entire word "apple"

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    bool_if_apple=False
    for a in input_text.split():
        if a.lower()=="apple":
            bool_if_apple=True
            break
    return (bool_if_apple)#(s)

#(Question:c)
def if_upper_case_exists():#(s)
    """
        Reports a boolean True/False if the paragraph contains any number of upper case letters

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    lists=list(input_text)
    bool_if_upper_case_exist=False
    for x in lists:
        if ord(x)>=65 and ord(x)<91:
            bool_if_upper_case_exist=True
            break
    return (bool_if_upper_case_exist)#(s)

#(Question:d)
def if_numbers_exist():#(s)
    """
        Reports a boolean True/False if the paragraph contains any number of integers

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    lists=list(input_text)
    bool_if_numbers_exist=False
    for x in lists:
        if ord(x)>=48 and ord(x)<58:
            bool_if_numbers_exist=True
            break
    return (bool_if_numbers_exist)#(s)

#(Question:e)
def if_spaces_exist():#(s)
    """
        Reports a boolean True/False if the paragraph contains any number of blank spaces

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    lists=list(input_text)
    bool_if_spaces_exist=False
    for x in lists:
        if x==' ':
            bool_if_spaces_exist=True
            break
    return (bool_if_spaces_exist)#(s)

#(Question:f)
def if_first_letter_t():#(s)
    """
        Reports a boolean True/False if the first letter of the paragraph is a t

        :input_text: The text file paragraph as a string
        :return: A boolean True/false
    """
    input_text = read_file()#(s)

    #Your code here
    x=input_text.strip()
    bool_if_first_letter_t= 't'in x[0].lower()
    return (bool_if_first_letter_t)#(s)

#(Question:g)
def fourth_letter_seventh_word():#(s)
    """
        Reports the fourth letter in the seventh word of the paragraph as a string

        :input_text: The text file paragraph as a string
        :return: A string letter
    """
    input_text = read_file()#(s)

    #Your code here
    lists=input_text.split()
    if len(lists)>=7 and len(lists[6])>=4:
        string_fourth_letter_seventh_word=lists[6][3]
    else:
        string_fourth_letter_seventh_word=''
    return (string_fourth_letter_seventh_word)#(s)

# ---Section 3 --- #

#(Question:a)
def convert_to_lower_case():#(s)
    """
        Converts the paragraph to entirely lowercase with no other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    string_lower_case_paragraph=input_text.lower()
    return (string_lower_case_paragraph)#(s)

#(Question:b)
def reverse_paragraph():#(s)
    """
        Reverses the paragraph such that it can be read backwards with no other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    lists=list(input_text)
    lists.reverse()
    string_reversed_paragraph=""
    for x in lists:
        string_reversed_paragraph += x
    return (string_reversed_paragraph)#(s)

#(Question:c)
def duplicate_and_concatenate_paragraph():#(s)
    """
        Duplicate the paragraph and combine them such that they can be read twice in order with
        no other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    input_text+=input_text
    string_duplicated_paragraph=input_text
    return (string_duplicated_paragraph)#(s)

#(Question:d)
def remove_whitespace_from_paragraph():#(s)
    """
        Remove any whitespace from the paragraph except spaces between words and numbers with no
        other changes

        :input_text: The text file paragraph as a string
        :return: A string paragraph
    """
    input_text = read_file()#(s)

    #Your code here
    string_clean_paragraph=input_text.strip()
    return (string_clean_paragraph)#(s)

if __name__ == '__main__':#(s)
    #You can place any ad-hoc testing here
    #i.e test = remove_whitespace_from_paragraph()
    #i.e print(test)
    pass 