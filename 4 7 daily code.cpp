#include<iostream>
#include<Windows.h>
using namespace std;




int main() {
	int sigma;
	cout << "what grade are you in?" << endl;
	cin >> sigma;

	if (sigma < 5) {
		cout << "enjoy elementary school!" << endl;
	}
	else if (sigma < 8) {
		cout << "have fun in middle school" << endl;
	}
	else if (sigma <= 12) {
		cout << "prepare well in highschool" << endl;
	}
	else
		cout << "not an option" << endl;

}

------------------------------------------------------

#include<iostream>
#include<Windows.h>
using namespace std;




int main() {
	int sigma;
	cout << "give me a number from 10 to 100" << endl;
	cin >> sigma;

	for (int i = 10; i <= sigma; i += 2)
		cout << i << endl;
}

------------------------------------------------------


#include<iostream>
#include<Windows.h>
using namespace std;

void MiniCalc(int x, int y);


int main() {
	int x;
	int y;
	cout << "CALCULATOR: " << endl;
	cin >> x;
	cin >> y;
	MiniCalc(x, y);

}

void MiniCalc(int x, int y) {
	char op;
	cout << "now choose an operator (+, -, x, /)" << endl;
	cin >> op;

	if (op == '-') {
		cout << "result: " << x - y << endl;
	}
	else if (op == '+') {
		cout << "result: " << x + y << endl;
	}
	else if (op == 'x') {
		cout << "result: " << x * y << endl;
	}
	else if (op == '/') {
		cout << "result: " << x / y << endl;
	}
	else
		cout << "thats not an option" << endl;

}
