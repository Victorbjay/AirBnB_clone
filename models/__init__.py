#!/usr/bin/python3
"""This module instantiates an object of class FileStorage and reloads it"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
