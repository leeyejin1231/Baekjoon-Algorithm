#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int a, b, c;
    cin >> a >> b >> c;
    if(b >= c){
        cout << -1;
    } else{
        cout << a/(c-b)+1;
    }
}