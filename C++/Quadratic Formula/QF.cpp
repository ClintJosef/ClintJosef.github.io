#include <iostream>

/*
Philsci computer science really went from 
"How to make a python function"
to
"Create a C++ program that implements the Quadratic Formula, in a week"
*/
using namespace std;

int main(){
    double a,b,c;
    double qf, x1, x2;
    double root; 
    string conclusion = "Y";
    
    while(conclusion == "Y"){
        cout<< "Please input a value for coefficient a:";
        cin>> a;
        cout<< "\nPlease input a value for coefficient b:";
        cin>> b;
        cout<< "\nPlease input a value for coefficient c: ";
        cin>>c;
        
        qf = b*b-4*a*c;
        for(double i = 0; i*i<=qf; i+=0.00001){root = i;}
        x1 = (-b + root)/(2*a);
        x2 = (-b - root)/(2*a);
        
        if(qf<0){
            cout<< "The quadratic equation has no real root. Thank you!";
        }else{
            switch(qf>0){
                case 0:
                    cout<< "The quadratic equation has one real root "
                        << "with multiplicity of two, namely " << x2
                        << ".Thank you!";
                    break;
                case 1:
                    cout<< "The quadratic equation has two distinct roots,"
                        << " namely " << x1 << " and " << x2
                        << ". Thank you!";
                    break;
            }
        }
        cout<< "\nWould you like to input another quadratic equation? Y/N: ";
        cin>> conclusion;
    }
    cout<< "Thank you! ";
    return 0;
}
