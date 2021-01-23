#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;

	// �ڸ���
	for (int i = 0; i < commands.size(); i++)
	{
		// �ӽ� ���͸� ���� 
		vector<int> temp;

		// ������ �ӽ� ���Ϳ� array[i] ���� array[j] ���� ���Ҹ� ����.
		// -1�� �� ������ �������� ���� �ε������� 1�� �� ũ�Ƿ� -1�� ���ش�.
		// -1�� ���ϰ� �Ǹ� 2, 6, 3�� ����� ����.
		for (int j = commands[i][0] - 1; j < commands[i][1]; j++)
			temp.push_back(array[j]);

		// �ӽ� ���� ����
		sort(temp.begin(), temp.end());

		// k�� �ش��ϴ� �ε��� ���� ����
		// -1�� �� ������ ���� for������ �� �Ͱ� �����ϴ�. 
		// -1�� ���ϸ� ��ǥ�� �ε����� ���� �ε����� �����Ͽ� answer�� �����ϰ� �Ǿ������.
		answer.push_back(temp[commands[i][2] - 1]);
	}
	return answer;
}