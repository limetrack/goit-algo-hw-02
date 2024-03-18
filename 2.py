from collections import deque

def is_palindrome(s):
    # Підготовка рядка: видалення пробілів та перетворення на нижній регістр
    formatted_string = ''.join(s.split()).lower()
    
    # Додавання символів до двосторонньої черги
    char_deque = deque(formatted_string)
    
    while len(char_deque) > 1:
        # Порівнюємо символи з обох кінців черги
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Тестування функції
test_strings = ["A man a plan a canal Panama", "Madam In Eden I’m Adam", "Not a Palindrome", "Was it a car or a cat I saw?"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")
