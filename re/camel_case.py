import re


def to_camel_case(text):
    result = re.split(r'[_|-]', text)
    print(result)
    return result[0] + ''.join(map(lambda word: word.title(), result[1:]))

if __name__ == '__main__':
    print(to_camel_case('_my_func_mother _The_rigdsa_fads'))
