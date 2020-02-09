# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0    #O(1)
    while (a < n * n * n): #O(n^3)
      a = a + n * n   #O(n^2)
```
The while loop is n^3 but it's happening at a rate of n^2. The n^2 inside the while loop 
cancels out the n^3 outside the while loop, which makes it just n. 

However, I'm also wondering if a = a + n * n is just constant time because it's a variable assignemnt

ANSWER: O(n)


```
b)  sum = 0
    for i in range(n): 
      j = 1
      while j < n: #logn
        j *= 2
        sum += 1
```

ANSWER: O(n log n) because it's nested

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
No matter what n is, it will recursively call itself n times. If n=3, it will call itself 3 times

ANSWER: O(n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


ANSWER: Binary search is the best cause you're trying to find some point between 0 stories and n stories by dividing by 2.

So divide n by 2.... This is the middle point. Test to see if egg breaks. If egg breaks then you need to go lower so divide by 2 again. Keep doing this until egg doesn't break
