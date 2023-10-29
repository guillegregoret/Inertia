from pymongo import MongoClient

client = MongoClient("mongodb+srv://guillegregoret:mGnbCsQoouBvpkmE@inertia-cluster.3tlzmy6.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]