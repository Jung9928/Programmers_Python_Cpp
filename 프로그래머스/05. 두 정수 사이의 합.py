def solution(a, b):
    answer = 0

    # for문의 range에 범위지정을 쉽게 하기 위해
    # a가 b보다 클 경우, a와 b 값을 서로 바꿔준다.
    if a > b:
        a, b = b, a

    # a부터 b까지 수를 모두 더한다.
    for i in range(a, b + 1):
        answer += i

    return answer