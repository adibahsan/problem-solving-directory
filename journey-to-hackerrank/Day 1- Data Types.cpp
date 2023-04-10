#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";


       int c1;
    double d1;
    string s1;
    // Read and save an integer, double, and String to your variables.
    // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
    cin >> c1 >> d1;
    getline(cin >> ws, s1);
    // Print the sum of both integer variables on a new line.
    cout << c1+i << endl;
    // Print the sum of the double variables on a new line.
    cout << setprecision(1) << fixed;
    cout << d1 + d << endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s + s1 << endl;
    return 0;
}
