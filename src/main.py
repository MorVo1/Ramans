from PIL import Image
import components

class Raman:
    
    def generate_raman(self, save_path: str = "out.png") -> None:
        generated = components.BaseComponent().get()
        for component in components.AbstractComponent.__subclasses__():
            generated = Image.alpha_composite(generated, component().get())
        generated.save(save_path)
