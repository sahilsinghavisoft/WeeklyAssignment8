import mongoengine
class PredictionData(mongoengine.Document):
    battery_power = mongoengine.IntField(required=True)
    fc = mongoengine.IntField(required=True)
    int_memory = mongoengine.IntField(required=True)
    mobile_wt = mongoengine.IntField(required=True)
    n_cores = mongoengine.IntField(required=True)
    pc = mongoengine.IntField(required=True)
    ram = mongoengine.IntField(required=True)
    talk_time = mongoengine.IntField(required=True)
    sc_size = mongoengine.FloatField(required=True)
    pixels = mongoengine.IntField(required=True)
    
    prediction = mongoengine.StringField()
    

metadata = {"collection": "mobileprice"}
