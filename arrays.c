/**
 * Arrays in C: Manipulting arrays
 * Insert the value: 99, 63, 71, and 83 to the index 1, 2, 3  and 4 respectively
 * Using any loop control structure, display result seperated by one tab
 * Return: 0 upon success else -1 with error message
 */
#include <stdio.h>

int main() {
	int myNumbers[] = {99, 63, 71, 83};
	int i;

	for (i = 0; i < 4; i++) {
		printf("%d\t", myNumbers[i]);
	}
	return 0;
}