#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    scanf("%d", &N);
    string num_to_word[] = {"zero", "one", "two",   "three", "four",
                            "five", "six", "seven", "eight", "nine"};
    if (1 <= N && N <= 9) {
        cout << num_to_word[N] << endl;
    } else {
        cout << "Greater than 9" << endl;
    }
    return 0;
}
