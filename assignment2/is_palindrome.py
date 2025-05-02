def is_palindrome(sentence):
    # Compare characters from both ends
    left, right = 0, len(sentence)-1
    while left <= right:
        if sentence[left] != sentence[right]:
            return False
        left += 1
        right -= 1
    return True