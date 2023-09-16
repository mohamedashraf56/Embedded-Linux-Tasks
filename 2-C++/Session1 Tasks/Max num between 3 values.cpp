
#include <iostream>
#include<iomanip>
using namespace std;

int main()
{
    int n1, n2, n3;
    cout << "PLEASE ENTER 3 NUMBERS\n";
    std::cin >> n1 >> n2 >> n3;

    if (n1 > n2 && n1 > n3)
    {
        std::cout << "1st is the maximun number\n";
    }
    else if(n2>n1 && n2>n3)
    {
        std::cout<< "2nd is the maximun number\n";
    }
    else
        std::cout<< "3rd is the maximun number\n";
 
    return 0;
}
