def menus():
    print('1. bacon 5000won, 2. icecream 3000won, 3. potato 1000won, 4.next people, 5.end, 6. point insert, 7.next day, 8.receipt select')

def icecream(icecnt):
    if(icecnt < 10):
        need = 10 - icecnt
    else:
        ice = icecnt % 10
        need = 10 - ice
    print(f'need the icecream about {need}')

def potato(potatocnt,icecnt):
    if(potatocnt < icecnt):
        need = icecnt - potatocnt
        print('potato is lower price than icecream')
        print(f'need the potatocnt about {need}')

def food_choice(ch,foodcnt,money,discount,foodlist):
    disprices = {}
    paymoney = 0
    if(discount != 0):
        for food, price in foodlist.items():
            disprice = price * 0.95
            disprices[food] = disprice
    else:
        for food, price in foodlist.items():
            disprices[food] = price
    if(ch == 1 and money >= disprices['bacon']) :
        paymoney += disprices['bacon']
        money -= disprices['bacon']
        foodcnt[0] += 1
        return [money, paymoney, foodcnt]
    elif(ch == 2 and money >= disprices['icecream']):
        paymoney += disprices['icecream']
        money -= disprices['icecream']
        foodcnt[1] += 1
        return [money, paymoney, foodcnt]
    elif(ch == 3 and money >= disprices['potato']):
        paymoney += disprices['potato']
        money -= disprices['potato']
        foodcnt[2] += 1
        return [money, paymoney, foodcnt]
    else :
        print('no money')
        return 
    
def earns_point(paymoney):
    pointcnt = (paymoney/10000)
    point = pointcnt * 1000
    return point

def people_insert(peoplec,point,allsequence, discount):
    peopledict = {}
    peopledict[allsequence] = peoplec + [point] + [discount]
    return peopledict

def receipt_select(peopledicts, daypeople, day, month):
    foodcnt = [0,0,0]
    fdays = 0
    ldays = 0
    cl = 0
    while d <= day and m <= month:
        d = 1 
        m = 1
        print(f'{d}. {m}war {d}il')
        d += 1
    ch = int(input('choose that one'))
    if(ch == 1):
        firstday = 1
        lastday = daypeople[ch]
    else:
        chcopy = ch
        while chcopy >= 1:
            fdays += daypeople[chcopy-1]
            ldays += daypeople[chcopy]
            chcopy -= 1
        firstday = fdays + 1
        lastday = ldays
    for i in range(firstday,lastday):
        foodcnt[0] += peopledicts[i][2]
        foodcnt[1] += peopledicts[i][3]
        foodcnt[2] += peopledicts[i][4]
    for i in range(firstday,lastday):
        if cl == 0:
            if(foodcnt[0] > 0 ):
                print(f'bacon * {foodcnt[0]} = {foodcnt[0]*5000}')
            if(foodcnt[1] > 0 ):
                print(f'icecream * {foodcnt[1]} = {foodcnt[1]*3000}')
            if(foodcnt[2] > 0 ):
                print(f'potato * {foodcnt[2]} = {foodcnt[2]*1000}')
            cl += 1
        print('==============================')
        if(peopledicts[i][6] > 0):
            print("discounted people!!")
        print(f'organic money : {peopledicts[i][0]}')
        print(f'paymoney money {peopledicts[i][1]}')
        print(f'bacon: {peopledicts[i][2]}')
        print(f'icecream: {peopledicts[i][3]}')
        print(f'potato: {peopledicts[i][4]}')
        if(peopledicts[i][5] > 0):
            print(f'point: {peopledicts[i][5]}')
        
        


# def receipt_select():
    
flag = True
flag2 = True
sequence = 1
allsequence = 1
allpeople = 0
month = 1
day = 1
foodlist = {'bacon' :5000, 'icecream':3000, 'potato':1000}
foodcnt = [0,0,0,0,0] # 
discount = 0
ch4 = 0
gubun = 0
paymoney = 0
point = 0
peopledicts = {}
daypeople = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while flag:
    print(f'{month} war {day} il')
    people = int(input('hows about people count?'))
    allpeople += people
    while flag2:
        if(gubun == 0):
            print(f'{sequence} people how have money?' )
            money = int(input())
            organicmoney = money
            gubun += 1

        menus()
        ch = int(input())

        if ch <= 3:
            peoplec = food_choice(ch, foodcnt, money, discount, foodlist)
            foodcnt[0] = peoplec[2][0]
            foodcnt[1] = peoplec[2][1]
            foodcnt[2] = peoplec[2][2]
            paymoney = peoplec[1]
            money = peoplec[0]
        elif ch == 4 or ch == 5:
            if foodcnt[1] % 10 != 0:
                icecream(foodcnt[1])
                ch4 += 1
            if foodcnt[3] < foodcnt[2]:
                potato(foodcnt[2], foodcnt[1])
                ch4 += 1
            if(ch4 == 0 and ch == 4):
                peopledicts.update(people_insert(peoplec, point, allsequence, discount))
                for i in range(len(foodcnt)):
                    foodcnt[i] = 0
                if(discount > 0):
                    discount -= 1
                gubun = 0
                daypeople[day] += 1
                sequence += 1
                allsequence += 1
            if(ch4 == 0 and ch == 5):
                #se2 += 1
                se2 = 1
                flag = False
                flag2 = False
        elif ch == 6:
            if(paymoney > 10000):
                point = earns_point(paymoney)
                print(f'your points is {point}')
        elif ch == 7:
            peopledicts.update(people_insert(peoplec, point, allsequence, discount))
            for i in range(len(foodcnt)):
                foodcnt[i] = 0
            if(allpeople > allsequence):
                discount = allpeople - allsequence
            print(f'{discount}명 이전되었습니다.')
            allsequence += 1
            daypeople[day] += 1
            day += 1
            flag2 = False
            
            



