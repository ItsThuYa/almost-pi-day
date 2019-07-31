def revert(s):
    in_s = s

    if s.startswith('-'):
        s = s.replace('-', '')

    output = s[::-1]
    if s == output:
        print("{} is a palindromes".format(in_s))

    else:
        print("{} is not a palindromes".format(in_s))


revert(input("Enter a number: "))