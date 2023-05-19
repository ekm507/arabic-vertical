
# convert font character to image

# کتابخانه‌ها
from PIL import Image, ImageDraw, ImageFont
from sys import argv

# تنظیمات
output_image_name = 'output.png'
font_path = './Vazirmatn-Thin.ttf'
font_size = 35
image_size = (1800, 600)
print_location = (400, 100)

text = "من فارسی را عمودی می‌نویسم."
text = '\n'.join(text.split(' '))
# چیزهای اولیه
my_image = Image.new('RGB', image_size, color = 'black')
# my_image = Image.open('input.png')
my_font = ImageFont.truetype(font_path, font_size)
my_color = (255, 255, 255)

# چاپ نوشته روی عکس
image_editable = ImageDraw.Draw(my_image)

def write_vertical(text, x, align):
    text = '\n'.join(text.split(' '))
    print_location = (x, 50)
    image_editable.text(print_location, text, my_color, font=my_font, direction='rtl', align=align, )

full_text = """من فارسی را عمودی می‌نویسم.
چون می‌توان فارسی را هم عمودی نوشت.
« قلم وزیرمتن با تنوع نازک «"""

full_text = open('text').read()

x = image_size[0] - font_size * 5
for text in full_text.split('\n'):
    write_vertical(text, x, 'right')
    x -= font_size * 5


# text = "من فارسی را عمودی می‌نویسم ."
# write_vertical('چون فارسی را هم می‌توان عمودی نوشت .', 300, 'left')
# # write_vertical('» قلم وزیرمتن با تنوع نازک «', 150, 'center')
# write_vertical('» قلم وزیرمتن با تنوع نازک «', 150, 'center')
# ذخیره کردن عکس
my_image.save(output_image_name)
