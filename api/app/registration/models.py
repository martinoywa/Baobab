from app import db
from datetime import date


class Offer(db.Model):

    __tablename__ = "offer"

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(),  db.ForeignKey("app_user.id"), nullable=False)
    event_id = db.Column(db.Integer(), db.ForeignKey("event.id"), nullable=False)
    offer_date = db.Column(db.DateTime(), nullable=False)
    expiry_date = db.Column(db.DateTime(), nullable=False)
    payment_required = db.Column(db.Boolean(), nullable=False)
    travel_award = db.Column(db.String(50), nullable=False)
    accommodation_award = db.Column(db.String(50), nullable=True)
    rejected = db.Column(db.String(50), nullable=True)
    rejected_reason = db.Column(db.String(50), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self,
                 user_id,
                 event_id,
                 offer_date,
                 expiry_date,
                 payment_required,
                 travel_award,
                 accommodation_award,
                 rejected,
                 rejected_reason,
                 updated_at):
        self.user_id = user_id
        self.event_id = event_id
        self.offer_date = offer_date
        self.expiry_date = expiry_date
        self.payment_required = payment_required
        self.travel_award = travel_award
        self.accommodation_award = accommodation_award
        self.rejected = rejected
        self.rejected_reason = rejected_reason
        self.updated_at = updated_at


class RegistrationForm(db.Model):

    __tablename__ = "registration_form"

    id = db.Column(db.Integer(), primary_key=True)
    event_id = db.Column(db.Integer(), db.ForeignKey("event.id"), nullable=False)

class RegistrationSection(db.Model):

    __tablename__ = "registration_section"

    id = db.Column(db.Integer(), primary_key=True)
    registration_form_id = db.Column(db.Integer(), db.ForeignKey("registration_form.id"), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    order = db.Column(db.Integer(), nullable=False)
    show_for_travel_award = db.Column(db.Boolean(), nullable=False)
    show_for_accommodation_award = db.Column(db.Boolean(), nullable=False)
    show_for_payment_required = db.Column(db.Boolean(), nullable=False)


class RegistrationQuestion(db.Model):

    __tablename__ = "registration_question"

    id = db.Column(db.Integer(), primary_key=True)
    registration_form_id = db.Column(db.Integer(), db.ForeignKey("registration_form.id"), nullable=False)
    section_id = db.Column(db.Integer(), db.ForeignKey("registration_section.id"), nullable=False)
    type = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    headline = db.Column(db.String(), nullable=False)
    placeholder = db.Column(db.String(), nullable=False)
    validation_regex = db.Column(db.String(), nullable=True)
    validation_text = db.Column(db.String(), nullable=True)
    order = db.Column(db.Integer(), nullable=False)
    options = db.Column(db.JSON(), nullable=True)
    is_required = db.Column(db.Boolean(), nullable=False)

# Registration


class Registration(db.Model):
    __tablename__ = "registration"

    id = db.Column(db.Integer(), primary_key=True)
    offer_id = db.Column(db.Integer(), db.ForeignKey("offer.id"), nullable=False)
    registration_form_id = db.Column(db.Integer(), db.ForeignKey("registration_form.id"), nullable=False)
    confirmed = db.Column(db.Boolean(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=True)
    confirmation_email_sent_at = db.Column(db.DateTime(), nullable=True)

    def __init__(self, offer_id, registration_form_id, confirmed=False, confirmation_email_sent_at=None):
        self.offer_id = offer_id
        self.registration_form_id = registration_form_id
        self.confirmed = confirmed
        self.created_at = date.today()
        self.confirmation_email_sent_at = confirmation_email_sent_at

    def confirm(self):
        self.confirmed = True
        self.confirmation_email_sent_at = date.today()


class RegistrationAnswer(db.Model):
    __tablename__ = "registration_answer"

    id = db.Column(db.Integer(), primary_key=True)
    registration_id = db.Column(db.Integer(), db.ForeignKey('registration.id'), nullable=False)
    registration_question_id = db.Column(db.Integer(), db.ForeignKey('registration_question.id'), nullable=False)
    value = db.Column(db.String(), nullable=False)


