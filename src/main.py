import code
from PIL import Image
from random import choice
from os import listdir
from os import chdir


class Raman:
    def __init__(self):
        self.base_path = '../images/base.png'
        self.tips_path = '../images/tips'
        self.faces_path = '../images/faces'
        self.shirts_path = '../images/shirts'
        self.pants_path = '../images/pants'
        self.boots_path = '../images/boots'
        self.code = None

    def __call__(self):
        base = Image.open(self.base_path)
        tip = Image.open(f'../images/tips/{choice(listdir(self.tips_path))}')
        face = Image.open(
            f'../images/faces/{choice(listdir(self.faces_path))}')
        shirt = Image.open(
            f'../images/shirts/{choice(listdir(self.shirts_path))}')
        pants = Image.open(
            f'../images/pants/{choice(listdir(self.pants_path))}')
        boots = Image.open(
            f'../images/boots/{choice(listdir(self.boots_path))}')

        generated = Image.alpha_composite(base, tip)
        generated = Image.alpha_composite(generated, face)
        generated = Image.alpha_composite(generated, shirt)
        generated = Image.alpha_composite(generated, pants)
        generated = Image.alpha_composite(generated, boots)

        generated.save('out.png')

        code_parts = [
            tip.filename.split('/')[3].strip(".png"),
            face.filename.split('/')[3].strip(".png"),
            shirt.filename.split('/')[3].strip(".png"),
            pants.filename.split('/')[3].strip(".png"),
            boots.filename.split('/')[3].strip(".png")
        ]
        self.code = ';'.join(code_parts)


raman = Raman()


def generate_raman():
    raman()


def get_previous_code() -> str:
    return raman.code


if __name__ == '__main__':
    generate_raman()
    print(get_previous_code())
