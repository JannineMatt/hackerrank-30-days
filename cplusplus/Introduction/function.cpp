#include <cstdio>
#include <iostream>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
    int num[] = {a, b, c, d};
    int max = a;
    for (size_t i = 1; i < 4; i++) {
        if (max < num[i]) {
            max = num[i];
        }
    }
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}
