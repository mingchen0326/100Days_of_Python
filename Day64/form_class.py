from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create form class for edit movie
class EditForm(FlaskForm):
    movie_rating = StringField(label='movie_rating', validators=[DataRequired()], render_kw={"style": "width: 200px;"})
    movie_review = StringField(label='movie_review', validators=[DataRequired()], render_kw={"style": "width: 200px;"})
    edit_submit = SubmitField(label='Done')


# Create WTF form to add movie
class AddForm(FlaskForm):
    movie_title = StringField(label='movie_title', validators=[DataRequired()], render_kw={"style": "width: 200px;"})
    add_submit = SubmitField(label='Add Movie')
