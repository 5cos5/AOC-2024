import re
def getSum(code):
    matches = re.finditer(r'mul\((?P<a>\d*)\,(?P<b>\d*)\)', code)
    return sum(int(match.group('a')) * int(match.group('b')) for match in matches)

with open('data.txt') as inputfile:
    code = inputfile.read()

part1 = getSum(code)

code = 'QSTART' + code.replace('don\'t()', 'QSTOP').replace('do()', 'QSTART')
sections = code.split('Q')
part2 = sum(getSum(s) for s in sections if s.startswith('START'))

print(f'part 1: {part1}')
print(f'part 2: {part2}')