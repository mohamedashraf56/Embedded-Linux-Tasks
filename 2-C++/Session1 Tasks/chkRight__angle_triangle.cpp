#include <iostream>
#include<iomanip>
#include <cmath>
using namespace std;

int main()
{
    int n1,n2, n3;
    cout << "PLEASE ENTER 3 Values\n";
    std::cin >> n1 >> n2 >> n3;

    if (pow(n1,2)+pow(n2,2)==pow(n3,2)    ||  pow(n2, 2) + pow(n3, 2) == pow(n1, 2)  || pow(n1, 2) + pow(n3, 2) == pow(n1, 2) )
    {
        std::cout << "these Values can form Right Angle Triangle\n ";
    }
 
    else
        std::cout << "Nooot Right Angle Triangle\n ";
 
    return 0;
}
