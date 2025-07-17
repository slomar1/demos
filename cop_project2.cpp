#include <iostream>
#include <iomanip>
using namespace std;


// Hi
// This is a basic restaurant menu thing



int main() {

	// Declaring variables as decimals
	double food;
	double tip;
	double tax;


	// Heading
	cout << "Restaurant Calculator\n\n";
	cout << "Enter the food charge: $";
	
	// Setting max decimal points to 2 and promting user input with terminal
	cout << fixed << setprecision(2);
	cin >> food;
	cout << "\n";

	// Calculations
	cout << "Totaling...\n\n";

	cout << "Food    :$" << food << endl;

	tip = food * 0.15;
	cout << "15% tip :$" << tip << endl;

	tax = food * 0.07;
	cout << "7% tax  :$" << tax << "\n\n";

	// Final Result
	cout << "Grand total: $" << food + tip + tax << "\n\n";

	cout << "End of results" << "\n\n";


	return 0;
}
