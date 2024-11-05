

# 2. Write as little code as possible to pass the test
def is_item_in_list(item, a_list):
    # 3. Refactor
    return item in a_list
    # if item in a_list:
    #     return True
    # else:
    #     return False


# 2. Write as little code as possible to pass the test
def is_palindrome(string):
    if len(string) < 2:
        return False
    if not string.isalpha():
        return False
    return string == string[::-1]

    # 3. Refactor
    # for i in range(len(string)):
    #     if string[i] != string[-1-i]:
    #         return False
    # return True 