#include <iostream>
#include <clocale>
#include <fstream>
#include <cstring> 
#include <string>
#include <string.h>
#include <math.h>
using namespace std;

int gcd(int a, int b) {
    while (a and b) {
        if (a > b)
            a %= b;
        else
            b %= a;
    }
    return a + b;
}

void text_normalization(char character, int ANSI_CODE, string& text) {
    if (ANSI_CODE == -72 || ANSI_CODE == -88) {
        text.push_back('е');
    }
    else if (ANSI_CODE >= -64 && ANSI_CODE <= -1) {
        text.push_back(tolower(character));
    }
}

void zero_array(float(&bigram_array)[31][31]) {
    for (int i = 0; i <= 30; i++) {
        for (int j = 0; j <= 30; j++) {
            bigram_array[i][j] = 0.0;
        }
    }
}

void bigram_freq_count(string& text, int& i, int& first_bigram_position, int& second_bigram_posotion) {
    first_bigram_position = second_bigram_posotion;
    if (text[i] == 'а') {
        second_bigram_posotion = 0;
    }
    else if (text[i] == 'б') {
        second_bigram_posotion = 1;
    }
    else if (text[i] == 'в') {
        second_bigram_posotion = 2;
    }
    else if (text[i] == 'г') {
        second_bigram_posotion = 3;
    }
    else if (text[i] == 'д') {
        second_bigram_posotion = 4;
    }
    else if (text[i] == 'е') {
        second_bigram_posotion = 5;
    }
    else if (text[i] == 'ж') {
        second_bigram_posotion = 6;
    }
    else if (text[i] == 'з') {
        second_bigram_posotion = 7;
    }
    else if (text[i] == 'и') {
        second_bigram_posotion = 8;
    }
    else if (text[i] == 'й') {
        second_bigram_posotion = 9;
    }
    else if (text[i] == 'к') {
        second_bigram_posotion = 10;
    }
    else if (text[i] == 'л') {
        second_bigram_posotion = 11;
    }
    else if (text[i] == 'м') {
        second_bigram_posotion = 12;
    }
    else if (text[i] == 'н') {
        second_bigram_posotion = 13;
    }
    else if (text[i] == 'о') {
        second_bigram_posotion = 14;
    }
    else if (text[i] == 'п') {
        second_bigram_posotion = 15;
    }
    else if (text[i] == 'р') {
        second_bigram_posotion = 16;
    }
    else if (text[i] == 'с') {
        second_bigram_posotion = 17;
    }
    else if (text[i] == 'т') {
        second_bigram_posotion = 18;
    }
    else if (text[i] == 'у') {
        second_bigram_posotion = 19;
    }
    else if (text[i] == 'ф') {
        second_bigram_posotion = 20;
    }
    else if (text[i] == 'х') {
        second_bigram_posotion = 21;
    }
    else if (text[i] == 'ц') {
        second_bigram_posotion = 22;
    }
    else if (text[i] == 'ч') {
        second_bigram_posotion = 23;
    }
    else if (text[i] == 'ш') {
        second_bigram_posotion = 24;
    }
    else if (text[i] == 'щ') {
        second_bigram_posotion = 25;
    }
    else if (text[i] == 'ы') {
        second_bigram_posotion = 26;
    }
    else if (text[i] == 'ь') {
        second_bigram_posotion = 27;
    }
    else if (text[i] == 'э') {
        second_bigram_posotion = 28;
    }
    else if (text[i] == 'ю') {
        second_bigram_posotion = 29;
    }
    else if (text[i] == '€') {
        second_bigram_posotion = 30;
    }
}

void show_bigram_freq(float(&bigram_array)[31][31], float amount) {
    ofstream file;
    file.open("Frequency of bigrams in ET.txt");
    float sum = 0;
    for (int i = 0; i <= 30; i++) {
        for (int j = 0; j <= 30; j++) {
            file << bigram_array[i][j] / amount << "\t";
        }
        file << endl;
    }
    file.close();
}

int gcdExtended(int a, int b, int* x, int* y) {
    if (a == 0) {
        *x = 0, * y = 1;
        return b;
    }

    int x1, y1;
    int gcd = gcdExtended(b % a, a, &x1, &y1);

    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}

int modInverse(int a, int m) {
    int x, y;
    int g = gcdExtended(a, m, &x, &y);
    if (g != 1)
        return 0;
    else {
        int res = (x % m + m) % m;
        return res;
    }
}

int bigram_value_counter(string& bigram, string& alphabet) {
    int bigram_value = 0;
    for (int i = 0; i < alphabet.length(); i++) {
        if (bigram[0] == alphabet[i]) {
            bigram_value = alphabet.length() * i;
        }
        if (bigram[1] == alphabet[i]) {
            bigram_value += i;
        }
    }
    return bigram_value;
}

void take_by_module(int& to_take, int module_to_take) {
    if (to_take < 0) {
        while (to_take < 0)
            to_take += module_to_take;
    }
    else {
        to_take = to_take % module_to_take;
    }
}

void insert_parameters_into_array(int(&parameters_a_and_b)[1000][2], int& par_a, int a, int b) {
    bool flag = true;
    for (int i = 0; i < par_a; i++) {
        if (parameters_a_and_b[i][0] == a && parameters_a_and_b[i][1] == b)
            flag = false;
    }
    if (flag) {
        parameters_a_and_b[par_a][0] = a;
        parameters_a_and_b[par_a][1] = b;
        par_a++;
    }
}

void modular_equation(int y, int x, int(&parameters_a_and_b)[1000][2], int& par_a, int mod, int y1, int x1) {
    int a, b;
    take_by_module(y, 961);
    take_by_module(x, 961);
    int pre = gcd(x, 961);
    if (pre) {
        a = modInverse(x, 961);
        if (a != 0) {
            a = a * y;
            take_by_module(a, 961);
            b = y1 - a * x1;
            take_by_module(b, 961);
            insert_parameters_into_array(parameters_a_and_b, par_a, a, b);
        }
    }
    else {
        if (y % pre == 0) { //если решени€ не существует, то мы его игнорируем
            y = y / pre;
            x = x / pre;
            mod = mod / pre;
            while (mod <= 961) {
                a = modInverse(x, 961);
                if (a != 0) {
                    a = a * y;
                    take_by_module(a, 961);
                    b = y1 - a * x1;
                    take_by_module(b, 961);
                    insert_parameters_into_array(parameters_a_and_b, par_a, a, b);
                    y += 31;
                    x += 31;
                    mod += 31;
                }
            }
        }
    }
}

void decryption(string& bigram, string& alphabet, string& decrypted_text, int a, int b) {
    int first_letter = 0, second_letter = 0, first_decrypted_letter = 0, second_decrypted_letter = 0, x = 0, y = 0;
    for (int i = 0; i < alphabet.length(); i++) {
        if (bigram[0] == alphabet[i]) {
            first_letter = i;
        }
        if (bigram[1] == alphabet[i]) {
            second_letter = i;
        }
    }
    x = first_letter * alphabet.length() + second_letter;
    y = (x - b) * modInverse(a, alphabet.length() * alphabet.length());
    take_by_module(y, alphabet.length() * alphabet.length());
    second_decrypted_letter = y;
    take_by_module(second_decrypted_letter, alphabet.length());
    first_decrypted_letter = (y - second_decrypted_letter) / alphabet.length();
    decrypted_text.push_back(alphabet[first_decrypted_letter]);
    decrypted_text.push_back(alphabet[second_decrypted_letter]);
}

bool check_for_noice(string& alphabet, string& decrypted_text, int& first_bigram_position, int& second_bigram_posotion, float(&bigram_array)[31][31]) {
    int freq_array[31];
    for (int i = 0; i < 31; i++)
        freq_array[i] = 0;
    zero_array(bigram_array);

    for (int i = 0; i <= decrypted_text.length() - 1; i = i + 2)
    {
        bigram_freq_count(decrypted_text, i, first_bigram_position, second_bigram_posotion);

        i++;
        bigram_freq_count(decrypted_text, i, first_bigram_position, second_bigram_posotion);
        i--;

        bigram_array[first_bigram_position][second_bigram_posotion]++;
    }
    for (int i = 0; i < decrypted_text.length(); i++) {
        for (int j = 0; j < 31; j++) {
            if (alphabet[j] == decrypted_text[i]) {
                freq_array[j]++;
                j = 31;
            }
        }
    }
    for (int i = 0; i < 31; i++) {
        if (freq_array[14] < freq_array[i])
            return false;
    }
    for (int i = 0; i < 31; i++) {
        for (int j = 0; j < 31; j++) {
            if (bigram_array[17][18] < bigram_array[i][j])
                return false;
        }
    }
    return true;
}

int main() {
    setlocale(LC_ALL, "Russian");
    int parameters_a_and_b[1000][2];
    for (int i = 0; i < 1000; i++)
        for (int j = 0; j < 2; j++)
            parameters_a_and_b[i][j] = 0;
    int par_a = 0;

    string encrypted_text, decrypted_text;
    string alphabet = "абвгдежзийклмнопрстуфхцчшщьыэю€";
    int first_bigram_position = 0, second_bigram_posotion = 0, bigrams_amount = 0;
    char character;

    ifstream file1("Encrypted_text.txt");
    while (!file1.eof()) {
        file1.get(character);
        text_normalization(character, static_cast<int> (character), encrypted_text);
    }
    file1.close();

    float bigram_array[31][31];
    zero_array(bigram_array);
    for (int i = 0; i <= encrypted_text.length() - 1; i = i + 2)
    {
        bigram_freq_count(encrypted_text, i, first_bigram_position, second_bigram_posotion);

        i++;
        bigram_freq_count(encrypted_text, i, first_bigram_position, second_bigram_posotion);
        bigrams_amount++;
        i--;

        bigram_array[first_bigram_position][second_bigram_posotion]++;
    }

    show_bigram_freq(bigram_array, bigrams_amount);

    int first1 = 0, first2 = 0, second1 = 0, second2 = 0, third1 = 0, third2 = 0, fourth1 = 0, fourth2 = 0, fifth1 = 0, fifth2 = 0;
    for (int i = 0; i <= 30; i++) {
        for (int j = 0; j <= 30; j++) {

            if (bigram_array[i][j] >= bigram_array[first1][first2]) {
                fifth1 = fourth1;
                fifth2 = fourth2;
                fourth1 = third1;
                fourth2 = third2;
                third1 = second1;
                third2 = second2;
                second1 = first1;
                second2 = first2;
                first1 = i;
                first2 = j;
            }

            if (bigram_array[i][j] >= bigram_array[second1][second2] && bigram_array[i][j] != bigram_array[first1][first2]) {
                fifth1 = fourth1;
                fifth2 = fourth2;
                fourth1 = third1;
                fourth2 = third2;
                third1 = second1;
                third2 = second2;
                second1 = i;
                second2 = j;
            }

            if (bigram_array[i][j] >= bigram_array[third1][third2] && bigram_array[i][j] != bigram_array[first1][first2] && bigram_array[i][j] != bigram_array[second1][second2]) {
                fifth1 = fourth1;
                fifth2 = fourth2;
                fourth1 = third1;
                fourth2 = third2;
                third1 = i;
                third2 = j;
            }

            if (bigram_array[i][j] >= bigram_array[fourth1][fourth2] && bigram_array[i][j] != bigram_array[first1][first2] && bigram_array[i][j] != bigram_array[second1][second2] && bigram_array[i][j] != bigram_array[third1][third2]) {
                fifth1 = fourth1;
                fifth2 = fourth2;
                fourth1 = i;
                fourth2 = j;
            }

            if (bigram_array[i][j] >= bigram_array[fifth1][fifth2] && bigram_array[i][j] != bigram_array[first1][first2] && bigram_array[i][j] != bigram_array[second1][second2] && bigram_array[i][j] != bigram_array[third1][third2] && bigram_array[i][j] != bigram_array[fourth1][fourth2]) {
                fifth1 = i;
                fifth2 = j;
            }
        }
    }

    string the_most_frequent_bigram_here1, the_most_frequent_bigram_here2, the_most_frequent_bigram_here3, the_most_frequent_bigram_here4, the_most_frequent_bigram_here5;
    the_most_frequent_bigram_here1.push_back(alphabet[first1]);
    the_most_frequent_bigram_here1.push_back(alphabet[first2]);
    the_most_frequent_bigram_here2.push_back(alphabet[second1]);
    the_most_frequent_bigram_here2.push_back(alphabet[second2]);
    the_most_frequent_bigram_here3.push_back(alphabet[third1]);
    the_most_frequent_bigram_here3.push_back(alphabet[third2]);
    the_most_frequent_bigram_here4.push_back(alphabet[fourth1]);
    the_most_frequent_bigram_here4.push_back(alphabet[fourth2]);
    the_most_frequent_bigram_here5.push_back(alphabet[fifth1]);
    the_most_frequent_bigram_here5.push_back(alphabet[fifth2]);
    cout << "The most frequent bigrams:\n";
    cout << "array[" << first1 << "][" << first2 << "] = " << bigram_array[first1][first2] << " - > " << the_most_frequent_bigram_here1 << endl;
    cout << "array[" << second1 << "][" << second2 << "] = " << bigram_array[second1][second2] << " - > " << the_most_frequent_bigram_here2 << endl;
    cout << "array[" << third1 << "][" << third2 << "] = " << bigram_array[third1][third2] << " - > " << the_most_frequent_bigram_here3 << endl;
    cout << "array[" << fourth1 << "][" << fourth2 << "] = " << bigram_array[fourth1][fourth2] << " - > " << the_most_frequent_bigram_here4 << endl;
    cout << "array[" << fifth1 << "][" << fifth2 << "] = " << bigram_array[fifth1][fifth2] << " - > " << the_most_frequent_bigram_here5 << endl;

    string bigram_array2[5] = { the_most_frequent_bigram_here1,  the_most_frequent_bigram_here2, the_most_frequent_bigram_here3,the_most_frequent_bigram_here4,the_most_frequent_bigram_here5 };
    string bigram_array1[5] = { "ст", "но", "то", "на", "ен" };
    string bigram;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i != j) {
                for (int k = 0; k < 5; k++) {
                    for (int l = 0; l < 5; l++) {
                        if (k != l) {
                            modular_equation(bigram_value_counter(bigram_array2[i], alphabet) - bigram_value_counter(bigram_array2[j], alphabet),
                                bigram_value_counter(bigram_array1[k], alphabet) - bigram_value_counter(bigram_array1[l], alphabet), parameters_a_and_b, par_a, 961,
                                bigram_value_counter(bigram_array2[i], alphabet), bigram_value_counter(bigram_array1[k], alphabet));
                        }
                    }
                }
            }
        }
    }
    cout << "All possible keys:\n";
    for (int i = 0; i <= par_a; i++) {
        cout << "(" << parameters_a_and_b[i][0] << "," << parameters_a_and_b[i][1] << "), ";
    }
    cout << endl;

    for (int i = 0; i <= par_a; i++) {
        for (int q = 0; q < encrypted_text.length(); q++) {
            bigram.push_back(encrypted_text[q]);
            q++;
            bigram.push_back(encrypted_text[q]);
            decryption(bigram, alphabet, decrypted_text, parameters_a_and_b[i][0], parameters_a_and_b[i][1]);
            bigram.clear();
        }
        if (check_for_noice(alphabet, decrypted_text, first_bigram_position, second_bigram_posotion, bigram_array)) {
            cout << "For key(" << parameters_a_and_b[i][0] << "," << parameters_a_and_b[i][1] << ") Ч decrypted text may be not a noice: " << endl;
            cout << decrypted_text << endl;
        }
        decrypted_text.clear();
    }

    return 0;
}