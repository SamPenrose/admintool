from flask_wtf import Form
from wtforms import TextField, DateField
from wtforms.validators import DataRequired, URL

from roster import Task

DATE_FORMAT = '%Y-%m-%d'

class EventForm(Form):
    id = TextField('Identifier', validators=[DataRequired()])
    startdate = DateField('Start', validators=[DataRequired()],
                          format=DATE_FORMAT)
    enddate = DateField('End', format=DATE_FORMAT)
    details_url = TextField('Details URL', validators=[URL()])

class TaskForm(Form):
    event_id = TextField('Event ID', validators=[DataRequired()])
    person_id = TextField('Person ID', validators=[DataRequired()])
    role = TextField('Role', validators=[DataRequired()])

