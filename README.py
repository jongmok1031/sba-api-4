"""
n: bool fn
n + activation = pn
nn = bool + activation
ann = bool + act + cost
dnn = ann  + ann + ...

cnn = dnn + convolution    => 이미지 분류. time fcn불필요
rnn = dnn + recurrent    => order   => context => 자연어처리.
lstm = rnn + time   =>sequential => 미래에 대한 예측

플라스크 개발환경
template리턴 -> legacy 방식 
json리턴 -> restful 방식 -> api서버가 만들어짐

wgsi 방식으로 전환
1. RESTful 로 전환
2. setup.py 생성, setuptools를 활용한 설정
3. root - folder 생성
    - package : __init__.py (o)
    - directory : __init__.py (x)
"""