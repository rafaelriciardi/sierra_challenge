# **AI Engineer Take-Home Assessment**

This document outlines the analysis and improvements made to the initial code provided for the take-home assessment.

## **1. Identified Problems with the Original Code**

* The temperature is set to a high value, which can make the model less deterministic and predictable.
* There is a lack of test cases. We only have one test for the True class and none for the False one.
* The prompt is not wrong, but it could be improved to enhance accuracy and the expected outputs.
* The code is not fail safe. It will break if anything goes wrong, such as API unavailability or bad responses from the model.
* Thinking as system integration, the return of the model as string forces a transformation every time its values need to be accessed

---

## **2. Implemented Improvements**

* [Done] Adjust the temperature to a lower value, making the model more deterministic and predictable, which is very important for this task.
* [Done] Change the functions return to a json object to be used in the next steps of the system.
* [Done] Create case tests, with real examples, containing spams and not spams content.
* [Done] Restructure the prompt with clearer and more strict instructions, making it less prone to hallucination.
* [Done] Add the few-shot technique to the prompt, providing a few examples and their expected outputs.
* [Done] Increase max tokens to ensure the full reasoning is returned
* [Done] Add a fallback option to another LLM service, enhancing the availability of the solution itself.
* Use a retry mechanism to ensure the output is as expected.
* [Done] Implement exception handling to act when the input is not as expected and when other kinds of errors hit the application, preventing it from breaking.
 

---

## **Project Overview**

From all the ideas I listed above, I was able to implement almost all of them in the given time. Let's dive into each of them in more detail.

To solve the identified issues and implement these improvements, the project was structured into three main files:

* `solution.py`: This file contains the core logic for the solution, including the source code to classify an email as spam or not.
* `test_cases.json`: A JSON file that I created manually by extracting real examples from my email, containing both spam and non-spam content.
* `test_spam_classifier.py`: A script to test all the cases from the JSON file against the functions developed in `solution.py`.