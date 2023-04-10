#include<iostream>
#include<vector>

using namespace std;

const string fizzBuzz = "FizzBuzz";
const string fizz = "Fizz";
const string buzz = "Buzz";

class Solution {
public:
   static int numberOfSteps(int num) {
        int steps = 0;
        while(num >=1){
            if(num%2 == 0){
                num = num/2;
            } else {
                num = num - 1;

            }
            steps++;
        }
        return steps;
    }

    static int numberOfStepsRecur(int num) {
        if(num ==1)
        {
            cout << "returning 1"<< num <<endl;
            return 1;
        }
        else if (num %2 == 0){
            cout << "returning %2 "<< num <<endl;
            return 1 + numberOfStepsRecur(num/2);
        }

         else if (num %2 == 1){
            cout << "returning  not %2 "<< num <<endl;
            return 1 + numberOfStepsRecur(num - 1);
        }
    }
};


int main()
{
    cout << "Hellow World" <<endl;

    cout << "response" << endl << Solution::numberOfSteps(123) <<endl;

    cout << "response recurr"<< endl << Solution::numberOfStepsRecur(123) <<endl;


}
