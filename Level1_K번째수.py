def solution(array, commands):
    answer = []
    stack = []

    for i in commands:
        # commands 내의 1번째 list 값에서 [2, 5]를 가져와서 인덱스로 사용
        # 즉, array[2 : 5]가 되는데 array의 2번째부터 5번째를 자르면
        # [5, 2, 6, 3]이다. 하지만 배열은 인덱스가 0부터 시작하므로,
        # 실제 2번째 값은 array[1]이므로, -1을 해줘야 한다.
        stack = array[i[0] - 1: i[1]]
        stack.sort()

        # 마찬가지 이유로 -1을 했다.
        answer.append(stack[i[2] - 1])

    return answer