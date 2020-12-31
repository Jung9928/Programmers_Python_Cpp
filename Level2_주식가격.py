# 문제 해결 방식 #
# 1) 각 주식가격 별, 가격하락 시간을 기록하기 위해 주식가격이 담긴 배열인 prices의 길이만큼 리스트를 생성하고 0으로 초기화.
# 2) 이중 for문으로 비교하면서 가격이 떨어졌다면 다음 인덱스로 넘어가고, 가격이 올랐다면 해당 주식 가격의 시간초 값을 1 증가시킨다.

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer