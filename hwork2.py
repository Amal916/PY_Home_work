paragraph = """
Python is a popular programming language. 
This Python course covers the basics of programming, 
data structures, and object-oriented concepts.
"""
length = len(paragraph)
print("Length of paragraph:", length)
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
preview = paragraph[:50]
print("Preview (first 50 characters):", preview)
paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python' with 'PYTHON':")
print(paragraph)
paragraph_lower = paragraph.lower()
print("\nLowercase paragraph:")
print(paragraph_lower)
paragraph_clean = paragraph_lower.strip()
print("\nTrimmed paragraph:")
print(paragraph_clean)
words = paragraph_clean.split()
print("\nList of words:")
print(words)
if "course" in words:
    print("\nThe word 'course' exists in the paragraph.")
else:
    print("\nThe word 'course' was not found in the paragraph.")
final_message = "The course description is {} characters long and has {} words.".format(len(paragraph_clean), len(words))
print("\n" + final_message)
