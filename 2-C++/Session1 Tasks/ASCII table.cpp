#include <iostream>
#include<iomanip>
using namespace std;

int main()
{
    unsigned char ch;
    std::cout << "+ ---------- + ----------+" << endl;

    std::cout << "|  Char      |  ASCIII   |" << endl;
    std::cout << "+ ---------- + ----------+" << endl;

    for (ch = 65; ch < 123; ch++)
    {
        std::cout << "|" << left << setw(12) << ch << "|" << left << setw(11) << (int)ch << "|" << endl;
    }
    return 0;
}
