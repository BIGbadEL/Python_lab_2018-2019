
int mynwd(int a, int b){
    if(b == 0){
        return a;
    } else {
       return mynwd(b, a % b);
    }
}