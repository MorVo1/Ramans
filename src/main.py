from PIL import Image
import components

class Raman:
    
    def generate_random(self, save_path: str = "raman.png") -> None:
        base, tip = components.BaseComponent(), components.TipsComponent()
        generated: Image.Image = Image.alpha_composite(base.get(), tip.get())
        for component in components.AbstractComponent.__subclasses__():
            generated = Image.alpha_composite(generated, component().get())
        generated.save(save_path)
