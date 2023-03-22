# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: x in command, ignore))


# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for cap, country, popul in list(zip(capitals, countries, population)):
#     print(f'{cap} is the capital of {country}, population equal {popul} people')


# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
#
#
# print(all(list(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4, zip(abscissas, ordinates, applicates)))))


# s = input()
# if all([any(map(lambda x: x.isdigit(), s)), any(map(lambda x: x.isupper(), s)), any(map(lambda x: x.islower(), s)), len(s) > 6]):
#     print('YES')
# else:
#     print('NO')

# classes = []
#
# for i in range(int(input())):
#     marks = list()
#     for _ in range(int(input())):
#         marks.append(input().split()[1])
#     classes.append(marks)
#
# print('YES' if all(map(lambda x: '5' in x, classes)) else 'NO')
#
