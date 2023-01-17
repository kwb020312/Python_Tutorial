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
