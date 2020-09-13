def solution(s):
    answer = ''

    # 문자열 길이가 홀수면 가운데 글자는 무조건 1개가 나오므로,
    # 가운데 문자 return
    if len(s) % 2 != 0:
        answer = s[len(s) // 2]

    # 문자열 길이가 짝수면 가운데 글자는 2개가 되므로,
    # 슬라이싱을 통해 2글자를 추출
    elif len(s) % 2 == 0:
        answer = s[(len(s) // 2) - 1: (len(s) // 2) + 1]

    return answer