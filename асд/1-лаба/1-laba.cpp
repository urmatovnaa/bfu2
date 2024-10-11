#include <iostream>
#include <fstream>

#include <vector>

#include <cmath>
#include <string>

using namespace std;

int main(){
    setlocale(0, "RU");

    string input;
    vector<char> data;
    bool correct = true;
    
    cout<< "Введите строку: " <<endl;
    cin>> input;

    for (int i = 0; i < input.length(); i++) {
        if (input[i] == '(' or input[i] == '[' or input[i] == '{'){
            data.push_back(input[i]);
        }
        else if (input[i] == ')' and data.back() == '('){
            data.pop_back();
        }
        else if (input[i] == '}' and data.back() == '{'){
            data.pop_back();
        }
        else if (input[i] == ']' and data.back() == '['){
            data.pop_back();
        }
        else {
            correct = false;
            break;
        }
    }
    if (correct){
        cout << "Строка правильная" << endl;
    }
    else {cout << "Строка не правильная" << endl;}
}