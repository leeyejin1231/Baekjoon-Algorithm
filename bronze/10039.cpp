#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int sum = 0;
    int score[5];
    for(int i=0; i<5; i++) cin >> score[i];
    for(int i=0; i<5; i++){
        if(score[i]<40) sum += 40;
        else sum += score[i];
    }
    cout << sum/5;
}