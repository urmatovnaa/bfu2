// Сортировка вставками

#include <cmath>
#include <iostream>

using namespace std;

int main() {
    const int k = 20;
    int numbers[k] = {53, 21, 41, 5, 6, 38, 70, 0, 90, -5, 6, 27, 789, 59, 2, 57, 29, 67, 14, 70};

    // int numbers[k];
    // for (int i = 0; i < k; i++) {
    //     std::cin >> numbers[i];
    // }

    for (int i = 1; i < k; i++){
        int number_now = numbers[i];
        int j = i - 1;
        while (j >= 0 and numbers[j] > number_now){
            numbers[j + 1] = numbers[j];
            j -= 1;
        }
        numbers[j + 1] = number_now;
    }
    for (int i = 0; i < k; i++){
        cout << numbers[i] << "  ";
    }
}