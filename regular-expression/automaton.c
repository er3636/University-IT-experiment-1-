#include <stdio.h>
#define S0 0 /*状態0 の定義*/
#define S1 1 /*状態1 の定義*/
#define S2 2 /*状態2 の定義*/
#define S3 3 /*状態3 の定義*/

int main(){
	int i=0;
	int State=S0;
	char str[256];
	scanf("%s", str);
	while(str[i] != '¥0'){
		switch(State){
			case S0: // 状態 0 の動作
				if(str[i] == '0') State = S0; //現在の文字が0 なら状態0 のまま
				if(str[i] == '1') State = S1; //現在の文字が1 なら状態1 への移動
				break;
			case S1:
				if(str[i] == '0') State = S2; //現在の文字が0 なら状態2 への移動
				if(str[i] == '1') State = S1; //現在の文字が1 なら状態1 のまま
				break;
			case S2:
				if(str[i] == '0') State = S0; //現在の文字が0 なら状態2 のまま
				if(str[i] == '1') State = S3; //現在の文字が1 なら状態3 への移動
				break;
			case S3:
				if(str[i] == '0') State = S3; //現在の文字が0 なら状態3 のまま
				if(str[i] == '1') State = S3; //現在の文字が1 なら状態3 のまま
				break;
		}
		i++;
	}
	if(State == S3) printf("accept¥n"); //最終状態が状態3 ならば受理する
	else printf("reject¥n"); //最終状態が状態3 じゃなければ受理しない
	return 0;
}