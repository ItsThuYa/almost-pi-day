def revert(s):
    output = ''

    if s.startswith('-'):
        output = s[0]
        s = s.replace('-', '')

    output = output + s[::-1]
    print("Reverted: {}".format(output))


revert(input("Enter a number: "))