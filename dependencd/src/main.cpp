#include <iostream>
#include "add.h"
using namespace std;

int main() {
    int a = 10, b = 20;
    int c = add(a, b);
    cout << "Result is " << c << endl;
    return 0;
}