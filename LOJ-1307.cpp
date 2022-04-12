#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
for(int cs=1;cs<=t;cs++)
{
    int an=0,n;
    cin>>n;
    int a[n+1];
    for(int i=0;i<n;i++)cin>>a[i];
    sort(a,a+n);

    
    for(int i=0;i<n;i++)
    for(int j=i+1;j<n;j++)
        an+=max(0,(int)(upper_bound(a,a+n,a[i]+a[j]-1)-a)-j-1);

    printf("Case %d: %d\n",cs,an);
}

}