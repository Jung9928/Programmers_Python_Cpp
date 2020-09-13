def solution(numbers):
    # 인자로 받은 정수가 저장된 list인 numbers를 문자열로 변환하고 map으로 변환 후,
    # 마지막으로 list 형태로 변환하여 numbers에 다시 저장.
    numbers = list(map(str, numbers))

    # 람다식을 통해 [6, 10, 2]가 [666, 101010, 222]가 되고
    # sort 함수에서 reverse=True를 해주었기 때문에 내림차순으로 정렬하게 되며
    # sort 함수가 내부적으로 정렬하기 위해 각 list내 element들을 비교하게 되는데
    # 비교할 때, 각 요소의 첫 인덱스
    # (ex: 666이라면 맨 앞의 6과 101010의 맨 앞의 1과 222의 2를 ASCII 값으로 변환하여 비교하게 된다.)
    # 만약 각 element들의 맨 앞의 숫자가 같은 경우, 다음 2번째 숫자끼리 비교하게 된다.
    # 그렇기 때문에 x*3한 이유는 최대한 많은 자릿수를 비교하여 정렬하기 위함이다.
    # 그 결과 [666, 222, 101010]으로 정렬되며, 앞 자리 수 만으로 정렬이 되었으므로
    # 비교를 당한 앞자리 수만 정렬되어 numbers에 저장된다.
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 정렬한 numbers를 join 함수를 사용하여 numbers에 저장된 각 정수를 하나로 통합하고,
    # int를 사용하여 정수로 변환한 뒤 str을 사용하여 문자열로 최종적으로 변환하여 return
    return str(int(''.join(numbers)))