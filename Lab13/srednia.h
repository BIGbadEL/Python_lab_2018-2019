
#include "sort.h"
double srednia(int* tab, int size){
    double result = 0.0;
    for(int i = 0; i < size; i++){
        result += tab[i];
    }

    return result / size;
}

int mediand(int* tab, int size){
    mysort(tab, size);
    return tab[size / 2];
}