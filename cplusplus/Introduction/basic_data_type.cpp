#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int var1;
    long var2;
    long long var3;
    char var4;
    float var5;
    double var6;

    scanf("%d %ld %lld %c %f %lf", &var1, &var2, &var3, &var4, &var5, &var6);
    printf("%d\n", var1);
    printf("%ld\n", var2);
    printf("%lld\n", var3);
    printf("%c\n", var4);
    printf("%f\n", var5);
    printf("%lf\n", var6);
    return 0;
}
