#include <iostream>
using namespace std;


// This program prompts the user for two integers, validates that the ending value
// is greater than or equal to the starting value, then outputs incrementing values by 5.

int main() {

	int userInt1;
	int userInt2;

	// Display program header
	cout << "Increment by 5\n\n";

	// Prompt user for input
	cout << "\nEnter the beginning value: ";
	cin >> userInt1;
	cout << "Enter the ending value: ";
	cin >> userInt2;

	// While loop for input validation
	while (userInt1 > userInt2) {

		cout << "\nThe ending value cannot be less than the beginning value. Try again." << endl;

		cout << "\nPlease input the value of your first integer: ";
		cin >> userInt1;
		cout << "Please input the value of your second integer: ";
		cin >> userInt2;

	}

	cout << "\nResults: ";

	// While loop to output final results
	while (userInt1 <= userInt2) {

		cout << userInt1 << " ";

		userInt1 = userInt1 + 5;
	}

	cout << "\n\nEnd of Results." << endl;


	return 0;
}
