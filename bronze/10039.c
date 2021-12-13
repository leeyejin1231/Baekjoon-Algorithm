#include <stdio.h>

int main(void){
    int sum = 0;
    int score[5];
    for(int i=0; i<5; i++) scanf("%d", &score[i]);
    for(int i=0; i<5; i++){
        if(score[i] < 40) sum += 40;
        else sum += score[i];
    }
    printf("%d", sum/5);
}