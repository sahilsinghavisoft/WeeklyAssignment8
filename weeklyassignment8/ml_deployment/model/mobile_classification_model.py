from pydantic import BaseModel

class InputFeatures(BaseModel):
    battery_power: int
    fc: int
    int_memory: int
    mobile_wt: int
    n_cores: int
    pc: int
    ram: int
    talk_time: int
    sc_size: float
    pixels: int