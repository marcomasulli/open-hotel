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

class UserForm(Form):
    email=StringField()
    password=PasswordField()
    is_active=BooleanField()
    submit=SubmitField()


class HotelForm(Form):
    hotel_name = StringField()
    hotel_address = StringField()
    hotel_country = StringField()
    hotel_province = StringField()
    hotel_location = StringField()
    hotel_rooms = IntegerField(validators=[Optional()])
    hotel_latitude = StringField(validators=[Optional()])
    hotel_longitude = StringField(validators=[Optional()])
    hotel_phone = StringField()
    hotel_email = StringField()
    hotel_contact_person = StringField(validators=[Optional()])
    hotel_contact_phone = StringField(validators=[Optional()])
    hotel_contact_email = StringField(validators=[Optional()])
    hotel_code = StringField(validators=[Optional()])
    hotel_chain_code = StringField(validators=[Optional()])
    hotel_brand_code = StringField(validators=[Optional()])
    hotel_city_code = StringField(validators=[Optional()])
    is_active = BooleanField()
    submit = SubmitField()

class HotelFormEdit(HotelForm):
    hotel_id = IntegerField()

class HotelInfoForm(Form):
    hotel_id = IntegerField()
    currency_code = StringField()
    currency_code_decimal_places = IntegerField()
    hotel_pms_system = StringField(validators=[Optional()])
    location_category = StringField(validators=[Optional()])
    segment_category = StringField(validators=[Optional()])
    hotel_category = StringField(validators=[Optional()])
    architectural_style = StringField(validators=[Optional()])
    submit=SubmitField()

class HotelInfoEdit(HotelInfoForm):
    info_id = IntegerField()
