#include <iostream>
#include <string>

using namespace std;

struct Element {
    string data;
    Element* next = nullptr;
    Element* prev = nullptr;

    Element(const string& d) : data(d) {}

    ~Element(){
        next = nullptr;
        prev = nullptr;
    }
};

class Stack {
private:
    Element* top = nullptr;

public:
    Stack() {}

    // конструктор копиравания
    Stack(const Stack& other) {
        Element* current = other.top;
        while (current->next) {
            current = current->next;
        }
        while (current) {
            append(current->data);
            current = current->prev;
        }
    }
    // оператор присваивания
    Stack operator=(const Stack& other) { 
        Stack result;
        Element* current = top;
        while (current->next) {
            current = current->next;
        }
        while (current) {
            result.append(current->data);
            current = current->prev;
        }
        return result;
    }

    // Добавление элемента в вершину стека
    void append(const string& data) {
        Element* newEl = new Element(data);
        if (top != nullptr) {
            newEl->next = top;
            top->prev = newEl;
        }
        top = newEl;
    }

    // Извлечение элемента с вершины стека
    string pop() {
        if (top == nullptr) return "";
        Element* old_top = top;
        string top_data = top->data;
        top = top->next;
        if (top != nullptr) {
            top->prev = nullptr;
        }
        delete old_top;
        return top_data;
    }
    // Просмотр элемента с вершины стека
    void get_top(){
        if (top){
            cout << top << endl;
        }
    } 

    // Поиск элемента (возвращает true/false)
    bool search(const string& data) {
        Element* current = top;
        while (current) {
            if (current->data == data){
                return true;
            }
            current = current->next;
        }
        return false;
    }

    //Вычисление веса элемента а (номер в стек если есть либо -1)
    int get_position(const string& data) {
        Element* current = top;
        int position = 1;
        while (current) {
            if (current->data == data) return position;
            position++;
            current = current->next;
        }
        return -1;
    }

    // Глубина стека (количество элементов)
    int size(){
        Element* current = top;
        int count = 0;
        while (current) {
            count++;
            current = current->next;
        }
        return count;
    }

    // Вывод элементов стека
    void print(){
        Element* current = top;
        while (current) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }

    // Операция + для последовательного соединения 2 стеков
    Stack operator+(Stack& other) {
        Stack result = (*this);
        Stack temp = -other;
        Element* current = temp.top;
        while (current) {
            result.append(current->data);
            current = current->next;
        }
        return result;
    }

    // Операция * для перекрестного соединения с преобладанием первого стека
    Stack operator*(Stack& other) {
        Stack result;
        Stack temp1 = (*this);
        Stack temp2 = other;
        Element* currentA = temp1.top;
        Element* currentB = temp2.top;
        while (currentA or currentB) {
            if (currentA) {
                result.append(currentA->data);
                currentA = currentA->next;
            }
            if (currentB) {
                result.append(currentB->data);
                currentB = currentB->next;
            }
        }
        return -result;
    }

    // Унарный оператор - для разворота стека
    Stack operator-() {
        Stack result;
        Element* current = top;
        while (current) {
            result.append(current->data);
            current = current->next;
        }
        return result;
    }

    // Удаляет элемент с весом i
    void Dzenga(int i){
        Element* current = top;
        int position = 1;
        while (current) {
            if (position == i){
                if (i == 1){
                    pop();
                }
                else if (i == size()){
                    current->prev->next = nullptr;
                    delete current;
                }
                else {
                    current->prev->next = current->next;
                    current->next->prev = current->prev;
                    delete current;
                }
            };
            position++;
            current = current->next;
        }
    }

    ~Stack() {
        while (top) {
            Element* temp = top;
            top = top->next;
            if (top){
                top->prev = nullptr;
            }
            delete temp;
        }
    }
};

int main() {
    Stack A;
    A.append("a1");
    A.append("a2");
    A.append("a3");
    A.append("a4");
    A.print();

    cout << "Deleted: " << A.pop() << endl;
    A.print();

    cout << "Search for a2: " << A.search("a2") << endl;

    A.print();
    cout << "Position for a3: " << A.get_position("a3") << endl;
    cout << "Size: " << A.size() << endl;
    Stack B;
    B.append("b1");
    B.append("b2");
    B.append("b3");
    B.append("b4");
    B.print();
    Stack C = -B;
    C.print();
    C.pop();
    C.print();
    cout << "A - " << endl;
    A.print();
    cout << "B - " << endl;
    B.print();
    Stack D = A + B;
    cout << "A + B " << endl;
    D.print();
    Stack G = A * B;
    cout << "A * B " << endl;
    G.print();
    G.Dzenga(3);
    G.print();

    return 0;
}
