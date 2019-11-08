#include "sort.h"

void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void mysort(int* tab, int size){
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size - 1; j++){
            if(tab[j] > tab[j+1]){
                swap(tab + j, tab + j + 1);
            }
        }
    }
}
