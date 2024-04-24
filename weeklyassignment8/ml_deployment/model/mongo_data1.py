import mongoengine
class PredictionData(mongoengine.Document):
    battery_power = mongoengine.FloatField(required=True)
    ram = mongoengine.FloatField(required=True)
    px_height = mongoengine.FloatField(required=True)
    px_width = mongoengine.FloatField(required=True)
    sc_h = mongoengine.FloatField(required=True)
    sc_w = mongoengine.FloatField(required=True)
    talk_time = mongoengine.FloatField(required=True)
    three_g = mongoengine.FloatField(required=True)
    touch_screen = mongoengine.FloatField(required=True)
    wifi = mongoengine.FloatField(required=True)
    prediction = mongoengine.StringField()

metadata = {"collection": "mobileprice"}
