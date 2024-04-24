from ml_deployment.config.v1 import BaseSettingsWrapper
class MongoConfig(BaseSettingsWrapper):
    mongo_host: str = "localhost"
mongo_config = MongoConfig()