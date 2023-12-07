# Todo-list

## Task - todo list is consist of tasks. Each task should have fields for:
- content - describes what you should do.
- datetime, when a task was created
- optional deadline datetime if a task should be done until some datetime
- the boolean field that marks if the task is done or not
- tags that are relevant for this task

## Tag - a tag symbolizes the theme of the task and consists only of a name.

# Installation

Create venv and install requirements


```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

## Configuration

### Environment Variables

This project uses environment variables for configuration. To set up the required variables, follow these steps:

1. Create a new `.env` file in the root directory of the project.

2. Copy the contents of the `.env_sample` file into `.env`.

3. Replace the placeholder values in the `.env` file with the actual values specific to your environment.

## Usage

- To apply migrations to the database use command:
```
python manage.py migrate
```
- Use the following command to load prepared data from fixture:
```
python manage.py loaddata todo_list_data.json
```

- To run server use command:
```
python manage.py runserver
```
- To run tests use command:
```
python manage.py test
```
