#include <iostream>
#include<iomanip>
#include <cmath>
using namespace std;


int main()
{

    cout << "--------------------------------------------------------------" << std::endl;
    cout << "                      THE MUltiplication Table               " << std::endl;
    cout << "--------------------------------------------------------------" << std::endl;

    for (int i = 1; i <=12; i++)
    {
        cout << "multiplication table of : " << i << std::endl;

        for (int j = 1; j <=12; j++)
        {
            cout << i << " * " << j << " = " << i * j << std::endl;
        }
        std::cout << "--------------------------------------------------------" << std::endl;
    }

}
