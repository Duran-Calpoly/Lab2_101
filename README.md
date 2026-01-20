# CSC 101: 6-Day Python Fundamentals Lab

Welcome to your Lab Series! This week is designed to help you master Python logic and unit testing. Instead of just writing code, you will learn to verify it using the `unittest` framework.
---
> [!IMPORTANT]
> **Final Step:** Be sure to **commit and push** your code to GitHub/GitLab after every lab. This ensures your changes are saved and your instructor can see your progress!
---

## Day 1: Functions and Unit Testing

**Concepts:** Parameter passing and the `unittest` framework.

**Your Task:** For this lab, the implementation code is provided to you in `lab2_1.py`. Your job is to write the test suite in `test_1.py`.

You must write **3 separate test methods** for each function (6 methods total). Each method should contain one `assertEqual` or `assertAlmostEqual`.

* **Function 1:** `get_first_alphabetically(char1, char2)`
* Accepts two single-character strings.
* Returns the character that appears first in the alphabet.


* **Function 2:** `calculate_triangle_area(base, height)`
* Accepts two numbers (base and height).
* Returns the area of the triangle ().
* **Note:** Use `assertAlmostEqual` for this function to handle floating-point precision.



---

## Day 2: Lists and Indexing

**Concepts:** List slicing, negative indexing, and floor division.

* **Function 1:** `reverse_list(data)`
* Returns a new list with the elements in reverse order.


* **Function 2:** `get_ends(data)`
* Returns a new list containing only the first and last elements.


* **Function 3:** `get_middle(data)`
* Returns the middle element.
* **Constraint:** If the list has an even number of elements, use floor division to "round down" to the lower middle index.



---

## Day 3: String Manipulation

**Concepts:** String concatenation, ASCII comparison, and slicing.

* **Function 1:** `alphabetize_two(word1, word2)`
* Accepts two strings and returns them as a single string, separated by a space, in alphabetical order.
* **Constraint:** Do **not** use `.sort()`, `.join()`, or `.lower()`.


* **Function 2:** `repeat_string(text, n)`
* Accepts a string and an integer . Returns the string repeated  times.


* **Function 3:** `swap_ends(text)`
* Returns a new string where the first and last characters are swapped.



---

## Day 4: For Loops and Logic

**Concepts:** The accumulator pattern and multi-pass iteration.

* **Function 1:** `get_evens(n)`
* Returns a list of all even numbers from 0 up to and including .


* **Function 2:** `find_second_largest(numbers)`
* Returns the second-largest number in the list.
* **Constraint:** You must iterate through the list **twice** (Pass 1: find max; Pass 2: find largest number smaller than that max).


* **Function 3:** `count_vowels(text)`
* Returns the total count of vowels (a, e, i, o, u) regardless of case.



---

## Day 5: Dictionaries

**Concepts:** Key-Value pairs and dictionary population.

* **Function 1:** `map_word_lengths(words)`
* Accepts a list of strings.
* Returns a dictionary where each **key** is a word from the list and its **value** is the length of that word.



---

## Day 6: Advanced Iteration

**Concepts:** Nested loops, List Comprehensions, and the `zip` function.

* **Function 1:** `multiplication_table()`
* Uses **nested loops** to return a single "flat" list of all products in a  table (from  up to ).


* **Function 2:** `get_multiples_of_three(numbers)`
* Returns a new list of all numbers greater than 0 that are multiples of 3.
* **Constraint:** You **must** use a **List Comprehension**.


* **Function 3:** `merge_lists(list1, list2)`
* Uses the `zip` function to return a list of tuples pairing the elements from two lists together.



---


