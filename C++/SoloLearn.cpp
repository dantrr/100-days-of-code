#include <iostream>
using namespace std; 
//you dont have to declare this namespace, as you can call std before each command such as std::cout
int main(){
    cout << "Hello World" << endl; // endl starts a new line, character out does not make a new line by default
    cout << "This is awesome"; // you can also use \n to start a new line, but it should be INSIDE the str.
    int score = 0; // unlike python, varaible types need to be declared
    int a = 12;
    int b = 30;
    int sum = a + b;
    cout << sum;
    return 0; // i dunno what this is for, but solo learn uses at the end of each program
}
// auto automatically detects variable type. example // auto a = 12

/* multi line comments are
made
with 
these
*/
// cin >> asks for user input to take in data
