#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <windows.h>
#include <iomanip>
std::string alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
std::string alphp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ";
char MyToLower(char r)
{
    switch (r)
    {
    case 'А': r = 'а'; break;
    case 'Б': r = 'б'; break;
    case 'В': r = 'в'; break;
    case 'Г': r = 'г'; break;
    case 'Д': r = 'д'; break;
    case 'Е': r = 'е'; break;
    case 'Ж': r = 'ж'; break;
    case 'З': r = 'з'; break;
    case 'И': r = 'и'; break;
    case 'Й': r = 'й'; break;
    case 'К': r = 'к'; break;
    case 'Л': r = 'л'; break;
    case 'М': r = 'м'; break;
    case 'Н': r = 'н'; break;
    case 'О': r = 'о'; break;
    case 'П': r = 'п'; break;
    case 'Р': r = 'р'; break;
    case 'С': r = 'с'; break;
    case 'Т': r = 'т'; break;
    case 'У': r = 'у'; break;
    case 'Ф': r = 'ф'; break;
    case 'Х': r = 'х'; break;
    case 'Ц': r = 'ц'; break;
    case 'Ч': r = 'ч'; break;
    case 'Ш': r = 'ш'; break;
    case 'Щ': r = 'щ'; break;
    case 'Ъ': r = 'ъ'; break;
    case 'Ы': r = 'ы'; break;
    case 'Ь': r = 'ь'; break;
    case 'Э': r = 'э'; break;
    case 'Ю': r = 'ю'; break;
    case 'Я': r = 'я'; break;
    
    }
    return r;
}


std::string format(std::string s) {
    for (int i = 0; i < s.length(); i++) {
        if (!(s[i] >= 'а' && s[i] <= 'я') && s[i]!='ё') {
            s[i]=' ';
        }
    }
    std::string t;
    char* pch = strtok((char*)s.c_str(), " ");
    while (pch != NULL) {
        t += std::string(pch)+" ";
        pch = strtok(NULL, " ");
    }
    
    return t;
}

std::string probdel(std::string s) {
    int size=0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != ' ') {
            size++;
        }
    }
    char* ns = new char[size];
    int j=0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != ' ') {
            ns[j]=s[i];
            j++;
        }
    }
    return std::string(ns);
}

double ent(std::string s,std::string alpha) {
    double ent=0;
    for (int i = 0; i < alpha.length(); i++) {
        double count = 0;
        std::cout << alpha[i] << " ";
        for (int j = 0; j < s.length(); j++) {
            if (alpha[i] == s[j]) {
                count++;
            }
        }
        if (count != 0) {
            ent += -(count / s.length()) * log2(count / s.length());
        }
        std::cout << count / s.length() << std::endl;
    }
    return ent;
}
double bifreqent(std::string s, std::string alpha) {
    double bient = 0;
    
    for (int i = 0; i < alpha.length(); i++) {
        for (int j = 0; j < alpha.length(); j++) {
            double count = 0;
            std::cout << alpha[i] << alpha[j] << " ";
            for (int m = 0; m < s.length() - 1; m++) {
                if (alpha[i] == s[m] && alpha[j] == s[m + 1]) {

                    
                    count++;


                }

            }
            if (count != 0) {
                bient += -0.5*count / (s.length()-1) * log2(count / (s.length()-1));
            }
            std::cout << std::setprecision(5) << count /(s.length()-1) << std::endl;


        }
    }
    return bient;
}
double bientfreqent2(std::string s, std::string alpha) {
    double bient = 0;
    
    for (int i = 0; i < alpha.length(); i++) {
        for (int j = 0; j < alpha.length(); j++) {
            double count = 0;
            std::cout << alpha[i] << alpha[j] << " ";
            for (int m = 0; m < s.length() - 3; m += 2) {
                if (alpha[i] == s[m] && alpha[j] == s[m + 1]) {
                   
                    count++;


                }

            }
            if (count != 0) {
                bient += -0.5 * count / (s.length() / 2) * log2(count / (s.length() / 2));
            }
            std::cout << std::setprecision(5) << count / (s.length() / 2) << std::endl;


        }
    }
    return bient;
}
int main() {


    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    std::string text;
    std::string s;
    std::ifstream in("text.txt");
    if (in.is_open()) {
        while (getline(in,s)) {
            text += s;
        }
        in.close();
    }
    for (int i = 0; i < text.length(); i++) {
        text[i] = MyToLower(text[i]);
    }
    
    std::ofstream out,ou;          
    out.open("form.txt"); 
    if (out.is_open())
    {
        out << format(text) << std::endl;
    }
    ou.open("berprob.txt");
    if (ou.is_open())
    {
        ou << probdel(format(text)) << std::endl;
    }
    
   std::cout << "З пробілами" << std::endl;
   std::cout << "Ентропія:" << ent(format(text),alphp) << std::endl;
   std::cout << "H1" << std::endl;
   std::cout << "Ентропія:" << bifreqent(format(text),alphp) << std::endl;
   std::cout << "H2" << std::endl;
   std::cout << "Ентропія:" << bientfreqent2(format(text),alphp) << std::endl;
   std::cout << "Без пробілів" << std::endl;
   std::cout << "Ентропія:" << ent(probdel(format(text)),alph) << std::endl;
   std::cout << "H1" << std::endl;
   std::cout << "Ентропія:" << bifreqent(probdel(format(text)),alph) << std::endl;
   std::cout << "H2" << std::endl;
   std::cout << "Ентропія:" << bientfreqent2(probdel(format(text)),alph) << std::endl;
    




    return 0;
}
