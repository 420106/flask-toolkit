from flask_wtf import FlaskForm
from wtforms import SelectField, FileField, SubmitField
from wtforms.validators import DataRequired
from ..script_mgmt.manager import Manager as Script_Manager

class UploadForm(FlaskForm):
    mger = Script_Manager()
    task = SelectField('Task', choices = mger.script_list, validators = [DataRequired()])
    file = FileField(validators = [DataRequired()])
    submit = SubmitField()
