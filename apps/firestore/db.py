from typing import Generator
import firebase_admin
from firebase_admin import firestore
from config import settings


class DatabaseInitialize:
    """
    Database Initialization and get data from database
    """

    def __init__(self):
        firebase_admin.initialize_app(settings.CRED)
        self.db_client = firestore.client()

    def get_collections(self) -> Generator:
        return self.db_client.collections()

    def get_documents(self, collection_name) -> list:
        return self.db_client.collection(collection_name).stream()
