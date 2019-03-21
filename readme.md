# inStep Overview

inStep is a events management application targeted towards volunteer run organizations. It was created as a full stack capstone student project by Nolan Little. It was developed for use by a non-profit dance organization. It is currently deployed in beta at www.instep.events. Any feedback via an issue or via message is welcome. To contribute to development follow start guide [here](#Development).

### Core Features

- Event Organizer (primary user) can create an "Event Blueprint " containing the events name, description, and venue/location.

- The organizer can create shifts to associate with an event including shift start and end time, description, and number of volunteers needed.

- After creating an event blueprint the organizer can create as many occurances of that event at once as they desire via the calendar feature.

- To publish an event each occurance has a unique sign-up link to distribute to your volunteer network. Organizers can copy the link with a simple button click from their dashboard.

- Organizers have access to a detail view both for event blueprints as well as event occurences. When viewing an occurence the organizer can easily see unfilled volunteer slots and current volunteers

- Volunteers (secondary user) can follow the sign-up link to a unique form for the event. They need only enter their name and an optional description and select a shift. Once they submit the form they are directed to a confirmation page and information to contact the events organizer.


At this stage volunteers are not authenticated users. The driving force behind this was to reduce the barrier to entry for volunteers. This does, however, come with trade offs. To prevent misuse the unique sign up link should only be distributed to a trusted volunteer network.

The calendar feature is an important part of the simplified workflow for event organizers. Want to create a monthly recurring event? Create the event blueprint and select each of the 12 dates from each month of the calendar view. A dynamic calendar displaying one month at a time with the ability to select dates and cycle between months makes this simple. One sumbission and the entire years worth of events is in your dashboard. You only need to revisit the app to copy the sign-up link at the appropriate time.

### Planned features

- Email notifications for event organizers containing notice about an upcoming scheduled event as well as the sign up link for convenience.

- Email confirmation and reminders for volunteers


## Development

inStep was created with the Django web app framework.

#### Basic requirements

- NPM
- Python 3.5 or newer. (deployement env will soon update to python 3.7.2)
- Django 2.1.7
- virtualenv

### Getting started
If you need in depth Python and package installation docs, head [here](https://packaging.python.org/tutorials/installing-packages/)

To begin ensure you have an updated version of Python

```
python -V
```

 To install/upgrade PIP (A package management system)
 ```
 python -m pip install --upgrade pip setuptools wheel
 ```

 To maintain a contained dev environment virtualenv is recommended

 ```
 pip install virtualenv
 ```

At this point we can setup our project. Begin by creating a base container level.
Inside this container create a clone of inStep.

```
git clone https://github.com/Nolan-Little/inStep.git
```

Next we create a virtual environment in the base container.
This command creates a virtual environmen called "env".

```
virtualenv env
```

To activate the virtual environment:
```
source env/bin/activate
```

Now we can navigate into the inStep project directory
```
cd inStep
```

To install remaining project requirements:
```
pip install -r requirements.txt
```

To continue, ensure you are in the directory containing the "manage.py" file.

Now we must create our development database:
```
python manage.py makemigrations volunteer
python manage.py migrate
```

Start development server:
```
python manage.py runserver 8000
```

You can now go to [localhost:8000](localhost:8000) to see the project.


