import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_heart_image(color, size=(80, 80)):
    heart = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(heart)
    
    width, height = size
    left = width // 4
    right = 3 * width // 4
    top = height // 4
    bottom = height
    
    draw.polygon([(width // 2, height),
                  (left, height // 2),
                  (right, height // 2)],
                 fill=color)
    
    draw.ellipse([left - width // 4, top - height // 4,
                  left + width // 4, top + height // 4],
                 fill=color)
    
    draw.ellipse([right - width // 4, top - height // 4,
                  right + width // 4, top + height // 4],
                 fill=color)
    
    return heart

# Create a blank image with white background
width, height = 800, 800
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Add black and white striped background
stripe_height = 50
for i in range(0, height, stripe_height * 2):
    draw.rectangle([0, i, width, i + stripe_height], fill='black')

# Add circle in the center
circle_center = (width // 2, height // 2)
circle_radius = 200
draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius], fill='black')

# Use the default font
font = ImageFont.load_default()

# Add "Happy Birthday" text in the center of the circle
text = "Happy\nBirthday\nMR.Bharath"
text_bbox = draw.multiline_textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = circle_center[0] - text_width // 2
text_y = circle_center[1] - text_height // 2
draw.multiline_text((text_x, text_y), text, fill='white', font=font, align="center")

# Create heart images
heart_red = create_heart_image('red')
heart_gold = create_heart_image('gold')

hearts = [heart_red, heart_gold]
num_hearts = 8
angle_step = 360 / num_hearts
for i in range(num_hearts):
    angle = np.deg2rad(i * angle_step)
    heart_x = int(circle_center[0] + (circle_radius + 50) * np.cos(angle)) - heart_red.width // 2
    heart_y = int(circle_center[1] + (circle_radius + 50) * np.sin(angle)) - heart_red.height // 2
    image.paste(hearts[i % len(hearts)], (heart_x, heart_y), hearts[i % len(hearts)])

# Save the image
image.save('hbday_bharath_3d.png')

# Show the image
image.show()
