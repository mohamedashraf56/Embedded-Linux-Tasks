#include <iostream>
#include <vector>

int arr_search (const std::vector<int>&arr,int target)
{
    for (int num:arr)
    {
        if(num == target)
        {
            return 1;           //number found
        }
    }

    return 0;                  //not found   
}


int main()
{
    while (1)
    {
    std::vector<int> numbers={7,8,9,10,99,5,2};
    int target;

    std::cout<<"Please enter the num to search for"<<std::endl;
    std::cin>>target;

    int Is_found=arr_search(numbers,target);

    if (Is_found)
    {
        std::cout<<"the number is founded"<<std::endl;
    }
    else{
     std::cout<<"the number is nooot founded"<<std::endl;   
    }
    }

    return 0;
}
