
#include <iostream>
#include "Matrix.h"
#include "ExtendedTest.h"
#include "ShortTest.h"

#include <cstring>
using namespace std;


int main() {
    testExtra();
	testAll();
	testAllExtended();
	cout << "Test End" << endl;
	system("pause");

}