from PIL import Image, ImageDraw, ImageFont

# Icon specifications
ICON_SIZE = 1024
BG_COLOR = (34, 45, 70)  # Background color
TEXT_COLOR = (255, 255, 255)  # Text color
FONT_PATH = "arial.ttf"  # Path to your font file
FONT_SIZE = 250

# Create the base image
icon = Image.new("RGB", (ICON_SIZE, ICON_SIZE), BG_COLOR)

# Draw a gradient background (optional)
draw = ImageDraw.Draw(icon)
for i in range(ICON_SIZE):
    gradient_color = (
        int(BG_COLOR[0] * (1 - i / ICON_SIZE) + 255 * (i / ICON_SIZE)),
        int(BG_COLOR[1] * (1 - i / ICON_SIZE) + 200 * (i / ICON_SIZE)),
        int(BG_COLOR[2] * (1 - i / ICON_SIZE) + 150 * (i / ICON_SIZE)),
    )
    draw.line([(0, i), (ICON_SIZE, i)], fill=gradient_color)

# Add text/logo
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
except IOError:
    font = ImageFont.load_default()

text = "Aenzbi"
text_width, text_height = draw.textsize(text, font=font)
text_x = (ICON_SIZE - text_width) // 2
text_y = (ICON_SIZE - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill=TEXT_COLOR)

# Add rounded corners (optional)
corner_radius = 100
for corner in [(0, 0), (0, ICON_SIZE), (ICON_SIZE, 0), (ICON_SIZE, ICON_SIZE)]:
    ellipse_box = [
        corner[0] - corner_radius if corner[0] > 0 else 0,
        corner[1] - corner_radius if corner[1] > 0 else 0,
        corner[0] + corner_radius,
        corner[1] + corner_radius,
    ]
    draw.pieslice(ellipse_box, 0, 360, fill=BG_COLOR)

# Save the icon
icon.save("icon.png")
print("Icon saved as icon.png")
