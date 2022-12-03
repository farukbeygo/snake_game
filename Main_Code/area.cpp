#include <iostream>

int main() {
    // Write C++ code here
    std::cout << "Your Bilkenter starts the its journey!!";
    // I am creating a 10x10 area for our bilkenter
    for (int i = 0; i<10; i++){
        std::cout << "\n";
        for (int j = 0; j<10; j++){
            std::cout << "*";
        }
    }
    
    return 0;
}