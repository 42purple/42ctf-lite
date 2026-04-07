#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char buffer[60];
	
	printf("Enter password...");
	scanf("%60s", buffer);
	
	int x = strncmp("too_easy", buffer, 8);
	int y = strncmp("_4_me", buffer + 8, 6);
	
	if (!x && !y) {
		printf("Correct!\n");
		exit(0);
	} else {
		printf("?\n");
	}
	exit(1);
}

