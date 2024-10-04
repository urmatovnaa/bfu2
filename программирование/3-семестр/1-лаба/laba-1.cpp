#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double f(double x) {
return 0.8*(x + 2) - 3*cos(0.7*x) + 2;
// return sqrt(sin(x+1)*sin(x+1)) - x + 1;
}

class Result
{
private:
    int m_k = 0;   //количество итераций
    double m_M;
    double m_Ep;  
public:
    // 1. Конструктор по умолчанию
    Result(){}

    // 4. Деструктор
    ~Result() 
    {
        cout << "Class deleted"  << endl;
    }

    void setK(int k){m_k = k;}
    void setM(double M){m_M = M;}
    void setEp(double Ep){m_Ep = Ep;}

    friend ostream& operator<<(ostream& out, const Result& c) 
    {
        out << "{M = "<< c.m_M << "; k = " << c.m_k << "; Ep = " << c.m_Ep << "}";
        return out;
    }

};

Result find_x(double E) 
{
    double R = -10;
    double L = -10;
    if (f(L) < 0){
        while (f(R) < 0){ R += 0.5;}
    }
    else if (f(L) > 0){
        while (f(R) > 0){ R += 0.5;}
    }
    int k = 0;
    double M = (R + L)/2; 
    while (abs(f(M)) - E > 0){
        if (f(L) > 0){
            if (f(M) > 0){L = M;}
            else {R = M;}
        }
        if (f(L) < 0){
            if (f(M) < 0){L = M;}
            else {R = M;}
        }
        M = (R + L)/2;
        k++;
        }
    Result res1;
    res1.setM(M);
    res1.setK(k);
    res1.setEp(abs(f(M)));
    return res1;
}


int main(){
    Result fin = find_x(1);
    cout << fin << endl;
}