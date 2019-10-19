````C
#include<stdio.h>
#include<string.h>
int main(void){
	char S1[5000] = {0};
	char S2[5000] = {0};
	printf( "1nd Enter:");
	scanf("%s",&S1);
	printf( "2nd Enter:");
	scanf("%s",&S2);
	int  A[5000] = {0};
	int  B[5000] = {0};
	int min,i,j,cur;
	int sum = 0;
	for(i = 0;i < strlen(S1);i++){
		for(j = 0;S2[j] != '\0';j++){
			if(S1[i] == S2[j]){
				if(j >= i){
					A[j-i]++;	
				}else{
					B[i-j]++;
				}
			}			
		}
	} 
	min = strlen(S1) >= strlen(S2) ? strlen(S2): strlen(S1);
	for(i = 0; i < min; i++){
		printf("\n%d\n",A[i]);
		sum += (A[i]*(A[i]-1))/2;
	}
	for(i = 0; i < min; i++){
		printf("\nB: %d\n",B[i]);
		sum += (B[i]*(B[i]-1))/2;
	}
	printf("OUTPUT\n%d\n",sum);
	return 0;
}
````
