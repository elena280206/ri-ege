print('Введите x')
x = int(input())
print('Введите y')
y = int(input())
if x > 0 and y > 0:
    print('1я четверть')
if x > 0 and y < 0:
    print('2я четверть')
if x < 0 and y< 0:
    print('3я четверть')
if x< 0 and y > 0:
    print('4я четверть')