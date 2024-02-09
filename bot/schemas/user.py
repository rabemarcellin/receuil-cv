from os import environ as env
import cloudinary
import cloudinary.uploader
from datetime import datetime
from utils import is_valid_url

cloudinary.config(
    cloud_name=env.get('CLOUDINARY_NAME'),
    api_key=env.get('CLOUDINARY_API_KEY'),
    api_secret=env.get('CLOUDINARY_API_SECRET'),
    secure=True
)

class User:
    def __init__(self, messenger_id, name, first_name=None) -> None:
        self._messenger_id = f"{messenger_id}"
        self.name = name
        self.first_name = first_name
        self.birthday = None
        self.academic_levels = []
        self.speciality = None
        self.last_occupation = None
        self.cv_url = None

    def get_messenger_id(self):
        return self._messenger_id if self._messenger_id else None
    
    def set_messenger_id(self, messenger_id):
        self._messenger_id = messenger_id
        return self
    
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
            birthday = datetime.strptime(date, '%d/%m/%Y')
            self.birthday = birthday.timestamp()
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

    def upload_cv(self, fb_cv):
        #todo: verifier que le fichier soit une fichier pdf ou image
        try:
            # Upload the image from the URL to Cloudinary
            upload_result = cloudinary.uploader.upload(fb_cv)
            # Get the new URL from the upload result
            self.cv_url = upload_result['url']
            return self
        except Exception as e:
            print(f"Error uploading image: {e}")
            return None
    
    def is_ready(self) -> bool:
        try:
            assert isinstance(self._messenger_id, str) and len(self._messenger_id) > 0
            assert isinstance(self.name, str) and len(self.name) > 0
            assert isinstance(self.first_name, str) and len(self.first_name) > 0
            assert self.birthday is not None
            assert len(self.academic_levels) > 0
            for level in self.academic_levels:
                assert isinstance(level, str) and len(level) > 0
            assert isinstance(self.last_occupation, str) and len(self.last_occupation) > 0
            assert is_valid_url(self.cv_url)

            return True
        except Exception as error:
            print(self)
            print(error)
            return False
        
    def parse(self) -> dict:
        try:
            assert self.is_ready()
            return {
                'messenger_id': self._messenger_id,
                'name': self.name,
                'first_name': self.first_name,
                'birthday': self.birthday,
                'academic_levels': self.academic_levels,
                'speciality': self.speciality,
                'last_occupation': self.last_occupation,
                'cv_url': self.cv_url
            }
        except:
            return None
            
