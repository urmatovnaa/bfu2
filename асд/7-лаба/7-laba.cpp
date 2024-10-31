// Сортировка Шелла nlogn,n^2

#include <cmath>
#include <iostream>

using namespace std;

int main() {
    const int k = 20;
    int numbers[k] = {53, 21, 41, 5, 6, 38, 70, 0, 90, -5, 6, 27, 789, 59, 2, 57, 29, 67, 14, 70};

    for (int step = k / 2; step > 0; step /= 2){
        for (int i = step; i < k; i++){
            int number_now = numbers[i];    
            int j = i;

            while (j >= step and numbers[j - step] > number_now) {
                numbers[j] = numbers[j - step];
                j -= step;
            }
            numbers[j] = number_now;
        }
    }
    for (int i = 0; i < k; i++){
        cout << numbers[i] << "  ";
    }
}