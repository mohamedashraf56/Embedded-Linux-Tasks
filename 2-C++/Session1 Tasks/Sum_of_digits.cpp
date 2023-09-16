#include <iostream>
#include<iomanip>
#include <cmath>
using namespace std;


int main()
{
	int num;
	cout << "Please enter a number " << endl;
	cin >> num;
	int sum = 0,digit=0;
	

	for (; num > 0;)
	{
		digit = num % 10;
		sum += digit;
		num /= 10;
	}

	cout << endl<< "The sum of num's digits = " << sum << endl;


}
