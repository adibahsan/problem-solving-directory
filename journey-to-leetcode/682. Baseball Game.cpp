#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations) {
        int size = operations.size();
        stack<int> scores;

        for(int i=0; i<size; i++){
            if(operations[i]== "C"){
                scores.pop();
            } else if (operations[i]== "D"){
                int temp = scores.top();
                scores.push(temp*2);
            }  else if (operations[i]== "+"){
                int temp = scores.top();
                scores.pop();
                int temp2 = scores.top();
                scores.push(temp);
                scores.push(temp2 + temp);
            } else scores.push(stoi((operations[i])));
        }

        int total = 0;

        while (!scores.empty()){
            total += scores.top();
            scores.pop();
        }

        return total;

    }
};
int main()
{
    cout << "682. Baseball Game" <<endl;
    Solution solution;
    vector<string> ops = {"5","2","C","D","+"};

    cout << "Tournament Winners" << endl << solution.calPoints(ops) <<endl;
}
