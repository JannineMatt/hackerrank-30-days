#include <cstdio>
#include <iostream>
using namespace std;

string int_odd_even(int n) {
    if (n % 2 == 0)
        return "even";
    return "odd";
}

string int_2_word(int n) {
    string num_to_word[] = {"zero", "one", "two",   "three", "four",
                            "five", "six", "seven", "eight", "nine"};
    return num_to_word[n];
}

int main() {
    int start, end;
    cin >> start;
    cin >> end;
    for (int i = start; i <= end; i++) {
        if (0 <= i && i <= 9) {
            cout << int_2_word(i) << endl;
        } else {
            cout << int_odd_even(i) << endl;
        }
    }
    return 0;
}
