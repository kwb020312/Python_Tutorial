# 🐍파이썬 기초 학습하기!

### 😀설치방법

[파이썬 공식 사이트](https://www.python.org/)에 접속하여 다운로드

`python --version`을 실행하여 버전을 확인한다.

### 😁데이터 타입

`python`의 데이터 타입은 `숫자`, `문자`, `리스트`, `튜플`, `매핑`, `불`, `세트`가 있다.

### 😂기본 연산

`+`, `-`, `%`, `/`, `*`, `>`, `<`, `==`, `>=`, `<=`, `!=`, `and`, `or`등 다양한 데이터 연산자를 지원한다.

### 🤣문자열 연산

```python
text1 = "김우빈"
test2 = "문관우"
test3 = "바보"

total_text = test1 + " " + text2 + " " + text3
print(total_text)
# return "김우빈 문관우 바보"
```

### 😃데이터 입력

입력은 `input`함수를 사용하여 작성된다. 기본적으로 입력받은 데이터는 `str`형으로 입력되며, 숫자로 사용하고 싶은 경우 자료형 변환을 해야한다.

```python
x = input("num1")
y = input("num2")

print(x * y) # return error

x = int(input("num1"))
y = int(input("num2"))

print(x * y) # return num1 * num2
```

### 😄조건문

`python`의 조건문은 `if`문에 `{}`를 붙이지 않으며 `:`로 블록처리를 진행한다.
이후 `tab`을 활용해 구문을 작성하며 `if`, `elif`, `else`로 나뉜다.

### 😅리스트

`python`의 `리스트`는 `배열`을 의미한다. 인덱스로 접근이 가능하며 선언방식은 아래와 같다.

```python
# 데이터 선언
test = [1, 2, 3, 4, 5]

# 데이터 접근
print(test[2]) # return 3

# 데이터 추가
test.append(6) # [1,2, ... 6]

# 데이터 삭제
del test[1] # [1, 3, ... 6]

# 데이터 슬라이싱
print(test[1:3]) # [3, 4]

# 데이터 길이
print(len(test)) # return 5

# 데이터 정렬
test.sort() # 사전 순 오름차 순
test.sort(reversed=True) # 사전 순 내림차 순
```
