# 프로그래머스 Level-2 스킬트리 #
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 문제 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 선행 스킬 순서가 "스파크 -> 라이트닝 볼트 -> 썬더" 일때, "썬더"를 배우려면
# 먼저 "라이트닝 볼트"를 배워야 하고, "라이트닝 볼트"를 배우려면 먼저 "스파크"를 배워야 한다.
# 위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있다.
# 따라서, "스파크 -> 힐링 -> 라이트닝 볼트 -> 썬더" 와 같은 스킬트리는 가능하지만,
# "썬더 -> 스파크" 나 "라이트닝 볼트 -> 스파크 -> 힐링 -> 썬더"와 같은 스킬트리는 불가능하다.

# 선행 스킬 순서 skill과 유저들이 만든 스킬트리를 담은 배열 skill_trees가 매개변수로 주어질 때,
# 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해라

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 제한 조건 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 1) 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있다.
# 2) 스킬 순서와 스킬트리는 문자열로 표기한다. ex) C -> B -> D 라면 "CBD"로 표기
# 3) 선행 스킬 순서 skill의 길이는 1이상 26이하이며, 스킬은 중복해 주어지지 않는다.
# 4) skill_trees는 길이 1이상 20이하인 배열이다.
# 5) skill_trees의 원소는 스킬을 나타내는 문자열이다.
#   -> skill_trees의 원소는 길이가 2 이상 26이하인 문자열이며, 스킬이 중복해 주어지지 않는다.


def solution(skill, skill_trees):
    answer = 0

    # 유저들이 만든 스킬트리를 담은 배열인 skill_trees의 원소 하나를 꺼냄.
    for i in skill_trees:
        # 선행 스킬 순서인 skill과 skill_trees의 원소를 비교하여 skill_trees의 원소가
        # skill 배열의 원소에 포함되는 원소들을 저장할 list 생성
        list = []
        check = True    # list에 저장된 데이터가 skill 배열 원소의 각 인덱스 값과 일치하는지 체크하기 위한 변수

        # skill_trees의 원소 하나를 가져와서 skill 배열의 있는 원소와 같으면 list에 저장
        for j in range(len(i)):
            if i[j] in skill:
                list.append(i[j])

        # skill 배열의 길이와 list길이가 같아지기 때문에 list의 길이만큼 반복문을 수행하여
        # list의 원소와 skill 배열의 원소 비교.
        for k in range(len(list)):
            # 만약 다른 경우, 스킬 트리가 아니게 된다.
            if list[k] != skill[k]:
                check = False
                break

        # 위 for문에서 check 변수 값이 True가 되는 경우는 스킬 트리인 skill과 list의 원소가 모두 같은 경우.
        if check == True:
            answer += 1

    return answer