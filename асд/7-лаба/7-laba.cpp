// Сортировка Шелла

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

    for (int index = 0; index < k - 1; index++) {
        int min_index = index;

        for (int i = index + 1; i < k; i++){
            if (numbers[min_index] > numbers[i]){
                min_index = i;
            }
        }
        if (index != min_index){
            int number = numbers[min_index];
            numbers[min_index] = numbers[index];
            numbers[index] = number;
        }
    }
    for (int i = 0; i < k; i++){
        cout << numbers[i] << "  ";
    }
}