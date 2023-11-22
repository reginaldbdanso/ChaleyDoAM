from flask import Response, Blueprint, render_template, request, redirect, url_for, Response
from icalendar import Calendar, Event
from datetime import datetime
import uuid
from .models import Task

task = Blueprint('tasks', __name__, url_prefix='/tasks')
tasks = []

@task.route('', methods=['GET'], strict_slashes=False)
def welcome_page():
    """This method gets tasks for the user"""
    return 'Welcome to the tasks page'

@task.route('/create_task', methods=['GET', 'POST'], strict_slashes=False)
def create_task():
    """This method gets tasks for the user"""
    # tasks = []
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        due_date_str = request.form.get('due_date')

        if due_date_str is None:
            # tasks.pop()
            return "Due date is required"

        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
            due_date_date = due_date.date()
        except ValueError:
            return "Invalid due date format. Please use the format 'YYYY-MM-DD'"

        # Perform any validation if needed

        # Create a task (replace with your actual task creation logic)
        if tasks is None:
            tasks.add(Task(title=title, description=description, due_date=due_date, due_date_date=due_date_date))  
        else:
            tasks.append(Task(title=title, description=description, due_date=due_date, due_date_date=due_date_date))
        # Save the task (if you have a database, add code to save the task)
        
    """This method gets tasks for the user"""
    return render_template('index.html', tasks=tasks)

    # Perform any validation if needed

    # Create a task (replace with your actual task creation logic)
    if due_date_str:
        tasks.append(Task(title=title, description=description, due_date=due_date, due_date_date=due_date_date))
    # Save the task (if you have a database, add code to save the task)
    
    """This method gets tasks for the user"""
    return render_template('index.html', tasks=tasks)

# @task.route('/app', methods=['GET'], strict_slashes=False)
# def get_tasks():
#     tasks = []
#     """This method gets tasks for the user"""
#     return render_template('index.html', tasks=tasks)

@task.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_task(id):
    """Gets a particular task"""
    return f"Task {id}"

@task.route('/export-calendar', strict_slashes=False)
def export_calendar():
    # tasks = []  # Replace with tasks retrieval logic

    cal = Calendar()

    for task in tasks:
        event = Event()
        event.add('summary', task.title)
        event.add('description', task.description)
        # Assuming task has a 'due_date' attribute
        event.add('dtstart', task.due_date)
        event.add('dtend', task.due_date)
        event.add('dtstamp', datetime.now())
        cal.add_component(event)

    response = Response(cal.to_ical(), mimetype="text/calendar")
    response.headers["Content-Disposition"] = "attachment; filename=tasks.ics"
    tasks = []
    return response
