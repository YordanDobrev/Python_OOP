from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        searched_category = next(filter(lambda c: c.id == category_id, self.categories))
        searched_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        searched_topic = next(filter(lambda t: t.id == topic_id, self.topics))
        searched_topic.storage_folder = new_storage_folder
        searched_topic.topic = new_topic

    def edit_document(self, document_id: int, new_file_name: str):
        searched_document = next(filter(lambda d: d.id == document_id, self.documents))
        searched_document.file_name = new_file_name

    def delete_category(self, category_id):
        searched_category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(searched_category)

    def delete_topic(self, topic_id):
        searched_topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(searched_topic)

    def delete_document(self, document_id):
        searched_document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(searched_document)

    def get_document(self, document_id):
        searched_document = next(filter(lambda d: d.id == document_id, self.documents))
        return searched_document

    def __repr__(self):
        result = []

        for doc in self.documents:
            result.append(str(doc))

        return "\n".join(result)
