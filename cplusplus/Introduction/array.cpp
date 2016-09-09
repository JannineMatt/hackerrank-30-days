#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int size;
    cin >> size;
    int numarr[size] = {0};
    for (int i = 0; i < size; i++) {
        cin >> numarr[i];
    }
    for (int i = size - 1; i >= 0; i--) {
        cout << numarr[i] << " ";
    }
    return 0;
}
