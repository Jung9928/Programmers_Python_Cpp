def solution(participant, completion):
    participant.sort()
    completion.sort()

    # 크기가 다른 두 배열을 비교 #
    # 핵심은 길이가 서로 다른 배열이므로, 길이가 1만큼 더 작은 Completion 길이만큼만 비교를 수행
    # 마지막 참여자를 제외한 참여자 전원과 완주자가 같은 지 비교.

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            # 같지 않으면 그 사람은 완주 실패자.
            return participant[i]

            # 비교가 안된 마지막 한사람이 완주 실패자임.
    # 그 이유는 for 루프 내 if문에서 같지 않은 사람이 발견되면 return이 되는데,
    # 마지막 이 return문 까지 오게 되는 경우는 마지막 참여자를 제외한 전원이 완주했다는 의미이기 때문
    return participant[i + 1]