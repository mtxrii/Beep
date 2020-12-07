> "Programming? All you ever do on that laptop is boop beeps. Beeps bops and boops"
>
> Fine then. You wanna see a screen full of beeps boops?

# Beep
A fun little novelty text encoder/decoder

Fire it up on write mode and give it a text file. Then specify what file to encode it to. Here's an example:

Given the file `collatz.py`:
```python
# Iterate collatz up to n
def collatz(n):
  while n > 1:
    if n % 2 == 1:
      n = 3 * n + 1
    else:
      n /= 2

    yield n

for i in collatz(10):
  print(i)
```

It's beepified version looks like this:
```
# | bop beep beep, boop, beep, beep boop beep, beep boop, boop, beep,  | boop beep boop beep, boop boop boop, beep boop beep beep, beep boop beep beep, beep boop, boop, boop boop beep beep,  | beep beep boop, beep boop boop beep,  | boop, boop boop boop,  | boop beep, 
boop beep beep, beep, beep beep boop beep,  | boop beep boop beep, boop boop boop, beep boop beep beep, beep boop beep beep, beep boop, boop, boop boop beep beep, boop beep bop, boop beep, beep boop bop, boop bop boop, 
 |  | beep boop boop, beep beep beep beep, beep beep, beep boop beep beep, beep,  | boop beep,  | > | beep boop boop boop boop, boop bop boop, 
 |  |  |  | beep beep, beep beep boop beep,  | boop beep,  | % | beep beep boop boop boop,  | == | beep boop boop boop boop, boop bop boop, 
 |  |  |  |  |  | boop beep,  | = | beep beep beep boop boop,  | * | boop beep,  | + | beep boop boop boop boop, 
 |  |  |  | beep, beep boop beep beep, beep beep beep, beep, boop bop boop, 
 |  |  |  |  |  | boop beep,  | /= | beep beep boop boop boop, 

 |  |  |  | boop beep boop boop, beep beep, beep, beep boop beep beep, boop beep beep,  | boop beep, 

beep beep boop beep, boop boop boop, beep boop beep,  | beep beep,  | beep beep, boop beep,  | boop beep boop beep, boop boop boop, beep boop beep beep, beep boop beep beep, beep boop, boop, boop boop beep beep, boop beep bop, beep boop boop boop boop, boop boop boop boop boop, beep boop bop, boop bop boop, 
 |  | beep boop boop beep, beep boop beep, beep beep, boop beep, boop, boop beep bop, beep beep, beep boop bop, 
```

And of course given this mess you can return it back to what it was before, making this thing also useful for encoding secrets n stuff. Any intruder who comes across your "homework" folder will be met with the transcript of an 80s sci fi robot enemy testifying in court.
