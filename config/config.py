from utils.env_utils import load_config
from pydantic import BaseModel


class Config(BaseModel):
    db_url: str
    root_node_title: str
    db_url_test: str
    # ...

    @classmethod
    def load_config(cls) -> 'Config':
        data_env = load_config()

        return Config(
            db_url=data_env['DB_URL'],
            db_url_test=data_env['DB_URL_TEST'],
            root_node_title=data_env['ROOT_NODE_TITLE'],
            # ...
        )


config = Config.load_config()


def get_config():
    return config
