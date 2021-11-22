#include <iostream>
#include <clocale>
#include <Windows.h>
#include <fstream>
#include <cstring> 
#include <string>
#include <string.h>
#include <math.h>
#include <stdlib.h>
using namespace std;

void free_symbols_counter_array(float(&symbols_counter_array)[32]) {
    for (int i = 0; i < 32; i++)
        symbols_counter_array[i] = 0;
}

void word_counter(string& text, float(&symbols_counter_array)[32], string& alphabet) {
    int alphabet_searcher = 0;
    for (int i = 0; i < text.length(); i++) {
        alphabet_searcher = 0;
        while (alphabet[alphabet_searcher] != text[i]) {
            alphabet_searcher++;
        }
        symbols_counter_array[alphabet_searcher]++;
        }
}

void compliance_index_counter(float(&symbols_counter_array)[32], float all_letters) {
    float index = 0;
    for (int i = 0; i < 32; i++) {
        index += ((symbols_counter_array[i] * (symbols_counter_array[i] - 1)) / (all_letters * (all_letters - 1 )));

    }
    cout << "Compliance index is equal to " << index << endl << endl;
    cout << "——————————————————————————————————————————————————————————————————————————————————————————————————————" << endl;
}

float compliance_index_counter_for_group(float(&symbols_counter_array)[32], float all_letters) {
    float index = 0;
    for (int i = 0; i < 32; i++)
        index += ((symbols_counter_array[i] * (symbols_counter_array[i] - 1)) / (all_letters * (all_letters - 1)));
    return index;
}

void text_normalization(char character, int ANSI_CODE, string& text) {
    if (ANSI_CODE == -72 || ANSI_CODE == -88) {
        text.push_back('å');
    }
    else if (ANSI_CODE >= -64 && ANSI_CODE <= -1) {
        text.push_back(tolower(character));
    }
}

void text_encryption(string& key_word, string& text_to_encrypt, string& encrypted_text, string& alphabet) {
    int key_word_position = -1, alphabet_position = 0, final_position = 0;
    for (int i = 0; i < text_to_encrypt.length(); i++)
    {
        key_word_position++;
        if (key_word_position >= key_word.length())
            key_word_position = 0;
        

        for (int search = 0; search <= alphabet.length(); search++)
            if (text_to_encrypt[i] == alphabet[search])
                final_position = search;


        for (int search = 0; search <= alphabet.length(); search++)
            if (key_word[key_word_position] == alphabet[search])
                final_position += search;


        if (final_position >= alphabet.length())
            final_position -= alphabet.length();
        encrypted_text.push_back(alphabet[final_position]);
    }

    cout << key_word.length() << ". Key word: \"" << key_word << "\"" << endl;
    cout << "Encrypted text:\n" << encrypted_text << endl << endl;
}

void key_length_search(string& text, float(&symbols_counter_array)[32], string& alphabet) {
    int step = 0;
    float compliance_index = 0;
    string group;

    for (int i = 2; i < 32; i++) {
        step = 0;
        while (step < i) {
            for (int j = step; j < text.length(); j = j + i) {
                    group.push_back(text[j]);
            }

            free_symbols_counter_array(symbols_counter_array);
            word_counter(group, symbols_counter_array, alphabet);
            compliance_index += compliance_index_counter_for_group(symbols_counter_array, group.length());

            group.clear();
            step++;
        }
        compliance_index = compliance_index / step;
        cout << "Compliance index for groups with step " << i << " = " << compliance_index << endl;
        compliance_index = 0;
    }
}

void key_search(float(&symbols_counter_array)[32], string& text, string& key, string& alphabet) {
    int step = 0, index_of_biggest_number_of_appearance = 0, biggest_appearence = 0;
    int shift[14] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
    int shift2[14] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
    string group;
    step = 0;
    cout << "Letter frequency: " << endl;
    while (step < 14) {
        for (int j = step; j < text.length(); j = j + 14) {
            group.push_back(text[j]);
        }

        free_symbols_counter_array(symbols_counter_array);
        word_counter(group, symbols_counter_array, alphabet);

        biggest_appearence = 0;
        index_of_biggest_number_of_appearance = 0;

        for (int j = 0; j < 32; j++) {
            if (symbols_counter_array[j] >= biggest_appearence) {
                biggest_appearence = symbols_counter_array[j];
                index_of_biggest_number_of_appearance = j;
            }
        }
        for (int j = 0; j < 32; j++) {
            cout << symbols_counter_array[j] / group.length() << " ";
        }
        cout << endl;
        shift[step] = index_of_biggest_number_of_appearance - 14;
        shift2[step] = index_of_biggest_number_of_appearance - 5;

        
        if (shift[step] < 0)
            shift[step] = shift[step] + 32;
        if (shift2[step] < 0)
            shift2[step] = shift2[step] + 32;
        group.clear();
        step++;
    } 
    cout << endl << "Key with \"o\": ";
    for (int i = 0; i<14; i++){
        cout << alphabet[shift[i]];
    }
    cout << endl << "Key with \"e\": ";
    for (int i = 0; i < 14; i++) {
        cout << alphabet[shift2[i]];
    }
}

void text_decryption(string& encrypted_text, string& alphabet, string& key) {
    string decrypted_text;
    int first_number = 0, second_number = 0, final_number = 0, key_position = 0;;
    for (int i = 0; i < encrypted_text.length(); i++) {
        first_number = 0;
        second_number = 0;

        while (alphabet[first_number] != encrypted_text[i])
            first_number++;

        if (key_position >= key.length())
            key_position = 0;
        while (alphabet[second_number] != key[key_position])
            second_number++;
        key_position++;

        final_number = first_number - second_number;
        if (final_number < 0)
            final_number += 32;
        decrypted_text.push_back(alphabet[final_number]);
    }
    cout << endl << "Decrypted text looks like: " << endl << decrypted_text;
}

int main() {
    setlocale(LC_ALL, "Russian");

    string text_to_encrypt, text_to_decrypt, encrypted_text, key_word;
    float symbols[32], index;
    char character;

    ifstream file1("To_Crypt.txt");
    while (!file1.eof()) {
        file1.get(character);
        text_normalization(character, static_cast<int> (character), text_to_encrypt);
    }
    file1.close();

    string alphabet = "àáâãäåæçèéêëìíîïğñòóôõö÷øùúûüışÿ";

    int key_word_inputer = 0;
    for (int i = 1; i <= 5; i++) {
        key_word.clear();
        encrypted_text.clear();
        key_word_inputer = 0;
        while (key_word_inputer != i) {
            key_word.push_back(alphabet[key_word_inputer]);
            key_word_inputer++;
        };

        text_encryption(key_word, text_to_encrypt, encrypted_text, alphabet);
        free_symbols_counter_array(symbols);
        word_counter(encrypted_text, symbols, alphabet);
        compliance_index_counter(symbols, encrypted_text.length());
    }

    for (int i = 10; i <= 20; i++) {
        key_word.clear();
        encrypted_text.clear();
        key_word_inputer = 0;
        while (key_word_inputer != i) {
            key_word.push_back(alphabet[key_word_inputer]);
            key_word_inputer++;
        };

        text_encryption(key_word, text_to_encrypt, encrypted_text, alphabet);
        free_symbols_counter_array(symbols);
        word_counter(encrypted_text, symbols, alphabet);
        compliance_index_counter(symbols, encrypted_text.length());
    }

    ifstream file2("To_Decrypt.txt");
    while (!file2.eof()) {
        file2.get(character);
        text_normalization(character, static_cast<int> (character), text_to_decrypt);
    }
    file2.close();
    cout << "Text we need to decrypt looks like: " << endl;
    cout << text_to_decrypt << endl;
    key_length_search(text_to_decrypt, symbols, alphabet);
    string key;
    key_search(symbols, text_to_decrypt, key, alphabet);
    key = "ıêîìàÿòíèêôóêî";
    text_decryption(text_to_decrypt, alphabet, key);
    system("pause");
	return 0;
}