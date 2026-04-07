#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void fail() {
	printf("?\n");
}

void ok() {
	printf("Well done!\n");
}

int validate_input_2(char * input) {
	const char s[4] = {
		'e', '!', '!', '?'
	};
	
	for (int i = 0; i < 4; i++) {
		if (input[i] + i != s[i]) {
			return 0;
		}
	}
	return 1;
}

int validate_input(char * input) {
	const char t[5] = {
		'g', 'o', 't', '_', 'm'
	};
	int res = 0; 
	for (int i = 0; i < 9; i++) {
		if (input[i] + i != t[i]) {
			return 0;
		}
		if (i > 4) {
		res = validate_input_2(input + 5);
		break ;
		}
	}
	return res;
}

int main(int argc, char ** argv) {
	if (argc != 2){
	fail();
		exit(2);
		}
	if (strlen(argv[1]) == 0) {
		fail();
		exit(1);
	}
	if (strlen(argv[1]) != 9) {
		fail();
		exit(3);
	}
	if (validate_input(argv[1]) == 1) {
		fail();
		exit(1);
	}
	ok();
	exit(42);
}
