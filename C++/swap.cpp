#include <iostream>
using namespace std;
int main(){
    int holdingTank;
    int fishTank1 = 10;
    int fishTank2 = 32;

    holdingTank = fishTank1;
    fishTank1 = fishTank2;
    fishTank2 = holdingTank;
//this program swaps values.

    cout << fishTank1;
    cout << fishTank2;
    return 0;
}