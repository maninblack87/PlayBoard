# User.py
import tkinter as tk
from Buildings.Building import Building
from Units.Unit import Unit

class User:

    def __init__(self, name):
        self.name : str = None
        self.user_building = []
        self.user_unit = []