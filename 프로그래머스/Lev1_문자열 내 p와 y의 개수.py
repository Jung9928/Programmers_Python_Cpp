def solution(s):
    answer = True
    pcnt = 0  # 'p'의 개수를 카운트
    ycnt = 0  # 'y'의 개수를 카운트

    # 'p'와 'y'의 개수를 비교하여 같으면 true 다르면 false
    # 비교 시, 대소문자 구분 안하는게 조건이므로, 전부 소문자로 치환
    for i in s.lower():
        if i == 'p':
            pcnt += 1
        elif i == 'y':
            ycnt += 1

    if pcnt == ycnt:  # 'p', 'y' 개수 같은 경우 True 출력
        return answer
    elif pcnt != ycnt:  # 'p', 'y' 개수가 다른 경우 False 출력
        return not answer

    # 'p'와 'y' 모두 하나도 없는(개수가 0) 경우 항상 true
    return True
