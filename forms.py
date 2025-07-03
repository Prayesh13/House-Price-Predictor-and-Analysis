from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    FloatField,
    SelectField,
    SubmitField,
    BooleanField
)

from wtforms.validators import DataRequired,Length,EqualTo

class Predictor(FlaskForm):
    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    bhk = IntegerField(
        'BHK',
        validators=[DataRequired(),Length(1,2)]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )

    location = SelectField(
        'Location',
        choices=[],
        validators=[DataRequired()]
    )