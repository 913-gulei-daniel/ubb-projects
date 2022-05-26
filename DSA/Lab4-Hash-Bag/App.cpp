#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;


bool isPrime(int n){
    if(n == 2) return true;
    if(n < 2) return false;
    if(n%2 == 0) return false;

    for(int i = 3; i * i <= n; i+=2){
        if(n%i == 0)
            return false;

    }

    return true;

}

int main() {
    int lmax = 10;
    int chars = 26;
    int ct = 0;
    long long currCombos = 1000000000;
    chars -= 9;

    while(currCombos > 1){
        currCombos /= 2;
        ct ++;

    }

    currCombos *= 1000000000;
    chars -= 9;

    while(currCombos > 1){
        currCombos /= 2;
        ct ++;

    }

    currCombos *= 100000000;

    while(currCombos > 1){
        currCombos /= 2;
        ct ++;

    }

    cout<<ct;

    return 0;

}