from os import listdir
from random import choice
from PIL import Image


class AbstractComponent:

    _load_path: str = None

    def get(self) -> Image.Image:
        return Image.open(f'{self._load_path}/{choice(listdir(self._load_path))}')


class BaseComponent(AbstractComponent):

    _load_path: str = '../images/base.png'

    def get(self) -> Image:
        return Image.open(self._load_path)


class TipsComponent(AbstractComponent):
    
    _load_path: str = '../images/tips'


class FacesComponent(AbstractComponent):

    _load_path: str = '../images/faces'


class ShirtsComponent(AbstractComponent):

    _load_path: str = '../images/shirts'


class PantsComponent(AbstractComponent):
    
    _load_path: str = '../images/pants'