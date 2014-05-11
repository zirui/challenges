#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

// you can also use includes, for example:
// #include <algorithm>

struct tuple
{
    int index;
    int val;
};

vector<int> counting_sort(vector<tuple>& A,int max_value)
{
    vector<int> count(max_value+1,0);
    vector<int> rst(A.size());
    for (int i = 0;i< A.size();i++)
            count[A[i].val] += 1;
    for (int i = 1;i< count.size();i++)
            count[i] += count[i-1];
    for (int i = A.size()-1;i>=0;i--)
    {
        //rst[count[A[i].val]-1] = A[i].val;
        rst[count[A[i].val]-1] = A[i].index;
        //cout<<count[A[i].val]-1<<" "<<A[i].val<<" "<<A[i].index<<endl;
        count[A[i].val] -= 1;
    }
    return rst;
}

int solution(vector<int> &A) 
{
    vector<tuple> A_tuple(A.size());
    for(int i = 0;i< A.size();i++)
    {
        A_tuple[i].index = i;
        A_tuple[i].val = A[i];
    }
    
    int max_value = 2000000000;
    //int max_value = 2000;
        

    vector<int> B = counting_sort(A_tuple,max_value);
    
    vector<int> C(A.size());

    C[0] = 1;
    int max_len = 0;
    for (int i = 1;i< B.size();i++)
    {
        if(B[i] >= B[i-1])
        {
            C[i] = C[i-1] + 1;
            max_len = max(C[i],max_len);
        }
        else
            C[i] = 1;
        //cout<<B[i]<<" "<<max_len<<endl;
    }
    return max_len;
}


int main()
{ 
    freopen("data","r",stdin);
    vector<int> A;
    int val;
    while(cin>>val)
    {
        A.push_back(val);
        //cout<<val<<endl;
    }
    int ans = solution(A);
    cout<<ans<<endl;

    return 0;
}
