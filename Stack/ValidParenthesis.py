"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""


#DONE AND UNDERSTOOD
def isValid(s):  
        """
        :type s: str
        :rtype: bool

        Implement a stack to keep track of the open brackets
        1. If the current character is an open bracket, push it to the stack
        2. If the current character is a closing bracket, check if the stack is empty
        3. If the stack is not empty, check if the top of the stack is the corresponding open bracket
        4. If it is, pop the top of the stack
        5. If it is not, return False
        6. If the stack is empty, return True
        
        """
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)

            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()

            else:
                return False

        return True if not stack else False

# Time Complexity: O(n)
# Space Complexity: O(n)

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
print(isValid("([])")) # True
print(isValid("([)]")) # False
print(isValid("{[]}")) # True
print(isValid("]")) # False
print(isValid("[")) # False
print(isValid("[")) # False
print(isValid("{{")) # False
print(isValid("{{}")) # False
print(isValid("{{}}")) # True



        
