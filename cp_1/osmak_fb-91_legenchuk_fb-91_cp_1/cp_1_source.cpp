// ******** Settings ********
constexpr auto FILEPATH = "Holmes.txt"; // Входной файл
constexpr auto H1 = "h1.csv";
constexpr auto H1_SPC = "h1_spc.csv";
constexpr auto H2 = "h2.csv";
constexpr auto H2_SPC = "h2_spc.csv";
constexpr auto H2_STP = "h2_stp.csv";
constexpr auto H2_SPC_STP = "h2_stp_spc.csv";

constexpr auto CONSOLE = true; // Вывод на консоль (true - выводить, false - не выводить)
// ******** ******** ********




// Standard
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <iomanip>

// Windows header
#include <windows.h>

template <typename T>
void measureEntropy(std::unordered_map<T, int> freq, int rang, unsigned int count, const std::string& save) {
	std::vector<std::pair<T, int>> table;
	table.reserve(freq.size());
	for (const auto& f : freq)
		table.emplace_back(f);

	std::sort(table.begin(), table.end(), [](const auto& lhs, const auto& rhs) {
		return std::tuple(lhs.second, rhs.first) > std::tuple(rhs.second, lhs.first);
		});

	std::fstream out(save, std::fstream::out | std::fstream::trunc);

	if (CONSOLE) std::cout << "Буква;Повторения;Частота" << std::endl;
	out << "Буква;Повторения;Частота" << std::endl;

	double ent = 0;
	for (const auto& [l, c] : table) {
		// f - частота
		double f = static_cast<double>(c) / count;
		// Формула ентропии -СУМ( p(i) * log2 p(i) ) где p (i) частота встречи конкретной буквы
		ent += f * log2(f);

		if (CONSOLE) std::cout << l << ';' << c << ';' << std::setprecision(12) << f << std::endl;
		out << l << ';' << c << ';' << std::setprecision(5) << f << std::endl;
	}

	ent /= -rang;

	if (CONSOLE) std::cout << "Энтропия: " << ent << std::endl;
	out << "Энтропия: " << ent << std::endl;
}


const std::vector<char> a1{ '_', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я' };
const std::vector<char> a2{ 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я' };

void buildTable(std::unordered_map<std::string, int> freq, unsigned int count, std::vector<char> alphabet, const std::string& save) {
	std::fstream out("table_" + save, std::fstream::out | std::fstream::trunc);

	for (const auto& i : alphabet)
		out << ";" << i;
	out << std::endl;

	for (const auto& i : alphabet) {
		out << i;
		for (const auto& j : alphabet) {
			std::string bigram;
			bigram += (i == ' ' ? '_' : i);
			bigram += (j == ' ' ? '_' : j);

			const auto c = freq[bigram];
			if (c == 0)
				out << ";-";
			else
				out << ";" << std::setprecision(5) << static_cast<double>(c) / count;
		}

		out << std::endl;
	}
}

int main() {
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);

	const auto& toUpper = [](const char ch) -> char {
		int code = static_cast<int>(ch);
		
		if (code == -72)
			return static_cast<char>(-88);

		return (code > -33 && code <= 0) ? static_cast<char>(code - 32) : ch;
	};

	const auto& isLetter = [](const char ch) -> bool {
		return ch > -65 && ch < -32 || ch == -88;
	};

	std::ifstream in(FILEPATH);

	if (!in.is_open()) {
		std::cout << "Не удалось открыть файл... " << FILEPATH;
		return 0;
	}

	// Считываем буквы с файла в вектор
	std::vector<char> letters;
	std::vector<char> letters_no_space;
	char letter;

	char prevCh = ' ';
	while (in.get(letter)) {
		char ch = (letter != '\n' ? toUpper(letter) : ' ');

		if (!isLetter(ch) && ch != ' ')
			continue;

		if (prevCh == ' ' && ch == ' ')
			continue;

		letters.push_back(ch);
		prevCh = ch;
	}

	// Заменяем букву <Ё> и <Ъ> на <Е> <Ь> соотвественно
	std::transform(letters.begin(), letters.end(), letters.begin(),
		[&toUpper](const char ch) -> char {
			if (toUpper(ch) == 'Ё') return 'Е';
			if (toUpper(ch) == 'Ъ') return 'Ь';

			return ch;
		});

	std::copy_if(letters.begin(), letters.end(), std::back_inserter(letters_no_space), [](const char ch) {
		return ch != ' ';
	});

	{
		// БУКВЫ (H1) - С ПРОБЕЛАМИ
		std::unordered_map<char, int> freq;
		unsigned int count = 0;

		for (const auto& ch : letters) {
			freq[ch == ' ' ? '_' : ch] += 1;
			count += 1;
		}

		measureEntropy(freq, 1, count, H1_SPC);
	}

	{
		// БУКВЫ (H1) - БЕЗ ПРОБЕЛОВ
		std::unordered_map<char, int> freq;
		unsigned int count = 0;

		for (const auto& ch : letters_no_space) {

			freq[ch] += 1;
			count += 1;
		}

		measureEntropy(freq, 1, count, H1);
	}

	{
		// БУКВЫ (H2) - C ПРОБЕЛАМИ
		std::unordered_map<std::string, int> freq;
		unsigned int count = 0;


		for (auto i = 0; i < letters.size() - 1; ++i) {
			char first  = letters[i];
			char second = letters[i + 1];

			std::string bigram;
			bigram += (first  == ' ' ? '_'  : first);
			bigram += (second == ' ' ? '_' : second);

			freq[bigram] += 1;
			count += 1;
		}

		measureEntropy(freq, 2, count, H2_SPC);
		buildTable(freq, count, a1, H2_SPC);
	}

	{
		// БУКВЫ (H2) - БЕЗ ПРОБЕЛОВ
		std::unordered_map<std::string, int> freq;
		unsigned int count = 0;

		for (auto i = 0; i < letters_no_space.size() - 1; ++i) {
			std::string bigram;
			bigram += letters_no_space[i];
			bigram += letters_no_space[i + 1];

			freq[bigram] += 1;
			count += 1;
		}

		measureEntropy(freq, 2, count, H2);
		buildTable(freq, count, a2, H2);
	}

	{
		// БУКВЫ (H2) - C ПРОБЕЛАМИ С ШАГОМ
		std::unordered_map<std::string, int> freq;
		unsigned int count = 0;


		for (auto i = 0; i < letters.size() - 2; i += 2) {
			char first  = letters[i];
			char second = letters[i + 1];

			std::string bigram;
			bigram += (first  == ' ' ? '_' : first);
			bigram += (second == ' ' ? '_' : second);

			freq[bigram] += 1;
			count += 1;
		}

		measureEntropy(freq, 2, count, H2_SPC_STP);
		buildTable(freq, count, a1, H2_SPC_STP);
	}

	{
		// БУКВЫ (H2) - БЕЗ ПРОБЕЛОВ С ШАГОМ
		std::unordered_map<std::string, int> freq;
		unsigned int count = 0;

		for (auto i = 0; i < letters_no_space.size() - 2; i += 2) {
			std::string bigram;
			bigram += letters_no_space[i];
			bigram += letters_no_space[i + 1];

			freq[bigram] += 1;
			count += 1;
		}

		measureEntropy(freq, 2, count, H2_STP);
		buildTable(freq, count, a2, H2_STP);
	}

	return 0;
}