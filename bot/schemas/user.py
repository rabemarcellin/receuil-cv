from datetime import datetime
from utils import is_valid_url

class User:
    def __init__(self, name, first_name=None) -> None:
        self.name = name
        self.first_name = first_name
        self.birthday = None
        self.academic_levels = []
        self.speciality = ""
        self.last_occupation = []
        self.cv_url = ""

    def set_name(self, name=None, first_name=None):
        if name or (isinstance(name, str) and len(name.strip()) > 0):
            self.name = name
        if first_name or (isinstance(first_name, str) and len(first_name.strip()) > 0):
            self.first_name = first_name

        if name or first_name:
            return self
        else:
            return None     
    
    def set_birthday(self, date):
        '''
        Ajouter le donnée de date de naissance à l'utilisateur,
        @param data Datetime:
            la date seulement sous format JJ/MM/AAAA
        '''
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return self
        except ValueError:
            return None 
        
    def add_academic_level(self, level):
        self.academic_levels.append(f"{level}")
        return self

    def set_speciality(self, speciality):
        self.speciality = speciality
        return self

    def set_last_occupation(self, occupation):
        self.last_occupation = occupation
        return self

    def upload_cv(self, cv):
        #todo: verifier que le fichier soit une fichier pdf ou image
        return self
    
    def isready(self) -> bool:
        try:
            assert isinstance(self.name, str) and len(self.name) > 0
            assert isinstance(self.first_name, str) and len(self.first_name) > 0
            assert self.birthday is not None
            assert len(self.academic_levels) > 0
            for level in self.academic_levels:
                assert isinstance(level, str) and len(level) > 0
            assert isinstance(self.last_occupation, str) and len(self.last_occupation) > 0
            assert is_valid_url(self.cv_url)

            return True
        except:
            return False
            
            
