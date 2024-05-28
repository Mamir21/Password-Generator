import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        charset = string.ascii_letters + string.digits
    elif complexity == 'medium': 
        charset = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        charset = string.ascii_letters + string.digits + string.punctuation + '£€¥§©®'
    else:
        raise ValueError("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        
    password = ''.join(random.choice(charset) for _ in range(length))
    return password
    
if __name__ == "__main__": 
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ").lower()
    print("Generated password:", generate_password(length, complexity))
