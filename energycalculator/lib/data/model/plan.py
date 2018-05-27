from pymodm import MongoModel, fields, EmbeddedMongoModel


class Plan(MongoModel):
    company_name = fields.CharField()
    plan_name = fields.CharField()
    publish_date = fields.DateTimeField()
    currency = fields.CharField()

    energy_charges = fields.EmbeddedDocumentField("Charges")
    delivery_charges = fields.EmbeddedDocumentField("Charges")

class Charges(EmbeddedMongoModel):
    base = fields.IntegerField()
    usage_schedule = fields.EmbeddedDocumentListField("UsageSchedule")

class UsageSchedule(EmbeddedMongoModel):
    lower = fields.IntegerField()
    upper = fields.IntegerField()
    fixed_charge = fields.IntegerField()
    per_kwh_charge = fields.Decimal128Field()
