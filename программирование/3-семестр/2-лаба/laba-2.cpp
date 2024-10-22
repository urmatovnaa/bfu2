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

class Point
{
public:
    double x;
    double y;
    Point(){}
    Point(double m_x, double m_y) : x(m_x), y(m_y) {}
};

Result find_M(double E) 
{
    double R = 0;
    double L = 0;
    while (true){
        if (f(L) < 0 and f(R) > 0){break;}
        else if (f(L) > 0 and f(R) < 0){break;}
        R += 0.5;
        L -= 0.5;
    }
    int k = 0;
    Point A(L, f(L));  
    Point B(R, f(R));
    double M_x = ((-1 * A.y) * (B.x- A.x))/(B.y - A.y) + A.x;
    Point M(M_x, 0); 
    while (abs(f(M.x)) - E > 0){
        k++;
        if (f(L) > 0){
            if (f(M.x) > 0){L = M.x;}
            else {R = M.x;}
        }
        if (f(L) < 0){
            if (f(M.x) < 0){L = M.x;}
            else {R = M.x;}
        }

        Point A(L, f(L));  
        Point B(R, f(R));
        M_x = ((-1 * A.y) * (B.x- A.x))/(B.y - A.y) + A.x;
        M.x = M_x;
    }
    Result res1;
    res1.setM(M.x);
    res1.setK(k);
    res1.setEp(abs(f(M.x)));
    return res1;
}


int main(){
    Result fin = find_M(0.1);
    cout << fin << endl;
}