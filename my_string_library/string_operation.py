class StringUtils:          # Оборачиваем функции в класс, для дальнейшего расширения и поддержки
    @staticmethod
    def reverse_string(s: str) -> str:      # Создаем функцию ревёрса строки
        if s == '': # Проверяем введена ли пустая строка
            return 'Введенна пустая строка!'
        elif s.isspace(): # Проверяем строку на пробелы
            return 'Введенны пробелы'
        elif s.isspace() == False: # Если введены пробелы и текст убираем пробелы и ревёрсим строку
            return s[::-1].strip()
        else:
            return s[::-1]
        
    @staticmethod
    def count_vowels(s: str) -> int:        # Создаем функцию поиска гласных строки (Русскиие и латинские буквы)
        vol = 'aeiouAEIOUаоуэыияёюеАОУЭЫИЯЁЮЕ'
        return sum(1 for char in s if char in vol)
    
    @staticmethod
    def is_palindrome(s: str) -> bool:      # Создаем функцию проверки палиндрома
        s = s.lower().replace(" ", "")
        return s == s[::-1]


print(StringUtils.count_vowels('')) 