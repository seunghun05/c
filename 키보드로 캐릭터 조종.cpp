#include <stdio.h>
#include <windows.h>

    enum COLOR {BLACK=0,B,G,BG,R,P,Y,W};
    
    
	void chColor(int n)
	{
		SetConsoleTextAttribute( GetStdHandle(STD_OUTPUT_HANDLE), n);
	}
	
	int main()
	{
		chColor(Y);
		printf("hello\n");
		
		chColor(P);
		printf("c programming\n");
		
		return 0;
	}
