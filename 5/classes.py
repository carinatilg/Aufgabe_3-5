from datetime import datetime
import json


class Person():
    def __init__(self, id, date_of_birth, firstname, lastname, picture_path, ekg_tests):
        self.id = id
        self.date_of_birth = date_of_birth
        self.firstname = firstname
        self.lastname = lastname
        self.picture_path = picture_path
        self.ekg_tests = ekg_tests

    def calc_age(self):
        current_year = datetime.now().year
        age = current_year - self.date_of_birth
        return age
    
    def calc_max_heart_rate(self):
        max_heart_rate = 220 - self.age 
        return max_heart_rate
    
    def load_by_id(self):

