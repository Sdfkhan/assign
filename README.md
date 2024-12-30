Selenium Search Functionality Test
This repository contains a Selenium test script to validate the search functionality on the Selenium Playground website.
Script Overview
The script performs the following actions:
1.	Navigates to the "Table Sort and Search Demo" page of Selenium Playground.
2.	Searches for the term "New York" in the search box.
3.	Validates that the table displays 5 rows related to the search.
4.	Confirms the total entry text matches the expected output.
   
File Structure
•	qa_selenium_test.py: Contains the Selenium test script using pytest framework.
•	README.md: Documentation for understanding and setting up the project.

Prerequisites
Before running the script, ensure you have the following installed:
1.	Python 3.x
2.	Google Chrome Browser
3.	ChromeDriver (compatible with your Chrome version)
4.	pip (Python package manager)
   
Setup Instructions
1.	Clone the repository:
2.	git clone <repository-url>
cd <repository-folder>
3.	Install the required dependencies:
pip install selenium pytest
4.	Update the ChromeDriver path in qa_selenium_test.py:
service = Service("path/to/chromedriver")  # Replace with your actual chromedriver path

Running the Test
Execute the test script using pytest:
pytest -v --capture=no --disable-warnings qa_selenium_test.py

Expected Output
The test validates:
1.	The search results show 5 rows for the term "New York."
2.	The total entries text reads: Showing 1 to 5 of 5 entries (filtered from 24 total entries).
Notes
•	Ensure ChromeDriver is added to your system PATH or specify the full path in the script.
•	The test runs in headless mode by default. You can remove the --headless argument in the script to see the browser.


