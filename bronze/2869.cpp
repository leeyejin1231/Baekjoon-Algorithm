#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b, v, day = 0;
    cin >> a >> b >> v;
    while(v>0){
        day++;
        v -= a;
        if(v==0 || v <0) break;
        v += b;
    }
    cout << day;
}