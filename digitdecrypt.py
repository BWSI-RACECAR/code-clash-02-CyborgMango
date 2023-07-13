"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #2 - Digit Decrypt (digitdecrypt.py)


Author: Koneshka Bandyopadhyay

Difficulty Level: 4/10

Prompt: Koneshka has a collection of 9 RACECARS, each with unique speed and a crypted 
identification number that helps identify the rankings of each of the RACECARS in terms
of speed. Write a program that helps identify the ranking of a car given the identification
number. The way we can decrypt this identification number is by adding digits of the number 
until we reach single digits. For example: Let’s say that the identification number is 38. 
Then, we add ‘3’ + ‘8’ to get 11. We further add the digits ‘1’+ ‘1’ to get 2, ranking the car
in 2nd place or 2nd fastest out of 9. Car with identification 1111 gives us 1+1+1+1=4, ranking 
the car 4th fastest out of 9. The goal is to add the digits until we reach single digits.

Test Cases:
Input: 48 Output: 3

Input: 13 Output: 4

Input: 0 Output: 0 
"""

class Solution:    
    def digitdecrypt(self, num):
            new=str(num)
            counter=0
            while len(new)>0:
              counter+=int(new[0])
              new=new[1:len(new)-1]
            counter2=0
            counter3=str(counter)
            while len(counter3)>0:
              counter2+=int(counter3[0])
              counter3=counter3[1:len(counter3)-1]
            return counter2
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()
