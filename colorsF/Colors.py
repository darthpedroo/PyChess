class Colors:
    def __init__(self):
        self.ColorsPallete = [
    [[0, 0, 0], [255, 255, 255]],   # Classic Black and White
    [[0, 0, 0], [255, 0, 0]],       # Traditional Red and White
    [[222, 184, 135], [139, 69, 19]],  # Classic Wood Theme
    [[173, 216, 230], [25, 25, 112]],   # Modern Blue Theme
    [[173, 216, 230], [0, 128, 0]],      # Elegant Green Theme
    [[255, 228, 196], [205, 133, 63]],  # Sandy Brown Theme
    [[240, 255, 240], [34, 139, 34]],   # Forest Green Theme
    [[255, 250, 205], [139, 69, 19]],   # Beige and Saddle Brown
    [[255, 239, 219], [210, 105, 30]],  # Peach Puff and Chocolate Brown
    [[255, 248, 220], [139, 101, 8]]    # Cornsilk and Dark Goldenrod
    ]

    def get_ColorPallete(self,indexOfPallete,colModule):
        return self.ColorsPallete[indexOfPallete][colModule]
        
        

    
