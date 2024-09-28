class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def getHexCode(self):
        
        return '#{:02x}{:02x}{:02x}'.format(self.red, self.green, self.blue)
    
    def getBits(self):
        color_hex = self.getHexCode()
        color_bits = []
        ascii_A = ord('A')
        format_specifier_bit = 'b'
        format_specifier_4bit = '04b'
        color_dec = 0
        hex_to_dec = 87

        for i in range(1, 7):
            if ord(color_hex[i]) >= ascii_A:
                color_dec = ord(color_hex[i]) - hex_to_dec
            else:
                color_dec = int(color_hex[i])

            if color_bits == []:
                if color_dec == 0:continue
                color_bits.append(format(color_dec, format_specifier_bit))            
            else:
                color_bits.append(format(color_dec, format_specifier_4bit))
        
        return ''.join(color_bits)

    def getColorShade(self):
        max_value = max([self.red, self.green, self.blue])
        max_list = []

        if self.red == max_value:
            max_list.append("red")
        if self.green == max_value:
            max_list.append("green")
        if self.blue == max_value:
            max_list.append("blue")
        
        if len(max_list) == 3:
            return "grayscale"
        else:
            return max_list[0]

color1 = RGB(0, 153, 255)

print(color1.getHexCode())

print(color1.getBits())

print(color1.getColorShade())


color2 = RGB(255, 255, 204)

print(color2.getHexCode())

print(color2.getBits())

print(color2.getColorShade())


color3 = RGB(0, 87, 0)

print(color3.getHexCode())

print(color3.getBits())

print(color3.getColorShade())


gray = RGB(123, 123, 123)

print(gray.getHexCode())

print(gray.getBits())

print(gray.getColorShade())