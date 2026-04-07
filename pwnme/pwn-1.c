#include <stdio.h>
#include <unistd.h>

int main() {
	int flag = 0;
	char buffer[40];
	
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
	printf("Enter the key...\n");
	read(0, buffer, 200);	
	if (flag != 0) {
		printf("Congrats! Here is your flag: 737461636b6a756d706572");
		return 0;
	}
	printf("...wrong\n");
	return 1;
}