# 1. Define a function named is_two. It should accept one input and return True
    # if the passed input is either the number or the string 2, False otherwise.
    
def is_two(x):
    '''
    takes in a number or a string and return True if:
    it is 2, or '2', or 'two', or 'Two', or 'TWO'
    '''
    if x == 2 or x == '2' or x == 'two' or x == 'Two' or x == 'TWO':
        return True
    else:
        return False


# 2. Define a function named is_vowel. 
    #It should return True if the passed string is a vowel, False otherwise.
    
def is_vowel():
    '''
    takes in a letter and returns true if the letter is 'a' or 'e' or 'i' or 'o' or 'u'
    or their capitalized versions.
    '''
    letter = input("Type a letter here to check if it is a vowel: ")
    if letter.isdigit():
        print("That's a digit Gidgit. Please use a LETTER with this function")
        return False
    if letter.isalpha():
        print("That's a letter, alright. But is it a vowel?")
        if letter.lower() == 'a'\
        or letter.lower() == 'e'\
        or letter.lower() == 'i'\
        or letter.lower() == 'o'\
        or letter.lower() == 'u':
            print("Yessir 'tis. You're smart like a kindergartner!")
            return True
        else:
            print("A vowel it is not.")
            return False
    else:
        print("That's neither letter, nor number. What rock are you under?")
        return False


# 3. Define a function named is_consonant. 
    # It should return True if the passed string is a consonant, False otherwise. 
    # Use your is_vowel function to accomplish this.
    
def is_consonant():
    '''
    takes in a letter and returns true if the letter is not 'a' or 'e' or 'i' or 'o' or 'u'
    or their capitalized versions.
    '''
    letter = input("Type a letter here to check if it is a consonant: ")
    if letter.isdigit():
        print("That's a digit Gidgit. Please use a LETTER with this function")
        return False
    if letter.isalpha():
        print("That's a letter, alright. But is it a consonant?")
        if letter.lower() != 'a'\
        and letter.lower() != 'e'\
        and letter.lower() != 'i'\
        and letter.lower() != 'o'\
        and letter.lower() != 'u':
            print("Yessir 'tis. You're smart like a kindergartner!")
            return True
        else:
            print("Doh! A consonant that is not.")
            return False
    else:
        print("That's neither letter, nor number. What rock are you under?")
        return False


# 4. Define a function that accepts a string that is a word. 
    # The function should capitalize the first letter of the word 
    # if the word starts with a consonant.
    
def cap_first_consonant(string):
    '''
    takes in a string and capitalizes the first letter if that letter is a consonant
    '''
    if string[0].lower() != 'a'\
    and string[0].lower() != 'e'\
    and string[0].lower() != 'i'\
    and string[0].lower() != 'o'\
    and string[0].lower() != 'u':
        return string[0].upper() + string[1:]
    else:
        return string


# 5. Define a function named calculate_tip. 
    # It should accept a tip percentage (a number between 0 and 1) 
    # and the bill total, and return the amount to tip.
    
def calculate_tip(tip_percentage_as_decimal, bill_total_without_tip):
    '''
    input the tip percentage as a decimal (between 0 and 1)
    then a comma then the total bill before tip. The function
    will output the tip amount and total bill with tip included
    '''

    tip_amount = round((tip_percentage_as_decimal * bill_total_without_tip), 2)
    total_bill_with_tip = bill_total_without_tip + tip_amount
    print('Amount to tip, Total bill with tip: ')
    return tip_amount, total_bill_with_tip


# 6. Define a function named apply_discount. 
    # It should accept a original price, and a discount percentage, 
    # and return the price after the discount is applied.
    
def apply_discount(original_price, discount_percentage):
    '''
    input the original item price then a comma then the discount as a percentage.
    Function will return the discounted item price.'''
    
    print('Discounted Price: ')
    return round((original_price - original_price * (discount_percentage / 100)))

    
def handle_commas(number_with_commas):
    '''
    Input a number AS A STRING with commas and returns the number without commas
    '''
    return float(number_with_commas.replace(',', ''))


def get_letter_grade(percentage_grade):
    '''
    Input a percentage grade between 0 and 100 and function returns
    a letter grade "A" for 90-100, "B" for 80 up to but not including 90,
    "C" for 70 up to but not including 80, and "F" for less than 70.'''
    
    if percentage_grade >= 90:
        return "A"
    elif percentage_grade >= 80:
        return "B"
    elif percentage_grade >= 70:
        return "C"
    else:
        return "F"
    