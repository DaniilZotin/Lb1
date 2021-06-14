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
        

