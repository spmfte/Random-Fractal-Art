import random
import datetime
from PIL import Image, ImageDraw

# Create a blank canvas
canvas_size = (500, 500)
canvas = Image.new('RGB', canvas_size, 'white')
draw = ImageDraw.Draw(canvas)

# Generate and draw a random visual animation, pattern, or fractal
def generate_visual():
  # Choose a random type of visual to generate
  visual_type = random.choice(['animation', 'pattern', 'fractal'])

  # Generate and draw the visual
  if visual_type == 'animation':
    # Generate random coordinates for the animation
    x1 = random.randint(0, canvas_size[0])
    y1 = random.randint(0, canvas_size[1])
    x2 = random.randint(0, canvas_size[0])
    y2 = random.randint(0, canvas_size[1])

    # Generate a random color for the animation
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the animation
    draw.line((x1, y1, x2, y2), fill=color, width=3)
  elif visual_type == 'pattern':
    # Generate random coordinates for the pattern
    x = random.randint(0, canvas_size[0])
    y = random.randint(0, canvas_size[1])
    size = random.randint(10, 50)

    # Generate a random color for the pattern
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the pattern
    draw.rectangle((x, y, x+size, y+size), fill=color)
  elif visual_type == 'fractal':
    # Generate random coordinates for the fractal
    x = random.randint(0, canvas_size[0])
    y = random.randint(0, canvas_size[1])
    size = random.randint(100, 200)

    # Generate a random color for the fractal
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the fractal
    draw.arc((x, y, x+size, y+size), 0, 360, fill=color)

# Generate and draw 10 random visuals
for _ in range(10):
  generate_visual()

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string
date_time_str = now.strftime("%B_%d_%Y_%H_%M_%S")

# Save and display the canvas with a filename that includes the date and time
canvas.save(f"visuals_{date_time_str}.png")
canvas.show()
