# Lb1
1) Клонуємо свій репозиторій:
![image](https://user-images.githubusercontent.com/85665335/122061328-10f46380-cdf7-11eb-97ba-d8ed8489f0d4.png)
2) Створюємо новий файл( в форматі py):
![image](https://user-images.githubusercontent.com/85665335/122062137-cd4e2980-cdf7-11eb-857d-dd39988c1fb9.png)
3) Пишемо свою чудову або не дуже програму:
![image](https://user-images.githubusercontent.com/85665335/122062428-12725b80-cdf8-11eb-9db3-1385247684f3.png)
4) Комітимо ( не забуваємо написати що ми зробили ):
![image](https://user-images.githubusercontent.com/85665335/122063444-f0c5a400-cdf8-11eb-87bd-01591062b64b.png)
5) Відправляємо на GitHub:
![image](https://user-images.githubusercontent.com/85665335/122063734-33877c00-cdf9-11eb-8776-4cb61ddb8d99.png)

6)Код моєї програми для зручного копіювання:
```python
from random import randint 

max_nubr = 0
name = []
print ("\n30 Випадкових цілих чисел")
for i in range(30) :
    name.append(randint(-100,100))
print (name)
for i in name :
    if i > max_nubr:
        max_nubr = i
print ('Максимальне число:',max_nubr,"його позиція -",name.index(max_nubr)+1)
print ('Оновлений список, складається тільки з непарних  в порядку зменшення:')
name.sort(reverse = True)
for i in name:
    if i % 2 == 0:
        continue
    print (i)
```





