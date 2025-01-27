#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

const int MAX_INCORRECT = 6;
char incorrect[MAX_INCORRECT];
int numIncorrect = 0;
int misses = 0;

void displayHangman() {
	cout << "\n";
	switch (misses) {
	case 0:
		cout << " +---+\n";
		cout << " |   |\n";
		cout << "     |\n";
		cout << "     |\n";
		cout << "     |\n";
		cout << "     |\n";
		cout << "--------\n";
		break;
	case 1:
		cout << " +---+\n";
		cout << " |   |\n";
		cout << " O   |\n";
		cout << "     |\n";
		cout << "     |\n";
		cout << "     |\n";
		cout << "--------\n";
		break;
	case 2:
		cout << " +---+\n";
		cout << " |   |\n";
		cout << " O   |\n";
		cout << " |   |\n";
		cout << "     |\n";
		cout << "     |\n";
		cout << "--------\n";
		break;
	case 3:
		cout << " +---+\n";
		cout << " |   |\n";
		cout << " O   |\n";
		cout << " |   |\n";
		cout << " |   |\n";
		cout << "     |\n";
		cout << "--------\n";
		break;
	case 4:
		cout << " +---+\n";
		cout << " |   |\n";
		cout << " O   |\n";
		cout << "/|\\  |\n";
		cout << " |   |\n";
		cout << "     |\n";
		cout << "--------\n";
		break;
	case 5:
		cout << " +---+\n";
		cout << " |   |\n";
		cout << " O   |\n";
		cout << "/|\\  |\n";
		cout << " |   |\n";
		cout << "/ \\  |\n";
		cout << "--------\n";
		break;
	}
}

void display(string guessedWord) {
	cout << "\n word: ";
	for (int i = 0; i < guessedWord.length(); i++) {
		cout << guessedWord[i] << ' ';
	}
	cout << "\n incorrect guesses: ";
	for (int i = 0; i < numIncorrect; i++) {
		cout << incorrect[i] << ' ';
	}
	cout << "\n misses left: " << MAX_INCORRECT - misses << "\n";
	displayHangman();
}

string processGuess(char guess, string word, string guessedWord) {
	bool isCorrect = false;
	for (int i = 0; i < word.length(); i++) {
		//cout << "checking " << word[i] << " against " << guess << " and guessedWord is " << guessedWord[i] << endl;
		if (word[i] == guess && guessedWord[i] == '_') {
			guessedWord[i] = guess;
			isCorrect = true;
			//cout << "setting isCorrect to true..." << endl;
		}
	}

	if (!isCorrect) {
		bool alreadyGuessed = false;


		for (int i = 0; i < numIncorrect; i++) {
			if (incorrect[i] == guess) {
				alreadyGuessed = true;
				break;
			}
		}

		if (!alreadyGuessed) {
			incorrect[numIncorrect++] = guess;
			misses += 1;
		}
	}
	return guessedWord;
}

int main() {
	string wordList[] = { "toilet", "ihatecoding", "trash", "skibidi", "sigma", "kitty", "dog", "lizard" };
	srand(time(0));
	string word = wordList[rand() % 8];  // Fixing the random word selection
	string guessedWord(word.length(), '_');  // Start with all spaces instead of underscores
	cout << "welcome to hangman\n";

	while (misses < MAX_INCORRECT && guessedWord != word) {
		display(guessedWord);
		cout << "enter your guess: ";
		char guess;
		cin >> guess;

		string oldGuessedWord = guessedWord;
		guessedWord = processGuess(guess, word, guessedWord);

		if (guessedWord == oldGuessedWord) {
			cout << "that letter isn't in the word\n";
		}
		else {
			cout << "good guess\n";
		}
	}

	if (guessedWord == word) {
		cout << "you guessed the word: " << word << "\n";
	}
	else {
		cout << "the word was: " << word << "\n";
	}

	return 0;
}
