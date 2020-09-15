
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    # Two pointer way:

    # left, right = 0, len(s) - 1
    # while left < right:
    #   s[left], s[right] = s[right], s[left]
    #   left += 1
    #   right -= 1

    # return s
    
    # Pythonic way....
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]
        
    return s


def main():
  print(reverseString(["h", "e", "l", "l", "o"]))
  print(reverseString(["k", "e", "v", "i", "n"]))


main()