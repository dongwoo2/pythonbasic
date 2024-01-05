# 저장하는 규칙을 만들어야함 그래서 ex01에 구분값으로 | 을 집어널었음
def lotto_input(filename):
    f = open(filename, 'r') # 파일이름 받아서 오픈해주는애 리드
    data = f.read() # 데이터 전체를 읽어들임
    f.close()
    return data # 전체 데이터 반환

def freq_counter(num_list): # 번호가 몇 번씩 나왔는지 체크해주는 함수
    freq = {k:0 for k in range(1,46)} # 1번부터 45번 0값으로 초기화

    for num in num_list:
        num = num.split(',') # numlist를 ,로 짤라서 ,로 짤린 리스트가 될건데 스플릿 함수는 문자열을 리스트로 반환
        for idx in num[1:7]: # 1번부터 6번 인덱스 앞에(회차) 번호 빼고, 뒤에 보너스 번호 뺴고 카운트
            freq[int(idx)] += 1  # 그 번호에 플러스 1을 하겠다.
    return freq

def freq_output(filename, freq): # 파일에 출력해주는 함수 filename에 freq 데이터 저장해줘
    with open(filename, 'w') as f: # 파일 쓰기모드로 열고
        for k, v in freq.items(): # 1번이 몇개~ 2번이 몇개~ 하면서 쓰기
            f.write(f'{k}:{v},')

data = lotto_input('lotto.txt')
num_list = data.split('|')
freq = freq_counter(num_list)
freq_output('bindo.txt', freq)
