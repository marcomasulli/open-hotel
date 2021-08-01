from flask_wtf import Form, FlaskForm
from wtforms.fields import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    DecimalField,
    HiddenField,
    IntegerField,
    TextAreaField,
    SelectField,
    DateField,
    FileField,
    FormField,
)
from wtforms.validators import (
    DataRequired,
    InputRequired,
    Email,
    Optional,
    ValidationError,
)

class AgentForm(Form):
    agent_name=StringField()
    agent_address=StringField()
    agent_country=StringField()
    agent_province=StringField()
    agent_location=StringField()
    agent_phone=StringField()
    agent_email=StringField(validators=[Email()])
    agent_contact_person=StringField()
    agent_type=StringField()
    agent_model=SelectField(choices=[('', 'Select an Agent Model')] + [(1, 'Commission'), (2, 'Net')], validators=[Optional()])
    agent_commission=DecimalField(validators=[Optional()])
    agent_discount=DecimalField(validators=[Optional()])
    is_active=BooleanField()
    submit=SubmitField()