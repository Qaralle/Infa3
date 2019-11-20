def INTKOTORIYYASDELAL(l):
    k=0
    for a in l:
        k=k*10+ ord(a)-48 # орд - номер символа по таблице юникод для '0' = 48
    return k

def convert1(a):
    l=list(a)
    s = len(l)
    k=0
    for i in range(0,s):
        l[i]=INTKOTORIYYASDELAL(l[i])*pow(-10,s-1-i) #обычная система перевода
        k=k+l[i]
    return k

def convert2(a):
    l=a.split('.')  #разделяем входную строку на тетрады
    k=list(l[0])
    new=0
    stroka=''
    while len(k)<4:  # дополняем самуе левую тетраду нулями
        k.insert(0,0)
    l[0]=''.join(map(str,k)) # приобразуем в список с элементами типа стринг
    for i in range(0,len(l)):
        k = list(l[i])   # берем тетрады по очреди
        for j in range(0,len(k)):
            new=new+INTKOTORIYYASDELAL(k[j])*(pow(2, 4-1-j))  #переводим тетраду в 10-ю СС
        if new == 10:
            stroka = stroka + 'A'
        elif new == 11:
            stroka = stroka + 'B'
        elif new == 12:
            stroka = stroka + 'C'
        elif new == 13:                  #Букавы для 16-й СС
            stroka = stroka + 'D'
        elif new == 14:
            stroka = stroka + 'E'
        elif new == 15:
            stroka = stroka + 'F'
        else:
            stroka=stroka+str(new)
        new=0  #обнуление перед седующей тетрадой
    return stroka

def printf(dano, nado, iz, v):   #метод что бы не писать огромные принты
    res = ' | '.join(['{} -> {}'.format(i, j) for i, j in zip(iz, v)]) #zip бере на вход списки iz и v и группирует 1 с 1 2 со 2 , формат подставляет в шаблон , join объеденяет в 1 строку разделяя |
    print('{} -> {} : {}'.format(dano, nado, res))

res=[]
with open('file.txt') as f:    #читаем файл как ф
    lines = f.readlines() # по линям? lines список из строк
for line in lines:
    lst = line.split()
    dano=lst[0]
    nado=lst[1]
    iz=lst[2:]

    if dano =='-10':
        for i in range(2,len(lst)):
            res.append(convert1(lst[i]))

    if dano =='2':
        for i in range(2,len(lst)):
            res.append(convert2(lst[i]))

    printf(dano,nado,iz,res)
    res=[]
input()




