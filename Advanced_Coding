#---------------------
# Problem Statement 1
#---------------------

# Alice challenged Bob to write the same word as his on a typewriter. Both are kids and are making some mistakes in typing and are making use of the ‘#’ key on a typewriter to delete the last character printed on it. An empty text remains empty even after backspaces. 

# Input Format
# The first line contains a string typed by Bob.

# The second line contains a string typed by Alice.

# Output Format
# The first line contains ‘YES’ if Alice is able to print the exact words as Bob, otherwise ‘NO’.

# Constraints
# 1 <= Bob.length

# Alice.length <= 100000

# Bob and Alice only contain lowercase letters and '#' characters.

#CODE
def process(text):
    result = []
    
    for char in text:
        if char == '#':
            if result:
                result.pop()
        else:
            result.append(char)
    return "".join(result)

def compare_process(bob,alice):
    return process(bob) == process(alice)

#input
bob = input()
alice = input()

if compare_process(bob,alice):
    print("YES")
else:
    print("NO")

#Time coplexity : O(N + M)
#Space coplexity : O(N + M)

# We traverse both strings once, and each append/pop operation takes constant time. Therefore total time complexity is O(N + M).
# We use extra lists to store processed characters, so space complexity is O(N + M).



#----------------------
# Problem Statement 2
#----------------------

# You are provided with a 2D array(N*M). Your task is to create an ArrayList of Node objects, where each row of the 2D array corresponds to one entry in the ArrayList. After that, a doubly-linked list is constructed, arranging nodes first by even indices from the ArrayList, followed by the odd indices.

# Input Format
# The first line contains an integer N, representing the size of the array row.

# The second line contains an integer M, representing the size of array col.

# The third line contains an array.

# Output Format
# return the linked list

# Constraints
# 1 <= N < 10^2
# 1 <= M < 10^2

#CODE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def createLinkedList(arr, N, M):

    # Step 1: Create ArrayList of Nodes
    nodes = []

    for row in arr:
        nodes.append(Node(row))

    # Step 2: Take even index nodes
    even_nodes = []

    for i in range(0, len(nodes), 2):
        even_nodes.append(nodes[i])

    # Step 3: Take odd index nodes
    odd_nodes = []

    for i in range(1, len(nodes), 2):
        odd_nodes.append(nodes[i])

    # Step 4: Combine
    ordered = even_nodes + odd_nodes

    # Step 5: Create doubly linked list
    for i in range(len(ordered) - 1):
        ordered[i].next = ordered[i + 1]
        ordered[i + 1].prev = ordered[i]

    # head of linked list
    return ordered[0]


# Take input
N = int(input())
M = int(input())
#Empty array
arr = []

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

head = createLinkedList(arr, N, M)

# Print Linked List
temp = head

while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next

print("None")


# Time Complexity :	O(N)
# Space Complexity : O(N)

# We traverse the nodes multiple times, but each traversal is linear. Therefore overall time complexity is O(N).
# Extra lists and linked list nodes require linear extra memory, so space complexity is O(N).



#---------------------
# Problem Statement 3
#---------------------

# Sid is reading a paragraph of a story and notices N different sentences. He's curious to know which sentence is the longest. Help Sid find the length of the longest sentence in the story. Sentences are separated by a comma(,),no other symbols are used except comma.
 
# Input Format
# The first line of input contains a string where sentences are separated by commas ( ,) 

# Output Format
# Display a single integer, that denotes the length of the longest sentence.

# Constraints
#  1<=N<=20

#CODE
# Take input string
s = input()

# Split string using comma
sentences = s.split(",")

# Variable to store maximum length
max_length = 0

# Traverse each sentence
for ch in sentences:

    # Find length of current sentence
    current_length = len(ch)

    # Update maximum length
    if current_length > max_length:
        max_length = current_length

# Print answer
print(max_length)

# Time Complexity :	O(N)
# Space Complexity : O(N)

# The split() function traverses the string once, taking O(N) time. The loop also processes all characters overall, so total time complexity remains O(N).
# Extra space is used to store separated sentences, therefore space complexity is O(N).



#---------------------
# Problem Statement 4
#---------------------

# Assert whether the given string has all the letters of the English alphabet or not.
# If yes return "True" else return "False".
# Assume the string contains nothing but lowercase English letters.

# Input Format
# The string to be checked.

# Output Format
# Display "True" if all the letters in English alphabets are present else display "False".

# Note: Output is case-sensitive.

# Constraints
# 1<=|S|<=1e^5

#CODE
s = "the quick brown fox jumps over the lazy dog"
s = s.lower()
alphabates = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for char in alphabates:
    if char not in s:
        is_pangram = False
        break

if is_pangram:
    print("True")
else:
    print("False")


# Time Complexity : O(N)
# Space Complexity : O(1)



#---------------------
# Problem Statement 5
#---------------------

# One day, Jack finds a string of characters. He is very keen to arrange them in reverse order, i.e., the first characters become the last characters, the second characters become the second-last characters, and so on.

# Now he wants your help  to find the kth character from the new string formed after reverse the original string.

# Note: String contains only lowercase Latin letters.

# Input Format

# The first line contains two integers n, k — the length of array and the value of k respectively.

# The second line contains a string containing n characters.

# Output Format

# Print a single line containing the kth character of the string.

# Constraints

# 1 ≤ k ≤ n≤ 10^6

# Testcase Input

# 5 2

# abdfa

# Testcase Output

# f

#CODE
# Input
n, k = map(int, input().split())

s = input()

# Reverse string
rev = s[::-1]

# Print kth character
print(rev[k - 1])



#---------------------
# Problem Statement 6
#----------------------

# You are provided with a 2D array(N*M). Your task is to create an ArrayList of Node objects, where each row of the 2D array corresponds to one entry in the ArrayList. After that, a doubly-linked list is constructed, arranging nodes first by even indices from the ArrayList, followed by the odd indices.

# Input Format

# The first line contains an integer N, representing the size of the array row.

# The second line contains an integer M, representing the size of array col.

# The third line contains an array.

# Output Format

# return the linked list

# Constraints

# 1 <= N < 10^2

# 1 <= M < 10^2

# Testcase Input

# 4

# 6

# 2 4 5 3 6 7

# 5 3 6 3 6 7

# 3 6 7 2 6 8

# 4 2 1 6 8 9

# Testcase Output

# 2 <---> 4 <---> 5 <---> 3 <---> 6 <---> 7 <---> 3 <---> 6 <---> 7 <---> 2 <---> 6 <---> 8 <---> 5 <---> 3 <---> 6 <---> 3 <---> 6 <---> 7 <---> 4 <---> 2 <---> 1 <---> 6 <---> 8 <---> 9 <---> null



#---------------------
# Problem Statement 7
#---------------------

# There are n spaceship at given lightyears away from the earth and traveling to reach a distant star system at k lightyear away from earth. You are given two integer arrays, position and speed, both of length n, where

# P[i] is the current distance of the ith spaceship

# S[i] is the speed of the ith spaceship in lightyears per year.

# As the spaceships travel toward the star system, an interesting phenomenon occurs: when a faster spaceship catches up to a slower one, it reduces its speed to match the slower spaceship's speed, forming a fleet. A fleet is a group of one or more spaceships that travel together at the same speed.

# Given this information, determine the number of distinct spacecraft fleets that will arrive at the destination star system. A fleet is considered distinct if no other fleet arrives at the destination at the same time while traveling together.

# Input Format

# The first line contains an integer 'n', representing the total number of spaceships.

# The second line contains an integer 'k', representing the distance of the star system from Earth.

# The third line contains 'n' space-separated integers denoting the current distance of the i-th spaceship from Earth.

# The fourth line contains 'n' space-separated integers denoting the speed of the i-th spaceship.

# Output Format

# Return the number of spacecraft fleets that will arrive at the destination.

# Constraints

# 1 <= n <= 10^5

# 0 < k <= 10^6

# 0 <= P[i] < target

# 0 < S[i] <= 10

# Testcase Input

# 4

# 14

# 10 8 5 3

# 2 4 1 3

# Testcase Output

# 2




#---------------------
# Problem Statement 8
#---------------------

# Ram gave Shyaam a challenge, he gave shyaam the head of a linked list, and an integer k. He asked Shyaam to swap the values of the Kth node from the beginning and the Kth node from the end (the list is 1-indexed).

# Note: The number of nodes in the list is N.

# Input Format

# The first line contains an integer N, representing the number of nodes in the linked list.

# The second line contains N space-separated integers, each representing the value of a node in the linked list.

# The third line contains an integer K, indicating the positions of the nodes to be swapped.

# Output Format

# Output the linked list after swapping the values of the two specified nodes.

# Constraints

# 1 <= K <= N <= 10^5

# 0 <= Node.val <= 10^2

# Testcase Input

# 5

# 1 2 3 4 5

# 2

# Testcase Output

# 1 4 3 2 5

