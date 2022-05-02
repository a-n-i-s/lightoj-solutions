#include<bits/stdc++.h>
using namespace std;
vector<int>sa,c;
string s;

void sort()
{
vector<int>cc[256];
for(int i=0;s[i];i++)
cc[s[i]].push_back(i);
for(int i=0,m=0;i<256;i++)
{
for(int j=0;j<cc[i].size();j++)
sa[m++]=cc[i][j];	
}
}

void sort1()
{
vector<int>cc[s.size()+1];
for(int i=0;i<sa.size();i++)
cc[c[sa[i]]].push_back(sa[i]);

for(int i=0,m=0;i<sa.size();i++)
{
for(int j=0;j<cc[i].size();j++)
sa[m++]=cc[i][j];	
}
}


void suffix_array()
{
	s+="$";
	int l=s.size();
	sa.clear();
	for(int i=0;i<l;i++)sa.push_back(i);
	sort();
	vector<int>cc(l+1);
	c.assign(l+1,0);
	
	for(int i=1;i<l;i++)
		c[sa[i]]=c[sa[i-1]]+(s[sa[i-1]]!=s[sa[i]]);
	
	for(int k=1;k<l;k*=2)
	{
		
	for(int i=0;i<sa.size();i++)sa[i]=(sa[i]-k+l)%l;
	
	sort1();
	
	cc[sa[0]]=0;
	for(int i=1;i<l;i++)
{		pair<int,int> d={c[sa[i-1]],c[(sa[i-1]+k)%l]};
		pair<int,int> dd={c[sa[i]],c[(sa[i]+k)%l]};
		cc[sa[i]]=cc[sa[i-1]]+(d!=dd);
}
	c=cc;
	if(c[sa[l-1]]==l-1)break;
	
	}
}

vector<int>lcp;
void get_lcp()
{int k=0;
lcp.assign(s.size(),0);
for(int i=0;i<s.size();i++)
{
	int j=sa[c[i]-1];
	while(s[i+k]==s[j+k] )k++;
	lcp[c[i]]=k;
	k=max(0,k-1);
	
}
	
}

int main()
{
	
int t;
cin>>t;
for(int cs=1;cs<=t;cs++)
{
cin>>s;
int a,r;
cin>>a>>r;
suffix_array();
get_lcp();

int an=0; for(int i=0;i<sa.size();i++) { int x=sa.size()-1     -    
sa[i]  -   lcp[i];
     an+=max(min(x+lcp[i],r)-lcp[i],0)-max(min(x+lcp[i],a-1)-lcp[i],0);	
}
	
cout<<"Case "<<cs<<": "<<an<<endl;	
}

}
