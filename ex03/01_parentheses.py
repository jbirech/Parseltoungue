import sys

def cap(text):
    i = True
    string = ""
    for char in text:
        if i:
            string += char.upper()
        else:
            string += char.lower()

        if (char.isalpha()):
            i = not i
    return string

def replace_vowel(test):
    i = 0
    for letters in test:
        if letters in ['a', 'e', 'o', 'u', 'A', 'E', 'O', 'U']:
            test = test.replace(letters, '*')
    print(test)

def paranthesis(s):
    i = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
            elif c == '(':
                j += 1
    return j == 0

def main(args):
    print(cap(args[1]))
    a = cap(args[1])
    replace_vowel(a)
    results = paranthesis(args[1])
    if results == False:
        print("Balanced? False")
    else:
        print("Balanced? True")

if __name__ == "__main__":
    main(sys.argv)