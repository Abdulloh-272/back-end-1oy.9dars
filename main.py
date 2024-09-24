

son1 = int(input('Birinchi sonni kiriting: '))
son2 = int(input('Ikkinchi sonni kiriting: '))
son3 = int(input('Uchinchi sonni kiriting: '))

tartib = 0

if son1 < son2 and son1 < son3 and son2 < son3:
    tartib = son1, son2 , son3
    print(1, tartib)
elif son1 < son2 and son1 < son3 and son2 > son3:
    tartib = son1, son3 , son2
    print(1.2, tartib)
elif son2 < son1 and son2 < son3 and son1 < son3:
    tartib = son2, son1, son3
    print(2, tartib)
elif son2 < son1 and son2 < son3 and son1 > son3:
    tartib = son2, son3, son1
    print(2.2, tartib)
elif son3 < son1 and son3 < son2 and son2 < son1:
    tartib = son3, son2, son1
    print(3, tartib)
elif son3 < son1 and son3 < son2 and son2 > son1:
    tartib = son3, son1, son2
    print(3.3, tartib)


belgi = input('Itioriy narsa kiriting: ')

if belgi.isalpha(): 
    print("harf")
elif belgi.isdigit():  
    print("son")
else:  
    print("belgi")


son_1 = int(input('Birinchi sonni kiriting: '))
son_2 = int(input('Ikkinchi sonni kiriting: '))
son_3 = int(input('Uchinchi sonni kiriting: '))

son_equal = 0

if son_1 > son_2 and son_1 > son_3 and son_2 > son_3:
    son_equal = son_1 + son_3
    print(1,son_equal)
elif son_1 > son_2 and son_1 > son_3 and son_2 < son_3:
    son_equal = son_1 + son_2
    print(2,son_equal)
elif son_2 > son_1 and son_2 > son_3 and son_1 > son_3:
    son_equal = son_2 + son_1
    print(3,son_equal)
elif son_2 > son_1 and son_2 > son_3 and son_1 < son_3:
    son_equal = son_2 + son_1
    print(4,son_equal)
elif son_3 > son_1 and son_3 > son_2 and son_1 < son_2:
    son_equal = son_3 + son_1
    print(5,son_equal)
elif son_3 > son_1 and son_3 > son_2 and son_1 > son_2:
    son_equal = son_3 + son_2
    print(6,son_equal)



















