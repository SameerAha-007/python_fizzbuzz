l=list(map(int,input("Enter a sequence of numbers:").split()))
l1=[]
for i in l:
  if i not in l1:
    l1.append(i)
l1.sort()
print(f"Removed Duplicates:{l1}")