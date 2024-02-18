#include <iostream>
using namespace std;
//函数模板
template<typename T>
void mySwap(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    int a, b;
    cin >> a >> b;
    mySwap(a, b);
    cout << a << " " << b << endl;
    return 0;
}