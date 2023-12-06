#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <regex>

std::map<const std::string, const std::string> NUMBER_MAPPING = {
    {"one", "1"},
    {"two", "2"},
    {"three", "3"},
    {"four", "4"},
    {"five", "5"},
    {"six", "6"},
    {"seven", "7"},
    {"eight", "8"},
    {"nine", "9"}};

std::vector<std::string> getLines()
{
    std::vector<std::string> lines;
    std::ifstream file("input.txt");
    if (!file.is_open())
    {
        return lines;
    }

    std::string line;
    while (std::getline(file, line))
    {
        lines.push_back(line);
    }
    file.close();
    return lines;
}

int getSubTotal(const std::string &line)
{
    std::vector<int> nums;
    for (const auto &x : line)
    {
        if (std::isdigit(x))
        {
            nums.push_back(x - '0');
        }
    }
    if (nums.empty())
    {
        return 0;
    }
    return nums[0] * 10 + nums[nums.size() - 1];
}

int main()
{
    int total1 = 0, total2 = 0;

    std::vector<std::string> lines = getLines();
    for (std::string &l : lines)
    {
        total1 += getSubTotal(l);
        for (const auto &[key, value] : NUMBER_MAPPING)
        {
            l = std::regex_replace(l, std::regex(key), key + NUMBER_MAPPING[key] + key);
        }
        total2 += getSubTotal(l);
    }

    std::cout << total1 << " " << total2 << std::endl;

    return 0;
}