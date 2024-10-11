// Сортировка расческой

#include <cmath>
#include <iostream>

using namespace std;

int main() {
    int k = 20;
    int numbers[k] = {53, 21, 41, 5, 6, 38, 70, 0, 90, -5, 6, 27, 789, 59, 2, 57, 29, 67, 14, 70};

    // int numbers[k];
    // for (int i = 0; i < k; i++) {
    //     std::cin >> numbers[i];
    // }
    int gap = k / 1.247 - 1;
    while (gap >= 1){
        for (int i = gap; i < k; i++){
            if (numbers[i - gap] > numbers[i]){
                int number = numbers[i - gap];
                numbers[i - gap] = numbers[i];
                numbers[i] = number;
            }
        }
        gap = (gap + 1) / 1.247 - 1;
    }
    for (int i = 0; i < k; i++){
        cout << numbers[i] << "  ";
    }
}