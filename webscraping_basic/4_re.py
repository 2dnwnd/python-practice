import re

p = re.compile('ca.e') #3 원하는 형ㅇ태


def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열 반환
        print(m.string) # 입력받은 문자열
        print(m.start()) # 일치하는 문자열의 시작 인덱스
        print(m.end()) # 일치하는 문자열의 끝 인덱스
        print(m.span()) # 일치하는 문자열의 시작과 끝 인덱스
    else:
        print('매칭되지 않음')

m = p.match('case') # match : 주어진 문자열의 처음부터 일치하는지 확인

# m = p.search('good care') # search : 주어진 문자열 중에 일치하는거 확인
print_match(m)

lst = p.findall('careless') #findall : 일치하는 모든것을 리스트로 반환
print(lst)