class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def __str__(self):
    return "Rectangle(width={0}, height={1})".format(self.width, self.height)

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return '\n'.join(["*" * self.width for i in range(self.height)]) + '\n'

  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)



class Square(Rectangle):
  def __init__(self, side):
    self.set_side(side)

  def __str__(self):
    return "Square(side={0})".format(self.width)

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def set_side(self, side):
    self.width = side
    self.height = side