#include <iostream>
#include <vector>
using namespace std;

#define INF (unsigned)-1
#define io(v) cin >> v
#define toStr(str) #str
#define foreach(v, i) for (int i = 0; i < v.size(); i++)

#define FUNCTION(name, operator)                                               \
    inline void name(int &current, int candidate) {                            \
        !(current operator candidate) ? current = candidate : false;           \
    }
#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    foreach (v, i) { io(v)[i]; }
    int mn = INF;
    int mx = -INF;
    cout << INF << endl;
    foreach (v, i) {
        minimum(mn, v[i]);
        maximum(mx, v[i]);
    }
    int ans = mx - mn;
    cout << toStr(Result =) << ' ' << ans;
    return 0;
}
