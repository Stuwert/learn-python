# A thoroughly useless wrapper

def count_string(str, substr):
    return str.count(substr)


print(count_string('banana', 'a'))


def is_palindrome(str_one, str_two):
    return str_one == str_two[::-1]


print(is_palindrome('aba', 'aba'))
print(is_palindrome('aba', 'aab'))


# ord converts character to ordinal
# chr converts ordinal to character
# need some way of storing if capital?
# What happens if the type is higher or lower than the translation?

print(ord('C'))
print(ord('Z'))
print(chr(63))

uppercase_lower_boundary = ord('A')
uppercase_upper_boundary = ord('Z')
lowercase_lower_boundary = ord('a')
lowercase_upper_boundary = ord('z')


def is_uppercase(letter_ord):
    return letter_ord < uppercase_upper_boundary and letter_ord > uppercase_lower_boundary


def is_lowercase(letter_ord):
    return letter_ord < lowercase_upper_boundary and letter_ord > lowercase_lower_boundary


def translate_letter_by(letter, translation_amount):

    # Check if exsting char is upper or lower
    # Check if resulting char is above or below
    # convert into something correct

    letter_ord = ord(letter)
    new_letter_ord = letter_ord + translation_amount

    if is_uppercase(letter_ord):
        if new_letter_ord < uppercase_lower_boundary:
            diff = new_letter_ord - uppercase_lower_boundary
            return chr(uppercase_upper_boundary + diff)
        if new_letter_ord > uppercase_upper_boundary:
            diff = new_letter_ord - uppercase_upper_boundary
            return chr(uppercase_lower_boundary + diff)
        return chr(new_letter_ord)
    if is_lowercase(letter_ord):
        if new_letter_ord < lowercase_lower_boundary:
            diff = new_letter_ord - lowercase_lower_boundary
            return chr(lowercase_upper_boundary + diff)
        if new_letter_ord > lowercase_upper_boundary:
            diff = new_letter_ord - lowercase_upper_boundary
            return chr(lowercase_lower_boundary + diff)
        return chr(new_letter_ord)

    # If it doesn't fit A-Za-z return it as is
    return letter


def shift_word_by(word, translation_amount):
    new_word = ''
    for letter in word:
        new_word += translate_letter_by(letter, translation_amount)
    return new_word


print(shift_word_by('bingbong', 27))
print(shift_word_by('dkpidqpi', -2))
