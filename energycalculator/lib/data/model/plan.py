from mongoengine import Document, StringField, DateTimeField, IntField, ListField, EmbeddedDocumentField, \
    EmbeddedDocument, DecimalField


class UsageSchedule(EmbeddedDocument):
    lower = IntField()
    upper = IntField()
    fixed_charge = IntField()
    per_kwh_charge = DecimalField()


class Charges(EmbeddedDocument):
    base = IntField()
    usage_schedule = ListField(EmbeddedDocumentField(UsageSchedule))


class Plan(Document):
    company_name = StringField()
    plan_name = StringField()
    publish_date = DateTimeField()
    currency = StringField()
    energy_charges = EmbeddedDocumentField(Charges)
    delivery_charges = EmbeddedDocumentField(Charges)
