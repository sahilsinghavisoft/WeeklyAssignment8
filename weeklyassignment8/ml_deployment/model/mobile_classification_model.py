from pydantic import BaseModel

class InputFeatures(BaseModel):
    battery_power: float
    ram: float
    px_height: float
    px_width: float
    sc_h: float
    sc_w: float
    talk_time: float
    three_g: float
    touch_screen: float
    wifi: float