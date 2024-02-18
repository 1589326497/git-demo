/**
 * @file lx.cpp
 * @author 宁子希 (1589326497@qq.com)
 * @brief 
 * @version 0.1
 * @date 2024-02-18
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include <iostream>
using namespace std;
//函数模板
/**
 * @brief 
 * 
 * @tparam T 
 * @param a 
 * @param b 
 */
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