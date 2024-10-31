#include <iostream>
#include <string>

using namespace std;


struct Element {
    string data;
    Element* next = nullptr;
    Element(const string& d) : data(d) {}
};

class Queue {
private:
    Element* first = nullptr;

public:
    Queue() {}

    Queue(const Queue& other) : first(other.first) {}

    // 3. Оператор присваивания копированием
    Queue& operator=(const Queue& other) 
    {
        first = other.first;
        return *this;
    }

    // Добавление элемента в конец списка
    void append(const string& data) {
        Element* newEl = new Element(data);
        if (first == nullptr) {first = newEl;}
        else{
            Element* current = first;
            while (current) {
                if (current->next){
                    current = current->next;
                }
                else {
                    current->next = newEl;
                    break;
                }
            }
        }
    }

    // извлечение первого элемента
    string get_first() {
        if (first == nullptr) return "";
        Element* old = first;
        string first_element = first->data;
        first = first->next;
        delete old;
        return first_element;
    }

    // Просмотр первого элемента
    void print_first() {
        cout << first << endl;
    }

    // Поиск элемента t/f
    bool search(const string& data) {
        Element* current = first;
        while (current) {
            if (current->data == data) return true;
            current = current->next;
        }
        return false;
    }

    // Вычисление веса элемента (номер в очереди или -1)
    int get_position(const string& data) {
        Element* current = first;
        int position = 1;
        while (current) {
            if (current->data == data) return position;
            position++;
            current = current->next;
        }
        return -1;
    }

    // Операция + для последовательного соединения двух очередей
    Queue operator+(Queue& other) {
        Queue result;
        Element* current = first;
        while (current) {
            result.append(current->data);
            current = current->next;
        }
        current = other.first;
        while (current) {
            result.append(current->data);
            current = current->next;
        }
        return result;
    }

    // Операция * для перекрестного соединения с преобладанием первой очереди
    Queue operator*(Queue& other) {
        Queue result;
        Element* currentA = first;
        Element* currentB = other.first;
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
        return result;
    }

    // Унарный оператор - для разворота очереди
    Queue operator-() {
        Queue result;
        Element* current = first;
        while (current) {
            Element* newEl = new Element(current->data);
            newEl->next = result.first;
            result.first = newEl;
            current = current->next;
        }
        return result;
    }

    // Удаление элемента a
    void DolgoZdat(const std::string& a) {
        if (first == nullptr) return;
        if (first->data == a) {
            get_first();
            return;
        }
        Element* current = first;
        while (current->next) {
            if (current->next->data == a) {
                Element* todel = current->next;
                current->next = current->next->next;
                delete todel;
                break;
            }
            current = current->next;
        }
    }

    // Вывод элементов очереди
    void print() const {
        Element* current = first;
        while (current) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }

    ~Queue() {
        while (first) {
            Element* temp = first;
            first = first->next;
            delete temp;
        }
    }
};


int main() {
    Queue A;
    A.append("a1");
    A.append("a2");
    A.append("a3");
    A.append("a4");
    A.print();

    A.DolgoZdat("a3");
    A.print();

    Queue B = -A; 
    B.print();

    Queue C = A + B;
    C.print();
    
    cout << C.get_first() << endl;
    C.print();

    cout << C.search("a1") << endl;
    cout << C.get_position("a2") << endl;

    B.get_first();
    B.get_first();
    cout << "__________________" << endl;
    A.print();
    cout << "))))))))))))))))))))))))))" << endl;
    B.print();
    Queue D = A * B;
    D.print();

    return 0;
}

