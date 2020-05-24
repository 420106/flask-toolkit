from flask import render_template, current_app, send_file
from . import main
from .forms import UploadForm
from ..script_mgmt.manager import Manager as Script_Manager

@main.route('/', methods = ['GET', 'POST'])
def index():
    form = UploadForm()
    task = None
    file = None
    if form.validate_on_submit():
        task = form.task.data
        file = form.file.data
        mger = Script_Manager()
        output = mger.invoke(task, file)
        file_path = current_app.config['TEMP_FILES'] + file.filename
        mger.save(output, file_path)
        return send_file(file_path)
    return render_template('index.html', form = form)
