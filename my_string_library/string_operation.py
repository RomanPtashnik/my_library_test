class StringUtils:          # Оборачиваем функции в класс, для дальнейшего расширения и поддержки
    def reverse_string(s: str) -> str:      # Создаем функцию ревёрса строки
        return s[::-1]
    
    def count_vowels(s: str) -> int:        # Создаем функцию поиска гласных строки (Русскиие и латинские буквы)
        vol = 'aeiouAEIOUаоуэыияёюеАОУЭЫИЯЁЮЕ'
        return sum(1 for char in s if char in vol)
            
    def is_palindrome(s: str) -> bool:      # Создаем функцию проверки палиндрома
        s = s.lower().replace(" ", "")
        return s == s[::-1]


print(StringUtils.count_vowels('')) 