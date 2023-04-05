from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap4
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import pandas as pd

# Create server app
app = Flask(__name__)
app.secret_key = "some secret"

# add Bootstrap for styling
bootstrap = Bootstrap4(app)

class CafeForm(FlaskForm):
    cafes = StringField(label="cafe name", validators=[DataRequired()])
    submit = SubmitField(label="submit")

class AddForm(FlaskForm):
    cafe_name = StringField(label="cafe name", validators=[DataRequired()], render_kw={"style": "width: 400px;"})
    map_link = StringField(label="map link", validators=[DataRequired()], render_kw={"style": "width: 400px;"})
    open_time = StringField(label="open time", validators=[DataRequired()], render_kw={"style": "width: 400px;"})
    close_time = StringField(label="cafe name", validators=[DataRequired()], render_kw={"style": "width: 400px;"})
    coffee_rating = SelectField(label="coffee rating", choices=[('1', '✘'),
                                                                ('2', '☕️'),
                                                                ('3', '☕️☕️'),
                                                                ('4', '☕️☕️☕️'),
                                                                ('5', '☕️☕️☕️☕️')],
                                                            render_kw={"style": "width: 400px;"})
    wifi_rating = SelectField(label="wifi rating", choices=[('1', '✘'),
                                                            ('2', '💪️'),
                                                            ('3', '💪️💪️'),
                                                            ('4', '💪️💪️💪️'),
                                                            ('5', '💪️💪️💪️💪️')],
                                                            render_kw={"style": "width: 400px;"})
    power_rating = SelectField(label="power rating", choices=[('1', '✘'),
                                                              ('2', '🔌'),
                                                              ('3', '🔌🔌'),
                                                              ('4', '🔌🔌🔌'),
                                                              ('5', '🔌🔌🔌🔌')],
                                                            render_kw={"style": "width: 400px;"})
    submit = SubmitField(label="Submit", render_kw={"style": "margin-top: 2%;"})

# Set up the home page
@app.route("/")
def home():
    return render_template('index.html')

#
@app.route("/cafes", methods=['GET', 'POST'])
def cafes():
    form = CafeForm()
    # Load CSV file into a pandas DataFrame
    csv_data = pd.read_csv('cafe-data.csv')
    list_of_rows = []
    # Iterate over each row in the DataFrame
    for index, row in csv_data.iterrows():
        # Access the values in each row using column names
        list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route("/add", methods=['GET', 'POST'])
def add_store():
    form = AddForm()
    print(form.cafe_name.data)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("received button feedback")
        print(form.cafe_name.data)
        print(form.open_time.data)
        return render_template('add.html')
    return render_template('add.html', form=form)

if (__name__ == "__main__"):
    app.run(debug=True)