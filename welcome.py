from PIL import Image, ImageDraw, ImageFilter,ImageFont
import json
import requests
import cv2

# title_font = ImageFont.truetype('./database/RussoOne-Regular.ttf', 50)
# user_font = ImageFont.truetype('./database/RussoOne-Regular.ttf', 100)
  # with open(f'./database/{server}.txt','r') as file:
    # data=json.load(file)
    # bg=data['welcome']['background']
    # im1=Image.open('./database/bg.png')

def welcome(server,user,pfp,sbg,color):
    tbg=Image.open('./database/transparent.png')
    title_font = ImageFont.truetype('./database/RussoOne-Regular.ttf', 1)
    user_font = ImageFont.truetype('./database/RussoOne-Regular.ttf', 1)
    im1 = Image.open(requests.get(sbg, stream=True).raw)
    im1=im1.resize((1050,300))
    # if pfp!='':
    if pfp!='':
      im2 = Image.open(requests.get(pfp, stream=True).raw)
    elif pfp=='':
      im2=Image.open('./database/default.png')
    back_im = tbg.copy()
    x=int(1050-255)
    y=int((900/2)-383)
    im2=im2.resize((200,200))
    back_im.paste(im2, (x,y))
    back_im.paste(im1, (0,0),im1)
    text_im=ImageDraw.Draw(back_im)
    title_text=f"WELCOME TO {server}"
    user_txt=f"{user.capitalize()}"

    fontsizea = 1  # starting font size
    fontsizeb = 1  # starting font size
    while title_font.getsize(title_text)[0] < 675 and fontsizea<50:
      fontsizea += 1
      title_font = ImageFont.truetype('./database/RussoOne-Regular.ttf', fontsizea)
    while user_font.getsize(user_txt)[0] < 675 and fontsizeb<100:
      fontsizeb += 1
      user_font = ImageFont.truetype('./database/RussoOne-Regular.ttf', fontsizeb)

    text_im.text((45,45), title_text, color, font=title_font)
    text_im.text((45,125), user_txt, color, font=user_font)
    back_im.save(f'./out/{server}.png')
    # file.close()
    return