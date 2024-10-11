/*Лаба №3 "Задача о простых множителях"
На вход дается одно число х, нужно вывести все числа от 1 до х, удовлетворяющие условию: 3^K*5^L*7^M = x
где K, L, M - натуральные числа или могут быть равны 0.*/

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool simple(int number){
    while (number != 1){
        if (number % 3 == 0){number /= 3;}
        else if (number % 5 == 0){number /=5;}
        else if (number % 7 == 0){number /=7;}
        else {return false;}
    }
    return true;
}

int main(){
    int x;
    
    cout<< "Введите число: " <<endl;
    cin>> x;
    for (int i = 1; i < x; i++){
        if (simple(i)){cout << i << endl;}
    }

}