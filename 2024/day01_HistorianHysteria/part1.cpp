#include <iostream>
#include <fstream>
#include <string>

class HistorianHysteria {
	public:

}


int main(){
	std::ifstream file("input/sample.txt");
	std::string str;
	std::string file_contents;

	while (std::getline(file, str)){
		file_contents += str;
		file_contents.push_back('\n');
	}
	std::cout << file_contents << std::endl;
	return 0;
}
