class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res = {""};

        for (char d : digits) {
            vector<string> temp;
            string letters = mapping[d - '0'];
            
            for (string comb : res) {
                for (char letter : letters) {
                    temp.push_back(comb + letter);
                }
            }

            res = temp;
        }
        
        return res;
    }
};
