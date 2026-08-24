"""
This module contains the solution for Day 3 of the Advent of Code challenge. The challenge involves processing a list of binary numbers to calculate two specific values: the gamma rate and the epsilon rate. The gamma rate is determined by finding the most common bit in each position across all binary numbers, while the epsilon rate is derived from the least common bit in each position.

"""

## Student File Management Program :

import json
import collections
import os

# ==========================================
# PRACTICE: Student File Management Program
# ==========================================

def save_students(students, filename="students.json"):
    """Saves a list of student dictionaries to a file using JSON."""
    try:
        with open(filename, "w") as file:
            # json.dumps converts Python list/dict to a string format
            json_string = json.dumps(students, indent=4)
            file.write(json_string)
        print(f"Successfully saved {len(students)} student records.")
    except IOError as e:
        print(f"File writing error: {e}")

def load_students(filename="students.json"):
    """Reads student records back from a file."""
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "r") as file:
            file_content = file.read()
            # json.loads converts the string text back into Python lists/dicts
            return json.loads(file_content)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading file: {e}")
        return []


# ==========================================
# TARGET: Day 3 Text Analyzer Challenge
# ==========================================

def analyze_text_file(filename):
    """Reads a text file and analyzes words, lines, characters, and frequencies."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return

    line_count = len(lines)
    char_count = 0
    all_words = []

    for line in lines:
        char_count += len(line)
        # Clean punctuation and split line into raw words
        cleaned_line = line.lower()
        for punct in [".", ",", "!", "?", ";", ":", "-", "\n"]:
            cleaned_line = cleaned_line.replace(punct, " ")
        
        words = cleaned_line.split()
        all_words.extend(words)

    word_count = len(all_words)
    
    # Find the most common word
    if all_words:
        word_counts = collections.Counter(all_words)
        most_common_word, highest_freq = word_counts.most_common(1)[0]
    else:
        most_common_word, highest_freq = "None", 0

    # Output the structured analysis metrics
    print("\n📊 --- FILE ANALYSIS RESULTS ---")
    print(f"📄 Total Lines      : {line_count}")
    print(f"🔤 Total Characters : {char_count}")
    print(f"📝 Total Words      : {word_count}")
    print(f"🔥 Most Common Word : '{most_common_word}' (used {highest_freq} times)")
    print("---------------------------------\n")


# ==========================================
# Execution Walkthrough
# ==========================================
if __name__ == "__main__":
    print("--- Running Student Management Demo ---")
    # Sample structured student database
    sample_students = [
        {"name": "Alice Smith", "roll_number": 101, "marks": 92.5},
        {"name": "Bob Jones", "roll_number": 102, "marks": 78.0},
        {"name": "Charlie Day", "roll_number": 103, "marks": 88.5}
    ]
    
    # Test saving data structures to disk
    save_students(sample_students)
    
    # Test retrieving structured data from disk
    loaded_data = load_students()
    print("Retrieved Data Sample:", loaded_data[0])

    print("\n--- Running Day 3 Challenge ---")
    # Create a dummy sample text file to test the text analyzer logic
    sample_story = (
        "Python is amazing. Coding in Python is fun, quick, and powerful.\n"
        "Functions make code reusable.\n"
        "Files make data permanent."
    )
    
    with open("story.txt", "w") as f:
        f.write(sample_story)
        
    # Process the file analytics
    analyze_text_file("story.txt")
