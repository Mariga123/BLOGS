from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.', validators=[Required()])
    submit = SubmitField('Save')


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category',
                           choices=[('Politics', 'politics'), ('Relationship', 'relationships'), ('Sports', 'sports')],
                           validators=[Required()])
    post = TextAreaField('Your Blog', validators=[Required()])
    submit = SubmitField('POST')


class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Comment')
    
class SubscriberForm(FlaskForm):
    email = StringField('Your Email Address')
    name = StringField('Enter your name',validators = [Required()])
    submit = SubmitField('Subscribe')