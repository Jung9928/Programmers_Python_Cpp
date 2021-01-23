#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;

	// 자르기
	for (int i = 0; i < commands.size(); i++)
	{
		// 임시 벡터를 생성 
		vector<int> temp;

		// 생성한 임시 벡터에 array[i] 부터 array[j] 까지 원소를 저장.
		// -1을 한 이유는 문제에서 원소 인덱스보다 1이 더 크므로 -1을 해준다.
		// -1을 안하게 되면 2, 6, 3만 저장될 것임.
		for (int j = commands[i][0] - 1; j < commands[i][1]; j++)
			temp.push_back(array[j]);

		// 임시 벡터 정렬
		sort(temp.begin(), temp.end());

		// k에 해당하는 인덱스 원소 저장
		// -1을 한 이유는 위의 for문에서 한 것과 동일하다. 
		// -1을 안하면 목표한 인덱스의 다음 인덱스를 참조하여 answer에 저장하게 되어버린다.
		answer.push_back(temp[commands[i][2] - 1]);
	}
	return answer;
}