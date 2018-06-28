class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        vector<int> c;
        int temp = 0;
        for(int i = 0;i<A.size();i++)
            for(int j = 0;j<B.size();j++){
                if(A.at(i)==B.at(j)){
                    c.push_back(j);
                    break;
                }
            }
        return c;
    }
};
