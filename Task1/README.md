#Опис виконаних завдань:
1) Зробити git clone свого минулого репозиторію:
![image](https://user-images.githubusercontent.com/85665335/122608665-49a96c80-d085-11eb-9a3a-9a11b8c39828.png)
2) створити папку task-0, та перемістити в неї всі файли першого завдання:
![image](https://user-images.githubusercontent.com/85665335/122609274-67c39c80-d086-11eb-884b-12825f96463c.png)
------------------------------------------->![image](https://user-images.githubusercontent.com/85665335/122609319-78741280-d086-11eb-989f-14cb326bc96b.png)<-------------------------------------------

3)А ось код моєї програми для копіювання:
```Python
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
# Задача цього фрагменту робити перші і останні букви кожного рядка великими
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
        step = mas[i] ** i
        mas2.insert(i, step)
print("Масив чисел піднесених до степеню по їх індексу:", mas2)
print ('*****************')
```
4)Коміти та їх опис:
![image](https://user-images.githubusercontent.com/85665335/122612373-ae67c580-d08b-11eb-8c2e-60f1b5d681f6.png)
-------------------------------------->![image](https://user-images.githubusercontent.com/85665335/122612864-8a58b400-d08c-11eb-96f5-bf6c8c8cd5ff.png)<--------------------------------------

5) Відправляємо все що ви зробили на GitHub:

![image](https://user-images.githubusercontent.com/85665335/122613339-5a5de080-d08d-11eb-8ca9-cab394729f57.png)








