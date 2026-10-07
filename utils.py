def is_palindrome(s):
    """Return True if the given string is a palindrome, otherwise False."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_words(text):
    """Return the number of words in the given text."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


print(is_palindrome("Madam"))
print(count_words("Artificial Intelligence Tools Lab"))
print(celsius_to_fahrenheit(25))

