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
        filename = current_app.config['TEMP_FILES'] + '\\' + file.filename
        filename_ = mger.save(output, filename)
        return send_file(filename_, as_attachment = True)
        # How to remove the temp file after the return
    return render_template('index.html', form = form)
