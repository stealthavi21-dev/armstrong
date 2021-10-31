i=int(input())
while i>0:
  b=int(input())
  c=0
  for j in str(b):
    c+=int(j)**len(str(b))
  if c==b:
    print('YES')
  else:
    print('NO')
  i-=1