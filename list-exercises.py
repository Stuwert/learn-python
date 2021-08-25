# Write a function nested_sum() which takes a list of lists of integers and adds up the list

def nested_sum(list_of_integers):
    sum = 0
    for nested_list in list_of_integers:
        for num in nested_list:
            sum += num
    return sum


print(nested_sum([[1, 2], [3], [4, 5, 6]]))

# Write a function call cumsum that takes a list off numbers and returns the cumulative sum
# i.e. a new list where the ith element is the sum of the first i+1 elements
# [1, 2, 3] -> [1, 3, 6]


def cumsum(integers):
    sum = 0
    cumsum_values = []
    for num in integers:
        sum += num
        cumsum_values.append(sum)
    return cumsum_values


print(cumsum([1, 2, 3]))

# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements


def middle(list_of_any):
    return list_of_any[1: -1]


print(middle([1, 2, 3, 4, 5]))


def chop(list_of_any):
    list_of_any.pop(0)
    list_of_any.pop()
    return None


test = [1, 2, 3]
print(test)
chop(test)
print(test)

# Returns true if list is sorted, returns false if not


def is_sorted(list_of_any):
    for idx in range(len(list_of_any)):
        if (idx > 0 and list_of_any[idx] < list_of_any[idx - 1]):
            return False
    return True


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
print(is_sorted(['a', 'b']))

# Two words are anagrams if you can rearrange the letters from one to spell the other


def is_anagram(str_one, str_two):
    list_one = [char for char in str_one]
    list_two = [char for char in str_two]
    list_one.sort()
    list_two.sort()
    return "".join(list_one) == "".join(list_two)


print(is_anagram("test", "stet"))
