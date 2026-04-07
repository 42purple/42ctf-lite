#include <stdio.h>
#include <unistd.h>

void vuln() {
	char buffer[250];
	printf("Enter the key...\n");
	read(0, buffer, 300);
	printf("...wrong\n");
}

int main() {
	vuln();
	return 1;
}