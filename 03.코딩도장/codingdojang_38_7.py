class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(x):
    try:
        y=x[::-1]
        if x != y:
            raise Exception
        print(x)
    except Exception as e:
        print('회문이 아닙니다.',e)

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)