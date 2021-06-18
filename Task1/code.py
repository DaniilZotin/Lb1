print ('*****************')
s = list(input('Введіть свій рядок:'))
mas = []
# Фрагмент коду за який мені стидно але він работає і харашо в майбутньому зміню
# Його задача видаляти цифри з рядка і додавати їх в масив
for i in range(len(s)): 
    if '1' in s:
        s.remove('1')
        mas.append('1')
    elif '2' in s:
        s.remove('2')
        mas.append('2')
    elif '3' in s:
        s.remove('3')
        mas.append('3')
    elif '4' in s:
        s.remove('4')
        mas.append('4')
    elif '5' in s:
        s.remove('5')
        mas.append('5')
    elif '6' in s:
        s.remove('6')
        mas.append('6')
    elif '7' in s:
        s.remove('7')
        mas.append('7')
    elif '8' in s:
        s.remove('8')
        mas.append('8')
    elif '9' in s:
       s.remove('9')
       mas.append('9')
    elif '0' in s:
        s.remove('0')
        mas.append('9')

# Був масив із рядків тепер із чисел
mas = [int(i) for i in mas]
s = ''.join(s)
print ('Масив тільки з числами',mas)
print ('Рядок без чисел:',s)

# Не бийте мене я це знайшов на stackoverflow і не докінця понімаю як воно працює АЛЕ ПРАЦЮЄ!)
def cap_both(phrase):
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), phrase.title().split()))

print ('Кожне слово починається з великої і кінчається великою:',cap_both(s))
maxnumber = max(mas)

# Видаляємо максимальний елемент з масиву щоб він нам не заважав
mas.remove(max(mas))

print("Максимальне значення в масиві:", maxnumber)
print ('Масив без максимального числа',mas)

# Цикл піднесення до степеню по індексу (не спрацює якщо не перетворити str в int)
mas2 = []
for i in range(len(mas)):
        temp = mas[i] ** i
        mas2.insert(i, temp)
print("Масив чисел піднесених до степеню по їх індексу:", mas2)
print ('*****************')

