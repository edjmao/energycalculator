from pymodm import MongoModel, fields, EmbeddedMongoModel


class Plan(MongoModel):
    company_name = fields.CharField()
    plan_name = fields.CharField()
    publish_date = fields.DateTimeField()

    energy_charges = fields.EmbeddedDocumentField("EnergyCharges")

class EnergyCharges(EmbeddedMongoModel):
    pass