def check_palindrome(word):
    length = len(word)
    all_match = True
    for index in range(length):
        if word[index] == word [-index-1]:
                return True
        else:
                all_match = False
                return False 
print(check_palindrome("palindromemordnilap"))

