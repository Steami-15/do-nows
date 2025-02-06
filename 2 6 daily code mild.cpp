#include <iostream>
using namespace std;

float CylinderVolume(int height,int radius);
bool isVowel(char a);
void CoinToss();
int main() {
cout << CylinderVolume(3, 4) << endl;
cout << isVowel('a') << endl;
CoinToss();
}

float CylinderVolume(int height, int radius) {
return 3.14 * (radius * radius) * height;
}

bool isVowel(char a) {
if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') {
return true;
}
else
return false;
}

void CoinToss() {
srand(time(NULL));
int num = rand() % 100;
if (num < 50)
cout << "heads" << endl;
else
cout << "tails" << endl;
cout << num;
}
