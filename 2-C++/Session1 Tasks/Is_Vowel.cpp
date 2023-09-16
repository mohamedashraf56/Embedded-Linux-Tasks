#include <iostream>
#include<iomanip>
#include <cmath>
using namespace std;

int main()
{
    string Vowel_letters = "aoeiuAOEIU";  //string of capital and small Vowels
        char letter;

    cout << "please Enter The Letter\n";
    cin >> letter;

      for (int i : Vowel_letters)
      {
          if (i == letter)    //check inpus equal any of vowels 
          {
              cout << "The letter is Vowel\n";
              return 0;
          }

      }
  cout << "Is Not Vowel\n";
  
}
