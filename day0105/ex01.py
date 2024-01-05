from random import randrange # 랜덤 임포트

def lotto_generator(): # 로또 번호 생성용 함수
    numset = set() # 중복제거용 set 객체 생성
    while len(numset) < 7: # 7까지 생성
        numset.add(randrange(1,46)) # 1부터 45까지 랜덤 숫자 더하기
    return sorted(list(numset)) # 셋 리스트 오름차순으로 변환

def lotto_dict_generator(n): # n개 수만큼 생성해주는 함수
    lotto_dict = {} # 딕셔너리 객체 생성
    for i in range(1, n+1): # n개 수만큼 포문 동작
        nums = lotto_generator() # nums에 리스트로 로또번호 반환
        bonus = nums.pop(randrange(0,7)) # nums에서 0~6번 째 인덱스중에서 랜덤으로 꺼내서 bonus에 반환
        lotto_dict[i] = (nums,bonus) # 딕셔너리 객체에 키값은 숫자로 밸류값은 튜플 nums,bonus로 추가
    return lotto_dict

def lotto_output(filename, lotto_dict):
    with open(filename, 'w', newline ='') as f: # 파일네임 받아서 열고 쓰기모드 그리고 f라는 이름으로 참조
        for k, nums in lotto_dict.items(): # 키, 밸류 언패킹해주고
            tmp = list(nums[0]) # 첫 번째 요소 인덱스 6자리
            tmp.insert(0,k) # 키값 번호
            tmp.append(nums[1]) # 보너스 번호
            tmp = str(tmp).replace('[', '').replace(' ','').replace(']', '|') # 변환
            f.write(tmp) # 파일에 써주기

lotto_dict = lotto_dict_generator(100)
lotto_output("lotto.txt",lotto_dict)