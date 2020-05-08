from more_itertools import locate
from  collections import  defaultdict

n = int(input())        #num of nodes
mat = list(map( int , input().split()))
m = []
k = 0
for i in range(n):
	m.append(mat[k:k+n])
	k+=n

d = defaultdict(list)
ctr_odd = 0

for index , i in enumerate(m):
	d[index] = list(locate(i))
	if len(d[index])%2!=0:
		ctr_odd+=1
		cur_node = index

if ctr_odd!=(0 or 2):
	print(0)
	exit()

edge = []
flag = 0
while(flag==0):
	edge.append((cur_node , d[cur_node][0]))
	val = d[cur_node][0]
	del d[cur_node][0]
	d[val].remove(cur_node)
	cur_node = val
	if len(d[cur_node])==0:
		flag = -1
		print(1)

