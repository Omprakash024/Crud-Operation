from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    format = StringField('format', validators=[DataRequired()])
    num_pages = StringField('pages', validators=[DataRequired()])
    submit = SubmitField('save')

class CreateBookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    avg_rating = StringField('ratings', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])
    format = StringField('format', validators=[DataRequired()])
    num_pages = IntegerField('pages', validators=[DataRequired()])
    pub_id = IntegerField('PublisherId', validators=[DataRequired()])
    submit = SubmitField('create')