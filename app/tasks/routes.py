from flask import Response, Blueprint, render_template, request, redirect, url_for, Response, jsonify
from icalendar import Calendar, Event
from datetime import datetime
import uuid
from .models import Task

task = Blueprint('tasks', __name__, url_prefix='/')
tasks = []

@task.route('', methods=['GET'], strict_slashes=False)
def welcome_page():
    """This method gets tasks for the user"""
    return render_template('welcome.html')

# @task.route('/create_task/<id>', methods=['GET', 'POST', 'DELETE'], strict_slashes=False)
@task.route('/create_task', defaults={'id': None}, methods=['GET', 'POST'], strict_slashes=False)
@task.route('/create_task/<id>', methods=['DELETE', 'PUT'], strict_slashes=False)
def create_task(id=None):
    """This method gets tasks for the user"""
    if request.method == 'GET':
        pass
        return render_template('app.html', tasks=tasks)
    # tasks = []
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        due_date_str = request.form.get('due_date')

        if due_date_str is None:
            return "Due date is required"

        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
            due_date_date = due_date.date()
        except ValueError:
            return "Invalid due date format. Please use the format 'YYYY-MM-DD'"

        # Perform any validation if needed

        # Create a task (replace with your actual task creation logic)
        if tasks is None:
            tasks.add(Task(title=title, description=description, due_date=due_date, due_date_date=due_date_date).to_dict())  
        elif due_date_str:
            tasks.append(Task(title=title, description=description, due_date=due_date, due_date_date=due_date_date).to_dict())
        # Save the task (if you have a database, add code to save the task)
        
        """This method gets tasks for the user"""
        return redirect(url_for('tasks.create_task'))

    elif request.method == 'DELETE':
        """Deletes a particular task"""
        for task in tasks:
            if task['id'] == id:
                print(task)
                print(task['id'])
                print(id)
                print(task['id'] == id)
                tasks.remove(task)
                return redirect(url_for('tasks.create_task')), 

        return "Task not found", 404
    
    elif request.method == 'PUT':
        """Edits a particular task"""
        for task in tasks:
            if task['id'] == id:
                print(task)
                print(task['id'])
                print(id)
                print(task['id'] == id)
                new_title = request.form.get('mtitle')
                print(new_title)
                new_description = request.form.get('mdescription')
                print(new_description)
                new_date = request.form.get('mdue_date')
                print(new_date)
                task['title'] = new_title
                task['description'] = new_description
                task['due_date'] = new_date
                task['due_date_date'] = new_date
                task['updated_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                print(task)
                return redirect(url_for('tasks.create_task')) 

        return "Task not found", 404
 

@task.route('/export-calendar', strict_slashes=False)
def export_calendar():
    # tasks = []  # Replace with tasks retrieval logic
    global tasks
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


