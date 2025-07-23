#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


// Reads student names into a vector until "end" is entered,
// then displays the alphabetical first and last names
// and the total number of students.


int main() {

	// Vector to hold all student names entered by the user
	std::vector<std::string> students;

	// Program title
	std::cout << "Front and Back" << std::endl;

	// Continuously prompt for student names
	while (true) {

		std::string studentName;

		// Prompt and read full line (supports spaces in names)
		std::cout << "\nEnter a student, press 'end' to quit: ";
		std::getline(std::cin, studentName);

		// Stores valid input and stops input when user types "end"
		if (studentName != "end") {
			students.push_back(studentName);
		}
		else {
			break;
		}

	}

	// Sort names in ascending alphabetical order
	std::sort(students.begin(), students.end());

	// Output results heading
	std::cout << "\nResults: " << std::endl;

	// Display the first name in sorted list
	std::cout << "\nFirst in line: ";
	std::cout << students.front();
	
	// Display the last name in sorted list
	std::cout << "\n\nLast in line: ";
	std::cout << students.back();

	// Display total count of names entered
	std::cout << "\n\nNumber of students:  ";
	std::cout << students.size() << std::endl;

	// Closing statement
	std::cout << "\nEnd of Results." << std::endl;

	return 0;
}
