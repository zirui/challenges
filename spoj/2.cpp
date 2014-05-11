#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>
#include <string.h>
using namespace std;


#define MAX_LEN 100001

bool primes[MAX_LEN];

int main()
{
    //freopen("in.data","r",stdin);
    int ncase;
    int m,n;
    cin>>ncase;
    while(ncase--)
    {
       cin>>m>>n;
       //vector<int> primes(n-m+1,1);
       memset(primes,1,sizeof(primes));
       int sqrtn = sqrt(n);
       for(int i =2;i<=sqrtn+1;i++)
       {
           int start = m/i * i;
           for(int j= start;j<=n;j+=i)
           {
               if(j !=i && j >= m)
                   primes[j-m] = 0;
           }
       }
       //for(int i = 0;i< primes.size();i++)
       for(int i = 0;i<n-m+1;i++)
           if(primes[i] && i+m != 1)
               cout<<i+m<<endl;
       if (ncase > 0)
           cout<<endl;
    }

}
