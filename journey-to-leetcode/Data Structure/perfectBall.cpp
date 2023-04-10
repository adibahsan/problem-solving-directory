#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int perfect_number(vector<int>& balls, int x, int y, int z) {
    int perfect_count = 0;
    int n = balls.size();

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (abs(balls[i] - balls[j]) <= x) {
                for (int k = j + 1; k < n; k++) {
                    if (abs(balls[j] - balls[k]) <= y && abs(balls[i] - balls[k]) <= z) {
                        perfect_count++;
                    }
                }
            }
        }
    }

    return perfect_count;
}

int main() {
    vector<int> balls = {3, 0, 1, 1, 9, 7};
    int x = 7, y = 2, z = 3;
    int perfect_count = perfect_number(balls, x, y, z);
    cout << "Perfect Number: " << perfect_count << endl;
    return 0;
}
