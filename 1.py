#!/usr/bin/python
def f(n,a,b,c):
	if n==1:
		print a,"->",c
	else:
		f(n-1,a,c,b)
		f(1,a,b,c)
		f(n-1,b,a,c)
f(3,"A","B","C")

