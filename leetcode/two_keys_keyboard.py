"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.


Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

This is the problem of finding minimun steps to reach target

"""

def two_keys_keyboard(n):
    current = 1
    previous = 0
    steps = 0

    while(current < n):
        if(n % current == 0): # check if the number of A's on screen divides the total number of required A's
            previous = current # copy operation
            current += previous # paste operation

            steps += 2 # increment the count by two because we did two operations copy and paste
        else:
            current += previous # paste operation
            steps += 1 # increment the count by one because we performed only one operation i.e. paste
    return steps

print(two_keys_keyboard(6))



