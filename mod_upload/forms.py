from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from wtforms.validators import DataRequired

class FileUploadForm(FlaskForm):
    file = FileField(label='Upload File',validators=[DataRequired()])
    submit = SubmitField(label='Upload')
