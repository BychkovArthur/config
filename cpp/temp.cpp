#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define max2(x, y) (x > y ? x : y)
#define min2(x, y) (x < y ? x : y)
#define max3(x, y, z) (x > max2(y, z) ? x : max2(y, z))
#define min3(x, y, z) (x < min2(y, z) ? x : min2(y, z))

using namespace std;

using ll = int64_t;
using ull = uint64_t;
using vi = vector<int>;
using vll = vector<ll>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

template <typename _Key, typename _Tp>
using umap = unordered_map<_Key, _Tp>;
template <typename _Value>
using uset = unordered_set<_Value>;

static const ll mod1 = 1'000'000'007;
static const ll mod2 = 2'147'483'647;

/*
    IO
*/

template<typename T, typename V>
ostream& operator<<(ostream& os, pair<T, V> pr) {
    os << pr.first << ", " << pr.second;
    return os;
}

template<typename Container, typename = void>
struct is_map : std::false_type {};

template<typename K, typename V>
struct is_map<map<K, V>> : std::true_type {};

template<typename K, typename V>
struct is_map<umap<K, V>> : std::true_type {};

template<typename Container>
typename std::enable_if<!is_map<Container>::value>::type
print(const Container& container) {
    for (const auto& elem : container) {
        cout << elem << ' ';
    }
    cout << endl;
}

template<typename Map>
typename std::enable_if<is_map<Map>::value>::type
print(const Map& mp) {
    for (const auto& kv : mp) {
        cout << kv.first << " : " << kv.second << '\n';
    }
    cout << endl;
}

/*
    IO
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    return 0;
}
