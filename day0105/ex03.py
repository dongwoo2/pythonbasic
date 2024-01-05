def freq_input(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data

def freq_print(freq, limit, reverse=True): # 프린트 하는 함수 리버스라는 매개변수 하나 맘들어서 오름차순,내림차순 할 수 있게
    freq = sorted(freq.items(), key = lambda x:x[1], reverse=reverse)
    for idx in range(0, limit):
        print(f'[{freq[idx][0]:2}]번:({freq[idx][1]:2})회')


data = freq_input("bindo.txt")
freq_list = data.split(',')
freq_list.pop()
freq = {k+1:int(v.split)(':')[1] for k,v in enumerate(freq_list)}
freq_print(freq,45)
print()
print('가장 많이 1등에 당첨된 번호')
freq_print(freq,6)
print()
print('가장 적게 1등에 당첨된 번호')
freq_print(freq, 6, reverse=False)