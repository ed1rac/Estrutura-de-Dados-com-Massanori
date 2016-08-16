#include <stdio.h>
#include <stdlib.h>

//Programa Trasformar em numero binário usando uma pilha

int main(){
	int n = 18;
	int t = 0;
	int p[32];
	while (n!=0){
		p[t++] = n%2;
		x = p[t];
		n /= 2;
	}
	while (t!=0){
		printf("%d", p[--t]);
	}
	system("pause");
}
