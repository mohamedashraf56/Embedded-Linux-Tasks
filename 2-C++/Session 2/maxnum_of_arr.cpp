#include <algorithm>
#include <iostream>
#include<string.h>

int main ()
{
 int arr[]={1,5,8,99,75,11,2,3};
 
std::cout<<*std::max_element(std::begin(arr),std::end(arr))<<std::endl;
//output 99

}
