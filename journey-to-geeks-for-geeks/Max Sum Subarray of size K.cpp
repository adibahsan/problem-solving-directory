//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
public:
    long maximumSumSubarray(int K, vector<int> &Arr , int N){
        long currentWindowSum = 0;
        int i = 0;
        for (;i<K;i++){
            currentWindowSum += Arr[i];
        }

        long maxSum  = currentWindowSum;

        int j = 0;

        for (; i<Arr.size(); i++){
            currentWindowSum -= Arr[j];
            currentWindowSum += Arr[i];

            if(currentWindowSum > maxSum){
                maxSum = currentWindowSum;
            }
            j++;
        }

        return maxSum;
        // code here
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int N,K;
        cin >> N >> K;;
        vector<int>Arr;
        for(int i=0;i<N;++i){
            int x;
            cin>>x;
            Arr.push_back(x);
        }
        Solution ob;
        cout << ob.maximumSumSubarray(K,Arr,N) << endl;
    }
    return 0;
}
// } Driver Code Ends
