import os
import settings

from pymongo import MongoClient


class Index(type):
    """
    Metaclass to create indexes in MongoDB.
    Args:
        type (type): Metaclass.
    """

    def __init__(cls, *args, **kwargs):
        if hasattr(cls, "index"):
            cls.get_instance().create_index(cls.index, unique=True)
        super().__init__(*args, **kwargs)

class BaseConnection:
    connection = MongoClient(
        settings.MONGO_URL,
        tlsAllowInvalidCertificates=True,
        retryWrites=False,
        tlsCAFile="mongo.pem",
        tls=True,
        directConnection=True,
    )

class BaseDB(BaseConnection, metaclass=Index):
    database = settings.DATABASE_ENVIRONMENT

database = BaseDB.connection[BaseDB.database]
