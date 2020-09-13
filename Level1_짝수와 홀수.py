def solution(num):
    answer = ''

    # 2로 나누었을 때, 나머지가 0인 경우는 짝수이므로 Even 출력
    if num % 2 == 0:
        answer = ''.join('Even')

    # 그 외 홀수인 경우 이므로, 'Odd' 출력
    else:
        answer = ''.join('Odd')

    return answer