# Command-Line Task Manager
### [Video Demo](https://youtu.be/frOoJK1mgQg)
### Allows users to add, edit, remove, and edit tasks. Tasks also have a due date and due time. Tasks are stored in a csv file. Uses regular expressions in order to validate user input and reprompts in case of invalid input. Uses mm/dd/yyyy and both 24 hour and 12 hour time formats.
# Requirements
### Requires the `tabulate` module. Install with:
```pip install tabulate```
### Testing requires the `pytest` module. Install with:
```pip install pytest```
# Libraries Used
### `csv` was used to read from and write to the file where tasks are stored. `re` was used to validate user input. `black` was used to format the file. `tabulate` was used to present options and task in an aesthetic manner. `csv` and `re` are built into python.
# Usage
### Go into the `project` folder
```cd project```
### Execute `project.py`
```python project.py```
### For testing (make sure pytest is installed):
```pytest test_project.py```
# Thoughts
### I originially went in with the idea of making a to-do item its own class with attributes of task, date, and time. However, I soon realized it would be mouch easier to just store those things as dictionaries since that would allow easier use of the csv module. However, I still implemented the input verification that was in that class.
### Originially and edit function was not supposed to be in there. However, I figured my program would be to simple without. Also, it would be annoying typing in a new task and deleting the old one. Doing this is what prompted me to make the user verification its own function.
### Testing was hard since my functions didn't take parameters. But I learned somethings about pytest and it worked out.
### CS50P is the first HarvardX class I've taken. I plan to continue on with CS50x and the rest of them. It's a bit of a bummer that CS50G is being shut down; I was looking forward to doing that one. To anyone thinking about taking a CS50 class: do it. It's tough at times and the lectures can be really long, but if a kid just out of middle school can do it, you can to.
