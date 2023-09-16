#include <iostream>
using namespace std;
#include <bitset>

int main()
{

	int num1;
	bitset<16>num2;

	cout << "Enter Decimal number\n";
	cin >> num1;
	cout << "Enter Binary number\n";
	cin >> num2;

	//convert from Decimal to Binary 

	bitset<16>bin = (num1);
	cout << "The binary representation :" << bin<<endl;

	//convert from binary to decimal using toulong
	cout << "The binary representation :" << num2.to_ulong() << endl;
	return 0;

}
