from faulthandler import disable
import tkinter as tk
from tkinter import dialog
from tkinter.filedialog import askopenfilename
from tkinter import * 
import os
import time
import __main__
import maps
import characters
import equipment
import enemies
from PIL import Image
from PIL import ImageTk
import random
import pickle
import sys

current_directory = os.getcwd()
print(current_directory)

if True:
    screen = tk.Tk()
    screen['bg']='black'
    screen.title('Bipole V: Dungeons of Biphero')
    screen.unbind_all("<<NextWindow>>")


    mainframe = tk.Frame(relief=tk.RAISED, bg='black')

    mainfont = "Courier"

    toprow = tk.Frame(master=mainframe, relief=tk.RAISED, bg='black')
    toprow.grid(row=0, column=0)

    save_button = tk.Button(master=toprow,text="SAVE",width=5,height=2,relief=RAISED, bg='black')
    save_button.config(font=(mainfont,29),fg='red')
    save_button.grid(row=0,column=0)

    Gold = 500

    filedisplay = tk.Label(master=toprow,text="Location: Bieace Castle\nGold: 0",anchor=CENTER,relief=tk.GROOVE,width=42,height=3, bg='black')
    filedisplay.config(font=(mainfont,25),fg='magenta2')
    filedisplay.grid(row=0, column=1)

    topsidefram = tk.Frame(master=toprow, relief=tk.RAISED, bg='black')
    topsidefram.grid(row=0,column=2)

    sidestepping = False

    sidestep_button = tk.Button(master=topsidefram,text="SIDE STEPPING\n(OFF)",width=16,height=2,relief=RAISED, bg='black')
    sidestep_button.config(font=(mainfont,14),fg='white')
    sidestep_button.grid(row=0,column=0)

    topsidebotmfram = tk.Frame(master=topsidefram, relief=tk.RAISED, bg='black')
    topsidebotmfram.grid(row=1,column=0)

    stat_button = tk.Button(master=topsidebotmfram,text="STAT",width=5,height=2,relief=RAISED, bg='black')
    stat_button.config(font=(mainfont,14),fg='cyan')
    stat_button.grid(row=0,column=0)

    key_button = tk.Button(master=topsidebotmfram,text="KEY ITEMS",width=10,height=2,relief=RAISED, bg='black')
    key_button.config(font=(mainfont,14),fg='yellow')
    key_button.grid(row=0,column=1)

    centrow = tk.Frame(master=mainframe, relief=tk.RAISED, bg='black')
    centrow.grid(row=1, column=0)


    sprites_canvas = tk.Canvas(master=centrow, relief=tk.RIDGE, height=600,width=650,bg='black',borderwidth=-1)
    sprites_canvas.grid(row=0,column=0)

    world_color = "stone"

    bottomest_layer = "brown"

    dimensions = (650,600)

    bottomest_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/bottomest_layer/"+bottomest_layer+".png").convert("RGBA")
    bottomest_background_sprite = ImageTk.PhotoImage(bottomest_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
    bottomest_background_image = sprites_canvas.create_image(0, 0, anchor=NW, image=bottomest_background_sprite)

    # bottomerer_background_sprites_sides = []
    # bottomerer_background_images_sides = []    
    # ind = 0
    # for x in range(4):
    #     bottomerer_background_sprites_sides.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+"0000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     bottomerer_background_images_sides.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomerer_background_sprites_sides[ind]))
    #     ind += 1
    
    bottomerer_background_sprite = ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+"0000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST))
    bottomerer_background_image = sprites_canvas.create_image(0, 0, anchor=NW, image=bottomerer_background_sprite)

    # bottomerer_background_sprites = []
    # bottomerer_background_images = []

    # bottomerer_background_sprite_unform10000 = Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+"0100"+".png").convert("RGBA")
    # bottomerer_background_sprite10000 = ImageTk.PhotoImage(bottomerer_background_sprite_unform10000.resize(dimensions,resample=Image.NEAREST))
    # bottomerer_background_sprites.append(bottomerer_background_sprite10000)
    # bottomerer_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomerer_background_sprite10000))

    # bottomerer_background_sprite_unform01000 = Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+"0000"+".png").convert("RGBA")
    # bottomerer_background_sprite01000 = ImageTk.PhotoImage(bottomerer_background_sprite_unform01000.resize(dimensions,resample=Image.NEAREST))
    # bottomerer_background_sprites.append(bottomerer_background_sprite01000)
    # bottomerer_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomerer_background_sprite01000))

    # bottomerer_background_sprite_unform00100 = Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+"1000"+".png").convert("RGBA")
    # bottomerer_background_sprite00100 = ImageTk.PhotoImage(bottomerer_background_sprite_unform00100.resize(dimensions,resample=Image.NEAREST))
    # bottomerer_background_sprites.append(bottomerer_background_sprite00100)
    # bottomerer_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomerer_background_sprite00100))

    # bottomerer_background_sprite_unform00010 = Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+"0001"+".png").convert("RGBA")
    # bottomerer_background_sprite00010 = ImageTk.PhotoImage(bottomerer_background_sprite_unform00010.resize(dimensions,resample=Image.NEAREST))
    # bottomerer_background_sprites.append(bottomerer_background_sprite00010)
    # bottomerer_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomerer_background_sprite00010))

    bottomer_background_sprite = ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottomer_layer/"+"00000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST))
    bottomer_background_image = sprites_canvas.create_image(0, 0, anchor=NW, image=bottomer_background_sprite)

    # bottomer_background_sprites_sides = []
    # bottomer_background_images_sides = []    
    # ind = 0
    # for x in range(5):
    #     bottomer_background_sprites_sides.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottomer_layer/"+"00000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     bottomer_background_images_sides.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomer_background_sprites_sides[ind]))
    #     ind += 1
    # bottomer_background_sprites = []
    # bottomer_background_images = []    
    # ind = 0
    # for x in range(5):
    #     bottomer_background_sprites.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottomer_layer/"+"00000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     bottomer_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottomer_background_sprites[ind]))
    #     ind += 1

    bottomerspr = [0]
    bottomerimg = [0]

    bottomerspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"protipole"+".png").convert("RGBA").resize((100,250),resample=Image.NEAREST)))
    bottomerimg.append(sprites_canvas.create_image(50+90, 310, anchor=CENTER, image=bottomerspr[1]))

    bottomerspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"protipole"+".png").convert("RGBA").resize((60,175),resample=Image.NEAREST)))
    bottomerimg.append(sprites_canvas.create_image(325, 290, anchor=CENTER, image=bottomerspr[2]))

    bottomerspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"protipole"+".png").convert("RGBA").resize((100,250),resample=Image.NEAREST)))
    bottomerimg.append(sprites_canvas.create_image(625-90, 310, anchor=CENTER, image=bottomerspr[3]))

    bottomerspr.append(0)
    bottomerimg.append(0)


    # bottom_background_sprites_sides = []
    # bottom_background_images_sides = []
    # ind = 0
    # for x in range(5):
    #     bottom_background_sprites_sides.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottom_layer/"+"00000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     bottom_background_images_sides.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottom_background_sprites_sides[ind]))
    #     ind += 1
    # bottom_background_sprites = []
    # bottom_background_images = []
    # ind = 0
    # for x in range(5):
    #     bottom_background_sprites.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottom_layer/"+"00000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     bottom_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=bottom_background_sprites[ind]))
    #     ind += 1

    bottom_background_sprite = ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/bottom_layer/"+"000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST))
    bottom_background_image = sprites_canvas.create_image(0, 0, anchor=NW, image=bottom_background_sprite)
    bottomspr = [0]
    bottomimg = [0]

    mul = 1

    bottomspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA").resize((165,420),resample=Image.NEAREST)))
    bottomimg.append(sprites_canvas.create_image(50, 320, anchor=CENTER, image=bottomspr[1]))

    bottomspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"protipole"+".png").convert("RGBA").resize((100,250),resample=Image.NEAREST)))
    bottomimg.append(sprites_canvas.create_image(325, 310, anchor=CENTER, image=bottomspr[2]))

    bottomspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA").resize((165,420),resample=Image.NEAREST)))
    bottomimg.append(sprites_canvas.create_image(625, 320, anchor=CENTER, image=bottomspr[3]))

    bottomspr.append(0)
    bottomimg.append(0)


    # top_background_sprites_sides = []
    # top_background_images_sides = []
    # ind = 0
    # for x in range(3):
    #     top_background_sprites_sides.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/top_layer/"+"000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     top_background_images_sides.append(sprites_canvas.create_image(0, 0, anchor=NW, image=top_background_sprites_sides[ind]))
    #     ind += 1
    # top_background_sprites = []
    # top_background_images = []
    # ind = 0
    # for x in range(3):
    #     top_background_sprites.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/top_layer/"+"000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST)))
    #     top_background_images.append(sprites_canvas.create_image(0, 0, anchor=NW, image=top_background_sprites[ind]))
    #     ind += 1
    
    top_background_sprite = ImageTk.PhotoImage(Image.open(str(current_directory)+"/world/"+world_color+"/top_layer/"+"000"+".png").convert("RGBA").resize(dimensions,resample=Image.NEAREST))
    top_background_image = sprites_canvas.create_image(0, 0, anchor=NW, image=top_background_sprite)

    topspr = [0]
    topimg = [0]

    topspr.append(ImageTk.PhotoImage(Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA").resize((165,420),resample=Image.NEAREST)))
    topimg.append(sprites_canvas.create_image(325, 320, anchor=CENTER, image=topspr[1]))




    key_background_unform = Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA")
    key_background_sprite = ImageTk.PhotoImage(key_background_unform.resize((650,600),resample=Image.NEAREST))
    key_background_image = sprites_canvas.create_image(0, 0, anchor=NW, image=key_background_sprite)


    char1_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA")
    character_sprite1 = ImageTk.PhotoImage(char1_background_sprite_unform.resize((200,500),resample=Image.NEAREST))
    character_image1 = sprites_canvas.create_image(100, 362, anchor=CENTER, image=character_sprite1)

    # character_sprite1 = PhotoImage(file = str(current_directory)+"/sprites/"+"bipoanderer.gif")
    # character_image1 = sprites_canvas.create_image(100, 362, anchor=CENTER, image=character_sprite1)

    char2_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA")
    character_sprite2 = ImageTk.PhotoImage(char2_background_sprite_unform.resize((200,500),resample=Image.NEAREST))
    character_image2 = sprites_canvas.create_image(325, 362, anchor=CENTER, image=character_sprite2)

    # character_sprite2 = PhotoImage(file = str(current_directory)+"/sprites/"+"protipole.gif")
    # character_image2 = sprites_canvas.create_image(325, 362, anchor=CENTER, image=character_sprite2)

    char3_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+"nothing"+".png").convert("RGBA")
    character_sprite3 = ImageTk.PhotoImage(char3_background_sprite_unform.resize((200,500),resample=Image.NEAREST))
    character_image3 = sprites_canvas.create_image(550, 362, anchor=CENTER, image=character_sprite3)



    
    dialouge = tk.Label(master=centrow, text="Lemniscate Bipole V: Dungeons of Biphero\n----------\n[A] Load Save\n[B] New Game", relief=tk.FLAT,width=50,height=30, bg='black')
    dialouge.config(font=(mainfont,12),fg='white')
    dialouge.grid(row=0,column=1)




    botrow = tk.Frame(master=mainframe, relief=tk.RAISED, bg='black')
    botrow.grid(row=2, column=0)

    # protagimg = PhotoImage(file="bipoleii_100x100.png")   
    # protagportrait = tk.Label(master=botrow, image=protagimg,relief=tk.RIDGE,width=150,height=150) 
    # protagportrait.grid(row=0,column=0)

    # img = None
    # portrait.config(image=img)
    # protagimg = None
    # protagportrait.config(image=img)


    party_frame = tk.Frame(master=botrow, relief=tk.RAISED, bg='black')
    party_frame.grid(row=0, column=0)

    party_font = 12

    party_member1 = tk.Label(master=party_frame, text="=EMPTY=", relief=tk.SUNKEN,width=51,height=2, bg='black')
    party_member1.config(font=(mainfont,party_font),fg='green2')
    party_member1.grid(row=0,column=0)

    party_member2 = tk.Label(master=party_frame, text="=EMPTY=", relief=tk.SUNKEN,width=51,height=2, bg='black')
    party_member2.config(font=(mainfont,party_font),fg='green2')
    party_member2.grid(row=1,column=0)

    party_member3 = tk.Label(master=party_frame, text="=EMPTY=", relief=tk.SUNKEN,width=51,height=2, bg='black')
    party_member3.config(font=(mainfont,party_font),fg='green2')
    party_member3.grid(row=2,column=0)

    party_member4 = tk.Label(master=party_frame, text="=EMPTY=", relief=tk.SUNKEN,width=51,height=2, bg='black')
    party_member4.config(font=(mainfont,party_font),fg='green2')
    party_member4.grid(row=3,column=0)



    buttons_frame = tk.Frame(master=botrow,relief=tk.FLAT, bg='black')
    buttons_frame.grid(row=0,column=1)

    # HP = 5

    # healthdisplay = tk.Label(master=lowerframe,text="HP 5/5",width=7,height=2,anchor=W)#("HP:",str(HP)+"/5"))
    # healthdisplay.config(font=(mainfont,40))
    # healthdisplay.grid(row=0,column=0)

    button_color = "black" #"grey6"

    a_button = tk.Button(master=buttons_frame,text="A",width=5,height=2,relief=RAISED, bg=button_color)
    a_button.config(font=(mainfont,20),fg='dodger blue')
    a_button.grid(row=0,column=0)

    up_button = tk.Button(master=buttons_frame,text="△",width=5,height=2,relief=RAISED, bg=button_color)
    up_button.config(font=(mainfont,20),fg='white')
    up_button.grid(row=0,column=1)

    b_button = tk.Button(master=buttons_frame,text="B",width=5,height=2,relief=RAISED, bg=button_color)
    b_button.config(font=(mainfont,20),fg='red')
    b_button.grid(row=0,column=2)

    equip_button = tk.Button(master=buttons_frame,text="EQUIP",width=5,height=2,relief=RAISED, bg=button_color)
    equip_button.config(font=(mainfont,20),fg='yellow')
    equip_button.grid(row=0,column=3)

    party_button = tk.Button(master=buttons_frame,text="PARTY",width=5,height=2,relief=RAISED, bg=button_color)
    party_button.config(font=(mainfont,20),fg='yellow')
    party_button.grid(row=0,column=4)

    item_button = tk.Button(master=buttons_frame,text="ITEM",width=5,height=2,relief=RAISED, bg=button_color)
    item_button.config(font=(mainfont,20),fg='yellow')
    item_button.grid(row=1,column=3)

    talk_button = tk.Button(master=buttons_frame,text="TALK",width=5,height=2,relief=RAISED, bg=button_color)
    talk_button.config(font=(mainfont,20),fg='yellow')
    talk_button.grid(row=1,column=4)

    left_button = tk.Button(master=buttons_frame,text="◁",width=5,height=2,relief=RAISED, bg=button_color)
    left_button.config(font=(mainfont,20),fg='white')
    left_button.grid(row=1,column=0)

    down_button = tk.Button(master=buttons_frame,text="▽",width=5,height=2,relief=RAISED, bg=button_color)
    down_button.config(font=(mainfont,20),fg='white')
    down_button.grid(row=1,column=1)

    right_button = tk.Button(master=buttons_frame,text="▷",width=5,height=2,relief=RAISED, bg=button_color)
    right_button.config(font=(mainfont,20),fg='white')
    right_button.grid(row=1,column=2)


    minimap_frame = tk.Frame(master=botrow,relief=tk.RAISED,bg="black")
    minimap_frame.grid(row=0,column=2)

    minimap_width = 2
    minimap_height = 1
    minimap_fontsize = 20
    minimap_default_color = "black"
    minimap_text_color = "magenta2"


    minimap_00 = tk.Label(master=minimap_frame, text="00", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_00.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_00.grid(row=0,column=0)

    minimap_10 = tk.Label(master=minimap_frame, text="10", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_10.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_10.grid(row=1,column=0)

    minimap_20 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_20.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_20.grid(row=2,column=0)

    minimap_30 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_30.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_30.grid(row=3,column=0)

    minimap_40 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_40.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_40.grid(row=4,column=0)


    minimap_01 = tk.Label(master=minimap_frame, text="01", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_01.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_01.grid(row=0,column=1)

    minimap_11 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_11.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_11.grid(row=1,column=1)

    minimap_21 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_21.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_21.grid(row=2,column=1)

    minimap_31 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_31.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_31.grid(row=3,column=1)

    minimap_41 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_41.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_41.grid(row=4,column=1)


    minimap_02 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_02.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_02.grid(row=0,column=2)

    minimap_12 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_12.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_12.grid(row=1,column=2)

    minimap_22 = tk.Label(master=minimap_frame, text="△", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_22.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_22.grid(row=2,column=2)

    minimap_32 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_32.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_32.grid(row=3,column=2)

    minimap_42 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_42.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_42.grid(row=4,column=2)


    minimap_03 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_03.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_03.grid(row=0,column=3)

    minimap_13 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_13.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_13.grid(row=1,column=3)

    minimap_23 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_23.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_23.grid(row=2,column=3)

    minimap_33 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_33.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_33.grid(row=3,column=3)

    minimap_43 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_43.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_43.grid(row=4,column=3)


    minimap_04 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_04.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_04.grid(row=0,column=4)

    minimap_14 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_14.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_14.grid(row=1,column=4)

    minimap_24 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_24.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_24.grid(row=2,column=4)

    minimap_34 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_34.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_34.grid(row=3,column=4)

    minimap_44 = tk.Label(master=minimap_frame, text="X", relief=tk.SUNKEN,width=minimap_width,height=minimap_height)
    minimap_44.config(font=(mainfont,minimap_fontsize),bg=minimap_default_color,fg=minimap_text_color)
    minimap_44.grid(row=4,column=4)

    vision_facing = "North"

    mainframe.pack()
else:
    print("how")

def clear_all_character_sprites():
    set_character_sprite(1,"nothing")
    set_character_sprite(2,"nothing")
    set_character_sprite(3,"nothing")

    # global character_sprite2
    # character_sprite2 = PhotoImage(file = str(current_directory)+"/sprites/nothing")
    # sprites_canvas.itemconfig(character_image2,image=character_sprite2)

    # global character_sprite3
    # character_sprite3 = PhotoImage(file = str(current_directory)+"/sprites/nothing")
    # sprites_canvas.itemconfig(character_image3,image=character_sprite3)

    print("all character sprites cleared")

def clear_sprite(num):
    if num == 1:
        print("cleared 1")
        global character_sprite1
        character_sprite1 = PhotoImage(file = str(current_directory)+"/sprites/nothing.png")
        sprites_canvas.itemconfig(character_image1,image=character_sprite1)
    elif num == 2:
        print("cleared 2")
        global character_sprite2    
        character_sprite2 = PhotoImage(file = str(current_directory)+"/sprites/nothing.png")
        sprites_canvas.itemconfig(character_image2,image=character_sprite2)
    elif num == 3:
        print("cleard 3")
        global character_sprite3
        character_sprite3 = PhotoImage(file = str(current_directory)+"/sprites/nothing.png")
        sprites_canvas.itemconfig(character_image3,image=character_sprite3)


def set_character_sprite(position,sprite):
    if position == 1:
        global char1_background_sprite_unform
        global character_sprite1
        char1_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+sprite+".png").convert("RGBA")
        character_sprite1 = ImageTk.PhotoImage(char1_background_sprite_unform.resize((200,500),resample=Image.NEAREST))
        sprites_canvas.itemconfig(character_image1, image = character_sprite1)
        print("character sprite 1 changed")
    elif position == 2:
        global char2_background_sprite_unform
        global character_sprite2
        char2_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+sprite+".png").convert("RGBA")
        character_sprite2 = ImageTk.PhotoImage(char2_background_sprite_unform.resize((200,500),resample=Image.NEAREST))
        sprites_canvas.itemconfig(character_image2, image = character_sprite2)
        print("character sprite 2 changed")
    elif position == 3:
        global char3_background_sprite_unform
        global character_sprite3
        char3_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+sprite+".png").convert("RGBA")
        character_sprite3 = ImageTk.PhotoImage(char3_background_sprite_unform.resize((200,500),resample=Image.NEAREST))
        sprites_canvas.itemconfig(character_image3, image = character_sprite3)
        print("character sprite 3 changed")
    else:
        print("ERROR ON set_character_sprite")

def set_big_character_sprite(sprite):
    global character_sprite2
    char2_background_sprite_unform = Image.open(str(current_directory)+"/sprites/"+sprite+".png").convert("RGBA")
    character_sprite2 = ImageTk.PhotoImage(char2_background_sprite_unform.resize((600,500),resample=Image.NEAREST))
    sprites_canvas.itemconfig(character_image2, image = character_sprite2)
    print("character sprite 2 changed (big)")

def set_key_background(sprite):
    global key_background_sprite
    key_background_unform = Image.open(str(current_directory)+"/sprites/"+sprite+".png").convert("RGBA")
    key_background_sprite = ImageTk.PhotoImage(key_background_unform.resize((650,600),resample=Image.NEAREST))
    sprites_canvas.itemconfig(key_background_image, image = key_background_sprite)
    print("set key background to \""+sprite+"\"")

def turn_right():
    global vision_facing
    if vision_facing == "North":
        vision_facing = "East"
        print("now facing east")
    elif vision_facing == "East":
        vision_facing = "South"
        print("now facing south")
    elif vision_facing == "South":
        vision_facing = "West"
        print("now facing west")
    elif vision_facing == "West":
        vision_facing = "North"
        print("now facing north")
    else:
        print("ERROR ON turn_right")
    refresh()

def turn_left():
    global vision_facing
    if vision_facing == "North":
        vision_facing = "West"
        print("now facing west")
    elif vision_facing == "West":
        vision_facing = "South"
        print("now facing south")
    elif vision_facing == "South":
        vision_facing = "East"
        print("now facing east")
    elif vision_facing == "East":
        vision_facing = "North"
        print("now facing north")
    else:
        print("ERROR ON turn_left")
    refresh()

def sidestep_toggle():
    global sidestepping
    if sidestepping == True:
        sidestepping = False
        sidestep_button.config(text="SIDE STEPPING\n(OFF)")
        print("side stepping disabled")
    elif sidestepping == False:
        sidestepping = True
        sidestep_button.config(text="SIDE STEPPING\n(ON)")
        print("side stepping enabled")

def nothing():
    #Bipole II: Trials developement status type beat amerite?
    pass

def disable_inputs():
    disable_keys()
    save_button.config(command=nothing)
    sidestep_button.config(command=nothing)
    stat_button.config(command=nothing)
    a_button.config(command=nothing)
    b_button.config(command=nothing)
    up_button.config(command=nothing)
    down_button.config(command=nothing)
    left_button.config(command=nothing)
    right_button.config(command=nothing)
    equip_button.config(command=nothing)
    party_button.config(command=nothing)
    item_button.config(command=nothing)
    talk_button.config(command=nothing)
    key_button.config(command=nothing)

def write_text(the_text):
    dialouge.config(text=the_text)

def clear_text():
    dialouge.config(text="")

def newgame():
    disable_inputs()
    clear_all_character_sprites()

def toggle_sidestep_button(yesno):
    global two_command
    if yesno == True:
        sidestep_button.config(command=sidestep_toggle)
        two_command = "sidestep_toggle()"
    elif yesno == False:
        sidestep_button.config(command=nothing)
        two_command = "nothing()"


q_command = "nothing()"
a_command = "nothing()"
w_command = "nothing()"
s_command = "nothing()"
e_command = "nothing()"
d_command = "nothing()"

r_command = "nothing()"
f_command = "nothing()"
t_command = "nothing()"
g_command = "nothing()"

one_command = "nothing()"
two_command = "nothing()"
three_command = "nothing()"
four_command = "nothing()"

space_command = "nothing()"

up_command = "nothing()"
down_command = "nothing()"
left_command = "nothing()"
right_command = "nothing()"


def key_input(e):
    #print(e.char)
    print(e)
    if e.char == "q":
        global q_command
        eval(q_command+"")
    elif e.char == "a":
        global a_command
        eval(a_command+"")
    elif e.char == "w":
        global w_command
        eval(w_command+"")
    elif e.char == "s":
        global s_command
        eval(s_command+"")
    elif e.char == "e":
        global e_command
        eval(e_command+"")
    elif e.char == "d":
        global d_command
        eval(d_command+"")
    
    elif e.char == "r":
        global r_command
        eval(r_command+"")
    elif e.char == "f":
        global f_command
        eval(f_command+"")
    elif e.char == "t":
        global t_command
        eval(t_command+"")
    elif e.char == "g":
        global g_command
        eval(g_command+"")

    elif e.char == "1":
        global one_command
        eval(one_command+"")
    elif e.char == "2":
        global two_command
        eval(two_command+"")
    elif e.char == "3":
        global three_command
        eval(three_command+"")
    elif e.char == "4":
        global four_command
        eval(four_command+"")

    elif e.char == " ":
        global space_command
        eval(space_command+"")

    elif e.keysym == "Up":
        global up_command
        eval(up_command+"")
    elif e.keysym == "Down":
        global down_command
        eval(down_command+"")
    elif e.keysym == "Left":
        global left_command
        eval(left_command+"")
    elif e.keysym == "Right":
        global right_command
        eval(right_command+"")

    else:
        print("unused key")

def disable_keys():
    global q_command
    global a_command
    global w_command
    global s_command
    global e_command
    global d_command
    global r_command
    global f_command
    global t_command
    global g_command
    global one_command
    global two_command
    global three_command
    global four_command
    global space_command
    global up_command
    global down_command
    global left_command
    global right_command

    q_command = "nothing()"
    a_command = "nothing()"
    w_command = "nothing()"
    s_command = "nothing()"
    e_command = "nothing()"
    d_command = "nothing()"

    r_command = "nothing()"
    f_command = "nothing()"
    t_command = "nothing()"
    g_command = "nothing()"

    one_command = "nothing()"
    two_command = "nothing()"
    three_command = "nothing()"
    four_command = "nothing()"

    space_command = "nothing()"

    up_command = "nothing()"
    down_command = "nothing()"
    left_command = "nothing()"
    right_command = "nothing()"

dialogue = ["install","bipole"]
dialogue_index = 1

def start_dialogue(input_file):
    disable_inputs()
    global dialogue
    global dialogue_index
    dialogue_index = 1
    file_contents = open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+input_file+".txt")
    dialogue = [line.rstrip('\n') for line in file_contents]
    print(dialogue)
    perform_dialogue()

def start_dialogue_direct(input_file):
    disable_inputs()
    global dialogue
    global dialogue_index
    dialogue_index = 1
    file_contents = open(current_directory+input_file)
    dialogue = [line.rstrip('\n') for line in file_contents]
    print(dialogue)
    perform_dialogue()

in_shop_list = False
shop_inventory = []
shop_end_index = 0

pawn_current = "equip"
pawn_mul = 0.5

multichoice_index = 0
multichoice_list = []

def perform_dialogue():
    disable_inputs()
    global dialogue
    global dialogue_index
    global space_command
    global g_command
    global yes_no_result
    global Gold
    global vision_facing
    global in_shop_list
    global shop_inventory
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global list_to_use_in_multi
    global multi_use_displayname
    global equip_stat_return_to
    global multiselect_index
    global mutliselect_buying
    global shop_end_index
    global item_stat_return_to
    global up_command
    global w_command
    global down_command
    global s_command
    global e_command
    global q_command
    global left_command
    global a_command
    global right_command
    global d_command
    global r_command
    global multi_char_stat_to_show
    global pawn_current
    global pawn_mul
    global current_encounter
    global current_encounter_all
    global battle_during_cutscene
    global current_encounter_all
    global current_encounter
    global did_move
    global multichoice_index
    global multichoice_list

    line = (dialogue[dialogue_index])
    if line == "#CLEAR":
        clear_all_character_sprites()
        dialogue_index += 1
        perform_dialogue()
    elif "#SET_IMAGE " in line:
        set_character_sprite(2,line.replace('#SET_IMAGE ',''))
        dialogue_index += 1
        perform_dialogue()
    elif "#SET_BIG_IMAGE " in line:
        set_big_character_sprite(line.replace('#SET_BIG_IMAGE ',''))
        dialogue_index += 1
        perform_dialogue()
    elif "#SET_KEY_BACK " in line:
        set_key_background(line.replace('#SET_KEY_BACK ',''))
        dialogue_index += 1
        perform_dialogue()
    elif line == "#END":
        refresh()
    elif line == "#END_KEY_ITEM":
        open_key_items()
    elif "#OPEN_DIALG " in line:
        thing = line.replace('#OPEN_DIALG ','')
        dialogue_index = 0
        file_contents = open(current_directory+"/dialogue/key_items/"+thing+".txt")
        dialogue = [line.rstrip('\n') for line in file_contents]
        print(dialogue)
        perform_dialogue()
    elif line == "_" or line == "-pass-" or "/==/." in line:
        dialogue_index += 1
        perform_dialogue()
    elif "#CHOICE " in line:
        dialogue_index += 1
        write_text(line.replace('#CHOICE ','').replace('[@]',"\n"))
        yes_no_controls()
    elif line == "#CHOICE_RESULT":
        if yes_no_result == False:
            dialogue_index += 1
            perform_dialogue()
        else:
            dialogue_index += 6
            perform_dialogue()
    elif line == "#CHOICE_RESULT_GO_TO":
        if yes_no_result == True:
            thing = dialogue[dialogue_index+1]
        else:
            thing = dialogue[dialogue_index+2]
        dialogue_index = search_for("/==/."+thing)
        perform_dialogue()
    elif "#SENDIFEQUIPMENT " in line:
        thing_to_check = getattr(equipment,line.replace('#SENDIFEQUIPMENT ',''))
        has = False
        for e in equipment.equipment_inventory:
            if e.DisplayName == thing_to_check.DisplayName:
                has = True
        if has:
            goto = dialogue[dialogue_index+1]
            print("HAS EQUIPMENT")
        else:
            goto = dialogue[dialogue_index+2]
            print("DOESN'T HAVE EQUIPMENT")
        dialogue_index = search_for("/==/."+goto)
        perform_dialogue()

        if Gold >= amount:
            thing = dialogue[dialogue_index+1]
        else:
            thing = dialogue[dialogue_index+2]
        dialogue_index = search_for("/==/."+thing)
        perform_dialogue()
    elif "#REMOVE_EQUIPMENT" in line:
        thing_to_get = getattr(equipment,line.replace('#REMOVE_EQUIPMENT ',''))
        removed = False
        for e in equipment.equipment_inventory:
            if e.DisplayName == thing_to_get.DisplayName:
                if removed == False:
                    equipment.equipment_inventory.remove(e) 
                    print("removed equipment")
                    removed = True
        if removed == False:
            print("didn't remove equipment (couldn't find)")
        dialogue_index += 1
        advance_text()
    elif "#SENDIFGOLD>= " in line:
        amount = (int)(line.replace("#SENDIFGOLD>= ",""))
        if Gold >= amount:
            thing = dialogue[dialogue_index+1]
        else:
            thing = dialogue[dialogue_index+2]
        dialogue_index = search_for("/==/."+thing)
        perform_dialogue()
    elif "#SENDIFKEYITEM " in line:
        keytocheck = getattr(equipment,line.replace('#SENDIFKEYITEM ',''))
        haskey = False
        for k in equipment.key_item_inventory:
            if k.DisplayName == keytocheck.DisplayName:
                haskey = True
                print(k.DisplayName+" is "+ keytocheck.DisplayName)
            else:
                print(k.DisplayName+" isn't "+ keytocheck.DisplayName)
        if haskey:
            thing = dialogue[dialogue_index+1]
            print("HAS KEY ITEM")
        else:
            thing = dialogue[dialogue_index+2]
            print("DOESN'T HAVE KEY ITEM")
        dialogue_index = search_for("/==/."+thing)
        perform_dialogue()
    elif line == "#DESTROY_SELF":
        cords = maps.return_player_cords()
        maps.current_location[1][cords[1]][cords[0]] = ["000"]
        did_move = False
        refresh()
    elif "#OVERRIDE_SELF" in line:
        cords = maps.return_player_cords()
        maps.current_location[1][cords[1]][cords[0]] = [line.replace('#OVERRIDE_SELF ','')]
        did_move = False
        refresh()
    elif line == "#RECRUIT":
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        characters.All_Recruited_Characters.append(eval("characters."+line))
        characters.Unequipped_Characters.append(eval("characters."+line))
        dialogue_index += 1
        perform_dialogue()
    elif "#GAIN_KEYITEM" in line:
        thing_to_get = getattr(equipment,line.replace('#GAIN_KEYITEM ',''))
        equipment.key_item_inventory.append(thing_to_get)
        dialogue_index += 1
        write_text("Obtained "+thing_to_get.DisplayName+"!\n["+thing_to_get.DisplayName+" was added to your KEY ITEMS]")
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
    elif "#REMOVE_KEYITEM" in line:
        thing_to_get = getattr(equipment,line.replace('#REMOVE_KEYITEM ',''))
        removed = False
        for k in equipment.key_item_inventory:
            if k.DisplayName == thing_to_get.DisplayName:
                if removed == False:
                    equipment.key_item_inventory.remove(k) 
                    print("removed key item")
                    removed = True
        if removed == False:
            print("didn't remove key item (couldn't find)")
        dialogue_index += 1
        advance_text()
    elif "#GAIN_EQUIPMENT " in line:
        if len(equipment.equipment_inventory) < 20:
            thing_to_get = getattr(equipment,line.replace('#GAIN_EQUIPMENT ',''))
            equipment.equipment_inventory.append(thing_to_get)
            dialogue_index += 1
            write_text("Obtained "+thing_to_get.DisplayName+"!")
            space_command = "advance_text()"
            g_command = "advance_text()"
            talk_button.config(command=advance_text)
        else:
            write_text("Equipment inventory is full,\ncannot obtain item.")
            dialogue_index = 0
            space_command = "refresh()"
            g_command = "refresh()"
            talk_button.config(command=refresh)
    elif "#GAIN_ITEM " in line:
        if len(equipment.item_inventory) < 20:
            thing_to_get = getattr(equipment,line.replace('#GAIN_ITEM ',''))
            equipment.item_inventory.append(thing_to_get)
            dialogue_index += 1
            write_text("Obtained "+thing_to_get.DisplayName+"!")
            space_command = "advance_text()"
            g_command = "advance_text()"
            talk_button.config(command=advance_text)
        else:
            write_text("Item inventory is full,\ncannot obtain item.")
            dialogue_index = 0
            space_command = "refresh()"
            g_command = "refresh()"
            talk_button.config(command=refresh)
    elif "#ADD_GOLD" in line:
        Gold += int(line.replace('#ADD_GOLD ',''))
        write_text("Obtained "+line.replace('#ADD_GOLD ','')+" gold!")
        dialogue_index += 1
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
    elif "#REMOVE_GOLD" in line:
        Gold -= int(line.replace('#REMOVE_GOLD ',''))
        #write_text("Lost "+line.replace('#REMOVE_GOLD ','')+" gold!")
        dialogue_index += 1
        # space_command = "advance_text()"
        # g_command = "advance_text()"
        # talk_button.config(command=advance_text)
        advance_text()
    elif line == "#ECOCHECKER":
        locs = []
        for loc in maps.List_of_All_Locations:
            if loc[8][1][0] != "no eco":
                locs.append(loc)
        txt = ""
        index = 0
        for loc in locs:
            if index != 0:
                txt = txt + "\n"
            txt = txt + loc[0] + " | " + str(loc[8][0]) + " (" + loc[8][1][0] + ", " + str(loc[8][1][1]) + ")"
            index += 1
        write_text(txt)
        dialogue_index += 1
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
    elif line == "#ECONOMY":
        thing = maps.current_location[8]
        print(thing)
        if (thing[0]-thing[2][4]) > 0:
            change = "("+str(round(((thing[0]-thing[2][4])/thing[0]*100),2)) + "% increase)"
        elif thing != 0:
            change = "("+str(round(((thing[2][4]-thing[0])/thing[0]*100),2)) + "% decrease)"
        else:
            chance = "(0% change)"
        chance = round((100-(100/(thing[1][1]*0.5))),2)
        if chance < 0:
            chance = 0
        write_text("Current local economy:\n"+str(thing[0])+" "+change+"\n"+thing[1][0]+" state for the past "+str(thing[1][1])+" battle(s)\n"+str(chance)+"% chance of economic state shift\n"+str(thing[2][0])+" > "+str(thing[2][1])+" > "+str(thing[2][2])+" > "+str(thing[2][3])+" > "+str(thing[2][4]))
        dialogue_index += 1
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
    elif line == "#PROGRESS_ECONOMY":
        progress_economy()
        write_text("Economy has been progressed!")
        dialogue_index += 1
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
    elif line == "#MOVE_TO":
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        maps.current_location = getattr(maps,line)
        print("location: "+maps.current_location[0])
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        print(dialogue[dialogue_index])
        print(dialogue[dialogue_index+1])
        maps.player_tracking[maps.player_cords[1]][maps.player_cords[0]] = [""]
        maps.player_tracking[int(dialogue[dialogue_index+1])][int(dialogue[dialogue_index])] = ["player"]
        dialogue_index += 2
        line = (dialogue[dialogue_index])
        print(line)
        if line != "NO CHANGE":
            vision_facing = line
        if maps.current_location[10] == "safe":
            print("SAVE ZONE, AUTOSAVING...")
            autosave_data()
        else:
            print("ZONE IS NOT SAFE, WILL NOT AUTOSAVE")
        dialogue_index += 1
        print(line)
        did_move = False
        refresh()
    elif line == "#SET_TILE":
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        map = getattr(maps,line)
        print("map: "+map[0])
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        y = (int)(dialogue[dialogue_index])
        x = (int)(dialogue[dialogue_index+1])
        dialogue_index += 2
        print((dialogue[dialogue_index]))
        map[1][y][x][0] = dialogue[dialogue_index]
        print(map[1])
        dialogue_index += 1
        perform_dialogue()
    elif line == "#RESTORE_ALL":
        for char in characters.All_Recruited_Characters:
            char.Current_HP = char.Max_HP
            char.Current_SP = char.Max_SP
        dialogue_index += 1
        perform_dialogue()
        shop_inventory = []
    elif line == "#SHOP_EQUIPMENT":
        filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
        shop_start_index= dialogue_index
        in_shop_list = True
        loop_index = 1
        shop_inventory = []
        while in_shop_list == True:
            loop_index += 1
            thing = (dialogue[dialogue_index+loop_index])
            print(thing)
            if thing == "#SHOP_END":
                in_shop_list = False
                shop_end_index = loop_index + dialogue_index + 1
            else:
                shop_inventory.append(getattr(equipment,thing))
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        text_to_use_in_multi = line + "\nLocal Economy: " + str(round(maps.current_location[8][0]/100,2)) + "x\n[A] Purchase\n[Left] Stats\n[B] Leave\n----------"
        temporary_text_to_use_in_multi = text_to_use_in_multi
        list_to_use_in_multi = shop_inventory
        multi_use_displayname = True
        equip_stat_return_to = "perform_dialogue"
        dialogue_index = shop_start_index
        multiselect_index = 0
        mutliselect_buying = True
        write_text(write_multiselect_with_price())
        up_button.config(command=multiselect_move_up_shop)
        up_command = 'multiselect_move_up_shop()'
        w_command = 'multiselect_move_up_shop()'
        down_button.config(command=multiselect_move_down_shop)
        down_command = 'multiselect_move_down_shop()'
        s_command = 'multiselect_move_down_shop()'
        b_button.config(command=end_shop)
        e_command = "end_shop()"
        a_button.config(command=purchase_equipment)
        q_command = "purchase_equipment()"
        left_button.config(command=print_equipment_stats)
        left_command = 'print_equipment_stats()'
        a_command = 'print_equipment_stats()'
    elif line == "#SHOP_ITEM":
        multi_char_stat_to_show = None
        filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
        shop_start_index= dialogue_index
        in_shop_list = True
        loop_index = 1
        shop_inventory = []
        while in_shop_list == True:
            loop_index += 1
            thing = (dialogue[dialogue_index+loop_index])
            print(thing)
            if thing == "#SHOP_END":
                in_shop_list = False
                shop_end_index = loop_index + dialogue_index + 1
            else:
                shop_inventory.append(getattr(equipment,thing))
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        text_to_use_in_multi = line + "\nLocal Economy: " + str(round(maps.current_location[8][0]/100,2)) + "x\n[A] Purchase\n[Left] Stats\n[B] Leave\n----------"
        temporary_text_to_use_in_multi = text_to_use_in_multi
        list_to_use_in_multi = shop_inventory
        multi_use_displayname = True
        item_stat_return_to = "perform_dialogue"
        dialogue_index = shop_start_index
        multiselect_index = 0
        mutliselect_buying = True
        write_text(write_multiselect_with_price())
        up_button.config(command=multiselect_move_up_shop)
        up_command = 'multiselect_move_up_shop()'
        w_command = 'multiselect_move_up_shop()'
        down_button.config(command=multiselect_move_down_shop)
        down_command = 'multiselect_move_down_shop()'
        s_command = 'multiselect_move_down_shop()'
        b_button.config(command=end_shop)
        e_command = "end_shop()"
        a_button.config(command=purchase_item)
        q_command = "purchase_item()"
        left_button.config(command=print_item_stats)
        left_command = 'print_item_stats()'
        a_command = 'print_item_stats()'
    elif line == "#PAWN_INIT_VAR":
        pawn_current = "equip"
        dialogue_index += 1
        perform_dialogue()
    elif line == "#PAWN":
        multi_char_stat_to_show = None
        filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
        shop_start_index = dialogue_index
        shop_end_index = dialogue_index +3
        dialogue_index += 1
        line = (dialogue[dialogue_index])
        if pawn_current == "equip":
            pawn_mul = float(dialogue[dialogue_index+1])
            print(pawn_mul)
            text_to_use_in_multi = line + "\n==SELL EQUIPMENT==\nPawn Pricing: "+str(pawn_mul)+"x\nLocal Economy: "+str(round(maps.current_location[8][0]/100,2))+"x\n[A] Sell\n[Left] Stats\n[Right] Items\n[B] Leave\n----------"
            temporary_text_to_use_in_multi = text_to_use_in_multi
            list_to_use_in_multi = equipment.equipment_inventory
            multi_use_displayname = True
            equip_stat_return_to = "perform_dialogue"
            multiselect_index = 0
            mutliselect_buying = False
            dialogue_index += 1
            dialogue_index = shop_start_index
            write_text(write_multiselect_with_price())
            up_button.config(command=multiselect_move_up_shop)
            up_command = 'multiselect_move_up_shop()'
            w_command = 'multiselect_move_up_shop()'
            down_button.config(command=multiselect_move_down_shop)
            down_command = 'multiselect_move_down_shop()'
            s_command = 'multiselect_move_down_shop()'
            b_button.config(command=end_shop)
            e_command = "end_shop()"
            if multiselect_index < len(equipment.equipment_inventory):
                a_button.config(command=sell_equipment)
                q_command = "sell_equipment()"
                left_button.config(command=print_equipment_stats)
                left_command = 'print_equipment_stats()'
                a_command = 'print_equipment_stats()'
            right_button.config(command=pawn_switch_to_items)
            right_command = 'pawn_switch_to_items()'
            d_command = 'pawn_switch_to_items()'
        elif pawn_current == "item":
            text_to_use_in_multi = line + "\n==SELL ITEMS==\nPawn Pricing: "+str(pawn_mul)+"x\nLocal Economy: "+str(round(maps.current_location[8][0]/100,2))+"x\n[A] Sell\n[Left] Stats\n[Right] Equipment\n[B] Leave\n----------"
            temporary_text_to_use_in_multi = text_to_use_in_multi
            list_to_use_in_multi = equipment.item_inventory
            multi_use_displayname = True
            item_stat_return_to = "perform_dialogue"
            multiselect_index = 0
            mutliselect_buying = False
            dialogue_index += 1
            pawn_mul = float(dialogue[dialogue_index])
            print(pawn_mul)
            dialogue_index = shop_start_index
            write_text(write_multiselect_with_price())
            up_button.config(command=multiselect_move_up_shop)
            up_command = 'multiselect_move_up_shop()'
            w_command = 'multiselect_move_up_shop()'
            down_button.config(command=multiselect_move_down_shop)
            down_command = 'multiselect_move_down_shop()'
            s_command = 'multiselect_move_down_shop()'
            b_button.config(command=end_shop)
            e_command = "end_shop()"
            if multiselect_index < len(equipment.item_inventory):
                a_button.config(command=sell_item)
                q_command = "sell_item()"
                left_button.config(command=print_item_stats)
                left_command = 'print_item_stats()'
                a_command = 'print_item_stats()'
            right_button.config(command=pawn_switch_to_equip)
            right_command = 'pawn_switch_to_equip()'
            d_command = 'pawn_switch_to_equip()'
    elif "#ENCOUNTER " in line:
        #current_encounter_all = getattr(enemies,line.replace('#ENCOUNTER ',''))
        current_encounter_all = getattr(enemies,line.replace('#ENCOUNTER ',''))[0]
        current_encounter = []
        print("\n\n\n\/\/\/\n")
        print(current_encounter_all)
        for enem in current_encounter_all:
            current_encounter.append(enem)
        print(current_encounter)
        for enem in current_encounter:
            enem.Current_HP = enem.Max_HP
            enem.Current_SP = enem.Max_SP
            enem.Effects = []
        image_index = 0
        for char in characters.Current_Party:
            char.Priority = 250
        if getattr(enemies,line.replace('#ENCOUNTER ',''))[1] == "Big":
            print("enemy big sprite")
            set_big_character_sprite(current_encounter[0].Sprite)
        else:
            for enem in current_encounter:
                if image_index == 0:
                    set_character_sprite(2,enem.Sprite)
                elif image_index == 1:
                    set_character_sprite(1,enem.Sprite)
                elif image_index == 2:
                    set_character_sprite(3,enem.Sprite)
                image_index += 1
        battle_during_cutscene = True
        dialogue_index += 1
        Combat_Start_Player_Turn()
    elif "#OPEN_PATHS " in line:
        for row in maps.current_location[1]:
            print(row)
            for thing in row:
                print(thing)
                print("_"+line.replace('#OPEN_PATHS ','')+" vs ")
                print(thing[0])
                if thing[0] == "_"+line.replace('#OPEN_PATHS ',''):
                    thing[0]= "000"
                    print("changed to 000")
        dialogue_index += 1
        advance_text()
    elif line == "#INIT_MULTICHOICE":
        multichoice_index = 0
        dialogue_index += 1
        perform_dialogue()
    elif line == "#MULTICHOICE":
        multichoice_list = eval(dialogue[dialogue_index+2])
        thing_to_write = dialogue[dialogue_index+1]+"\n\n"+multichoice_list[multichoice_index]+"\n\n<--    -->\n[A] Select\n[B] Close"
        write_text(thing_to_write.replace('[@]',"\n"))
        a_command = "multichoice_move_left()"
        left_command = "multichoice_move_left()"
        left_button.config(command=multichoice_move_left)
        d_command = "multichoice_move_right()"
        right_command = "multichoice_move_right()"
        right_button.config(command=multichoice_move_right)
        q_command = "multichoice_select()"
        a_button.config(command=multichoice_select)
        e_command = "multichoice_return()"
        b_button.config(command=multichoice_return)
    elif "#GOTO " in line:
        dialogue_index = search_for("/==/."+line.replace('#GOTO ',''))
        perform_dialogue()
    elif line == "#PERFORM_WARP_TILE":
        standing_on = maps.return_tile_on()
        print("STANDING ON: "+standing_on)
        warp_letter = None
        warp_number = None
        if "w" in standing_on:
            warp_letter = "w"
        else:
            warp_letter = "W"
        warp_number = standing_on.replace(warp_letter,"")
        print("warp_letter: "+warp_letter)
        print("warp_number: "+warp_number)
        traveling_to = None
        if warp_letter == "w":
            traveling_to = "W"
        else:
            traveling_to = "w"
        traveling_to = traveling_to + warp_number
        print("traveling_to: "+traveling_to)
        row_index = 0
        col_index = 0
        for row in maps.current_location[1]:
            print(row)
            col_index = 0
            for thing in row:
                print(thing)
                print(thing[0])
                if thing[0] == traveling_to:
                    print("WARP POINT FOUND")
                    maps.player_tracking[maps.player_cords[1]][maps.player_cords[0]] = [""]
                    maps.player_tracking[row_index][col_index] = ["player"]
                col_index += 1
            row_index += 1
        dialogue_index += 1
        advance_text()
    elif line == "#POINT_CASINO":
        win_number = random.randint(0,200)
        if(win_number == 0):
            write_text("==========================\nJACKPOT!!!  WON 10000G!!!\n==========================\n    (You won 10,000 G!)")
            Gold += 10000
        elif(win_number < 6):
            write_text("==========================\nMINIJACKPOT!  WON 2000G!\n==========================\n    (You won 2,000 G!)")
            Gold += 2000
        elif(win_number < 21):
            write_text("==========================\nWON 750G!\n==========================\n      (You won 750 G!)")
            Gold += 750
        elif(win_number < 40):
            write_text("==========================\nWON 250G!\n==========================\n      (You won 250 G!)")
            Gold += 250
        elif(win_number < 60):
            write_text("==========================\nWON 12G!\n==========================\n      (You won 12 G!)")
            Gold += 12
        elif(win_number < 72):
            write_text("==========================\nWON 1G!\n==========================\n      (You won 1 G!)")
            Gold += 1
        else:
            write_text("==========================\nYOU LOST!\n==========================\n       (Luck issue.)")
        filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
        dialogue_index += 1
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
    elif "#WALL_SWAP " in line:
        already_swapped = []
        r_index = 0
        for row in maps.current_location[1]:
            print(row)
            t_index = 0
            for thing in row:
                print(thing)
                print("_"+line.replace('#WALL_SWAP ','')+" vs ")
                print(thing[0])
                if thing[0] == "_"+line.replace('#WALL_SWAP ',''):
                    thing[0]= "-"+line.replace('#WALL_SWAP ','')
                    print("changed to -"+line.replace('#WALL_SWAP ',''))
                    already_swapped.append([r_index,t_index])
                t_index += 1
            r_index += 1
        r_index = 0
        for row in maps.current_location[1]:
            print(row)
            t_index = 0
            for thing in row:
                print(thing)
                print("-"+line.replace('#WALL_SWAP ','')+" vs ")
                print(thing[0])
                if thing[0] == "-"+line.replace('#WALL_SWAP ',''):
                    has_swapped = False
                    for swapped in already_swapped:
                        if swapped[0] == r_index and swapped[1] == t_index:
                            has_swapped = True
                            print("not swapping, tile was just swapped")
                    if has_swapped == False:
                        thing[0]= "_"+line.replace('#WALL_SWAP ','')
                        print("changed to _"+line.replace('#WALL_SWAP ',''))
                t_index += 1
            r_index += 1
        dialogue_index += 1
        advance_text()
    else:
        write_text(line.replace('[@]',"\n"))
        dialogue_index += 1
        space_command = "advance_text()"
        g_command = "advance_text()"
        talk_button.config(command=advance_text)
        

def multichoice_move_left():
    disable_inputs()
    print("multichoice_move_left")
    global multichoice_index
    global multichoice_list
    if multichoice_index <= 0:
        multichoice_index = len(multichoice_list)-1
    else:
        multichoice_index -= 1
    perform_dialogue()

def multichoice_move_right():
    disable_inputs()
    print("multichoice_move_right")
    global multichoice_index
    global multichoice_list
    if multichoice_index >= len(multichoice_list)-1:
        multichoice_index = 0
    else:
        multichoice_index += 1
    perform_dialogue()
    
def multichoice_select():
    disable_inputs()
    print("multichoice_select")
    global multichoice_list
    global multichoice_index
    global dialogue_index
    global dialogue
    dialogue_index = search_for("/==/."+multichoice_list[multichoice_index])
    perform_dialogue()

def multichoice_return():
    disable_inputs()
    print("multichoice_return")
    global multichoice_list
    global multichoice_index
    global dialogue_index
    global dialogue
    dialogue_index = search_for("/==/."+dialogue[dialogue_index+3])
    perform_dialogue()

def search_for(text):
    ind = 0
    thing = text
    for x in dialogue:
        if x == thing:
            return ind
        ind += 1
    print("deez nuts!!! 🤣🤣🤣🤣🤣🤣🤣")
    return "deez nuts!!! 🤣🤣🤣🤣🤣🤣🤣"


def progress_economy():
    # 1 Golden - (6 to 20)
    # 2/3 Flourishing - (3 to 12)
    # 4/5/6 Rising - (1 to 7)
    # 7/8/9 Neutral - (-5 to 5)
    # 10 Crackhead - (-10 to 10)
    # 11/12/13 Falling - (-7 to -1)
    # 14/15 Failing - (-12 to -3)
    # 16 Crashing - (-20 to -6)
    for loc in maps.List_of_All_Locations:
        print(loc[0]+" is "+loc[8][1][0])
        if loc[8][1][0] != "no eco":
            thing = loc[8]
            print("Current: "+thing[1][0])
            if thing[1][0] == "Golden":
                rng = random.randint(6,20)
            elif thing[1][0] == "Flourishing":
                rng = random.randint(3,12)
            elif thing[1][0] == "Rising":
                rng = random.randint(1,7)
            elif thing[1][0] == "Neutral":
                rng = random.randint(-3,3)
            elif thing[1][0] == "Crackhead":
                rng = random.randint(-10,10)
            elif thing[1][0] == "Falling":
                rng = random.randint(-7,-1)
            elif thing[1][0] == "Failing":
                rng = random.randint(-12,-3)
            elif thing[1][0] == "Crashing":
                rng = random.randint(-20,-6)
            print(thing[2])
            del thing[2][0]
            thing[2].append(thing[0])
            print(thing[2])
            print("Change: "+str(rng))
            to_add = round((thing[0]*(rng/100)),2)
            print(str(thing[0])+" + "+str(to_add)+" = "+str(thing[0]+to_add))
            thing[0] =round((thing[0] + to_add),2)

            chance = round((100-(100/(thing[1][1]*0.5))),2)
            rng = random.randint(0,100)
            if rng <= chance:
                print(str(rng)+" <= "+str(chance)+" | CHANGE")
                hasChanged = False
                check = thing[1][0]

                while hasChanged == False:
                    rng = random.randint(1,16)
                    print("rng = "+str(rng))
                    if rng == 1:
                        if check != "Golden" and check != "Crashing" and thing[0] < 200:
                            thing[1][0] = "Golden"
                            hasChanged = True
                    elif rng == 2 or rng == 3:
                        if check != "Flourishing" and thing[0] < 200:
                            thing[1][0] = "Flourishing"
                            hasChanged = True
                    elif rng == 4 or rng == 5 or rng == 6 and thing[0] < 300 and thing[0] > 15:
                        if check != "Rising":
                            thing[1][0] = "Rising"
                            hasChanged = True
                    elif rng == 7 or rng == 8 or rng == 9 and thing[0] < 300 and thing[0] > 15:
                        if check != "Neutral":
                            thing[1][0] = "Neutral"
                            hasChanged = True
                    elif rng == 10:
                        if check != "Crackhead" and check != "Rising" and check != "Falling" and thing[0] < 250:
                            thing[1][0] = "Rising"
                            hasChanged = True
                    elif rng == 11 or rng == 12 or rng == 13:
                        if check != "Falling" and thing[0] > 15:
                            thing[1][0] = "Falling"
                            hasChanged = True
                    elif rng == 14 or rng == 15 and thing[0] > 15:
                        if check != "Failing":
                            thing[1][0] = "Failing"
                            hasChanged = True
                    elif rng == 16:
                        if check != "Crashing" and thing[0] > 20:
                            thing[1][0] = "Crashing"
                            hasChanged = True
                    if hasChanged == False:
                        print("repeating...")
                print("set to "+thing[1][0])
                thing[1][1] = 1
            else:
                print(str(rng)+" <= "+str(chance)+" | NO CHANGE")
                thing[1][1] += 1



def pawn_switch_to_items():
    global pawn_current
    pawn_current = "item"
    perform_dialogue()

def pawn_switch_to_equip():
    global pawn_current
    pawn_current = "equip"
    perform_dialogue()

def sell_equipment():
    disable_inputs()
    global pawn_mul
    global multiselect_index
    global temporary_text_to_use_in_multi
    if multiselect_index < len(equipment.equipment_inventory):
        if equipment.equipment_inventory[multiselect_index].Purchasing_Price > 0:
            write_text("Sell "+ equipment.equipment_inventory[multiselect_index].DisplayName + " for " + str(round(equipment.equipment_inventory[multiselect_index].Purchasing_Price*pawn_mul*(maps.current_location[8][0]/100)))+ "G?\n[A] Yes\n[B] No")
            global e_command
            b_button.config(command=perform_dialogue)
            e_command = "perform_dialogue()"
            global q_command
            a_button.config(command=confirm_sell_equipment)
            q_command = "confirm_sell_equipment()"
        else:
            temporary_text_to_use_in_multi = "I ain't buying that"
            perform_dialogue()
    else:
        temporary_text_to_use_in_multi = "Nothing is selected"
        perform_dialogue()

def sell_item():
    disable_inputs()
    global pawn_mul
    global multiselect_index
    global temporary_text_to_use_in_multi
    if multiselect_index < len(equipment.item_inventory):
        if equipment.item_inventory[multiselect_index].Purchasing_Price > 0:
            write_text("Sell "+ equipment.item_inventory[multiselect_index].DisplayName + " for " + str(round(equipment.item_inventory[multiselect_index].Purchasing_Price*pawn_mul*(maps.current_location[8][0]/100)))+ "G?\n[A] Yes\n[B] No")
            global e_command
            b_button.config(command=perform_dialogue)
            e_command = "perform_dialogue()"
            global q_command
            a_button.config(command=confirm_sell_item)
            q_command = "confirm_sell_item()"
        else:
            temporary_text_to_use_in_multi = "I ain't buying that"
            perform_dialogue()
    else:
        temporary_text_to_use_in_multi = "Nothing is selected"
        perform_dialogue()

def confirm_sell_item():
    global multiselect_index
    global Gold
    global pawn_mul
    thing = equipment.item_inventory[multiselect_index]
    Gold = round(Gold + (equipment.item_inventory[multiselect_index].Purchasing_Price*pawn_mul*(maps.current_location[8][0]/100)))
    equipment.item_inventory.remove(thing)
    write_text("Sold "+thing.DisplayName)
    filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
    global e_command
    b_button.config(command=perform_dialogue)
    e_command = "perform_dialogue()"
    global q_command
    a_button.config(command=perform_dialogue)
    q_command = "perform_dialogue()"
    global g_command
    global space_command
    talk_button.config(command=perform_dialogue)
    g_command = "perform_dialogue()"
    space_command = "perform_dialogue()"

def confirm_sell_equipment():
    global multiselect_index
    global Gold
    global pawn_mul
    thing = equipment.equipment_inventory[multiselect_index]
    Gold = round(Gold + (equipment.equipment_inventory[multiselect_index].Purchasing_Price*pawn_mul*(maps.current_location[8][0]/100)))
    equipment.equipment_inventory.remove(thing)
    write_text("Sold "+thing.DisplayName)
    filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
    global e_command
    b_button.config(command=perform_dialogue)
    e_command = "perform_dialogue()"
    global q_command
    a_button.config(command=perform_dialogue)
    q_command = "perform_dialogue()"
    global g_command
    global space_command
    talk_button.config(command=perform_dialogue)
    g_command = "perform_dialogue()"
    space_command = "perform_dialogue()"

def purchase_equipment():
    disable_inputs()
    global shop_inventory
    global multiselect_index
    write_text("Buy "+ shop_inventory[multiselect_index].DisplayName + " for " + str(round(shop_inventory[multiselect_index].Purchasing_Price*(maps.current_location[8][0]/100))) + "G?\n[A] Yes\n[B] No")
    global e_command
    b_button.config(command=perform_dialogue)
    e_command = "perform_dialogue()"
    global q_command
    a_button.config(command=confirm_buy_equipment)
    q_command = "confirm_buy_equipment()"

def purchase_item():
    disable_inputs()
    global shop_inventory
    global multiselect_index
    write_text("Buy "+ shop_inventory[multiselect_index].DisplayName + " for " + str(round(shop_inventory[multiselect_index].Purchasing_Price*(maps.current_location[8][0]/100))) + "G?\n[A] Yes\n[B] No")
    global e_command
    b_button.config(command=perform_dialogue)
    e_command = "perform_dialogue()"
    global q_command
    a_button.config(command=confirm_buy_item)
    q_command = "confirm_buy_item()"

def confirm_buy_equipment():
    global shop_inventory
    global multiselect_index
    global Gold
    thing = shop_inventory[multiselect_index]
    if Gold < round(shop_inventory[multiselect_index].Purchasing_Price*(maps.current_location[8][0]/100)):
        write_text("Not enough gold")
    elif len(equipment.equipment_inventory) >= 20:
        write_text("Equipment inventory full")
    else:
        Gold = round(Gold - (shop_inventory[multiselect_index].Purchasing_Price*(maps.current_location[8][0]/100)))
        equipment.equipment_inventory.append(thing)
        write_text("Purchased "+thing.DisplayName)
    filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
    global e_command
    b_button.config(command=perform_dialogue)
    e_command = "perform_dialogue()"
    global q_command
    a_button.config(command=perform_dialogue)
    q_command = "perform_dialogue()"
    global g_command
    global space_command
    talk_button.config(command=perform_dialogue)
    g_command = "perform_dialogue()"
    space_command = "perform_dialogue()"

def confirm_buy_item():
    global shop_inventory
    global multiselect_index
    global Gold
    thing = shop_inventory[multiselect_index]
    if Gold < round(shop_inventory[multiselect_index].Purchasing_Price*(maps.current_location[8][0]/100)):
        write_text("Not enough gold")
    elif len(equipment.item_inventory) >= 20:
        write_text("Item inventory full")
    else:
        Gold = round(Gold - (shop_inventory[multiselect_index].Purchasing_Price*(maps.current_location[8][0]/100)))
        equipment.item_inventory.append(thing)
        write_text("Purchased "+thing.DisplayName)
    filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
    global e_command
    b_button.config(command=perform_dialogue)
    e_command = "perform_dialogue()"
    global q_command
    a_button.config(command=perform_dialogue)
    q_command = "perform_dialogue()"
    global g_command
    talk_button.config(command=perform_dialogue)
    g_command = "perform_dialogue()" 

def end_shop():
    global shop_end_index
    global dialogue_index
    dialogue_index = shop_end_index
    perform_dialogue()

def advance_text():
    disable_inputs()
    perform_dialogue()

dialouge_file = "empty"

current_encounter = []
current_encounter_all = []

def refresh():
    disable_inputs()
    update_minimap()
    clear_other_npcs_sprites()
    generate_background()
    clear_all_character_sprites()
    write_text("")
    update_party_text()
    set_key_background("nothing")
    global battle_during_cutscene
    battle_during_cutscene = False
    global dialogue_index
    global dialogue
    global dialouge_file
    dialouge_file = "empty"
    dialouge = [line.rstrip('\n') for line in current_directory+"/dialogue/"+maps.current_location[4]+"/"+dialouge_file+".txt"]
    dialogue_index = 1
    cords = maps.return_player_cords()
    global Gold
    filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
    standing_on = maps.current_location[1][cords[1]][cords[0]][0]
    global space_command
    global g_command
    global r_command
    if standing_on == "000" or standing_on.startswith("-"):
        global did_move
        if did_move == True:
            did_move = False
            if maps.current_location[5] == True:
                if maps.current_location[7] >= random.randint(0,100):
                    write_text("Enemy encounter!")
                    global current_encounter
                    global current_encounter_all
                    encounter_no = str(random.randint(0,len(maps.current_location[6])-1))
                    current_encounter_all = maps.current_location[6][int(encounter_no)][0]
                    current_encounter = []
                    for enem in current_encounter_all:
                        current_encounter.append(enem)
                    for enemy in current_encounter:
                        enemy.Current_HP = enemy.Max_HP
                        enemy.Current_SP = enemy.Max_SP
                        enemy.Effects = []
                    image_index = 0
                    for char in characters.Current_Party:
                        char.Priority = 250
                    if maps.current_location[6][int(encounter_no)][1] == "Big":
                        print("enemy big sprite")
                        set_big_character_sprite(current_encounter[0].Sprite)
                    else:
                        for enem in current_encounter:
                            if image_index == 0:
                                set_character_sprite(2,enem.Sprite)
                            elif image_index == 1:
                                set_character_sprite(1,enem.Sprite)
                            elif image_index == 2:
                                set_character_sprite(3,enem.Sprite)
                            image_index += 1
                    space_command = "Combat_Start_Player_Turn()"
                    g_command = "Combat_Start_Player_Turn()"
                    talk_button.config(command=Combat_Start_Player_Turn)
                    r_command = "Combat_Start_Player_Turn()"
                    a_button.config(command=Combat_Start_Player_Turn)
                else:
                    enable_movement_controls()
            else:
                enable_movement_controls()
        else:
            enable_movement_controls()
    elif standing_on.startswith('n'):
        enable_movement_controls()
    elif standing_on.startswith('T') or standing_on.startswith('R') or standing_on.startswith('N'):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        set_character_sprite(2,dialouge[0])
        write_text("[TALK]")
        enable_movement_controls()
    elif standing_on.startswith('Q'):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        set_character_sprite(2,dialouge[0])
        write_text("[QUEST]")
        enable_movement_controls()
    elif standing_on.startswith("C"):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        set_character_sprite(2,dialouge[0])
        write_text("[CHEST]")
        enable_movement_controls()
    elif standing_on.startswith("D"):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        set_character_sprite(2,dialouge[0])
        write_text("[ENTERANCE]")
        enable_movement_controls()
    elif standing_on.startswith("H"):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        set_character_sprite(2,dialouge[0])
        write_text("[SHRINE]")
        enable_movement_controls()
    elif standing_on.startswith("S"):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        #set_big_character_sprite(dialouge[0])
        set_character_sprite(2,dialouge[0])
        write_text("[SHOP]")
        enable_movement_controls()
    elif standing_on.startswith("P"):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        #print(dialogue[0])
        set_character_sprite(2,dialouge[0])
        write_text("[PAWN]")
        enable_movement_controls()
    elif standing_on.startswith("F") or standing_on.startswith("E"):
        dialouge_file = standing_on
        dialouge = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+standing_on+".txt")]
        set_character_sprite(2,dialouge[0])
        start_dialogue(dialouge_file)
    elif standing_on.startswith("W") or standing_on.startswith("w"):
        set_character_sprite(2,"warp")
        write_text("[WARP]")
        dialouge_file = "warp"
        enable_movement_controls()
    elif standing_on.startswith("s"):
        standing_on = maps.return_tile_on()
        print("STANDING ON: "+standing_on)
        swap_number = standing_on.replace("s","")
        print("swap_number: "+swap_number)
        traveling_to = "r" + swap_number
        print("traveling_to: "+traveling_to)
        row_index = 0
        col_index = 0
        for row in maps.current_location[1]:
            print(row)
            col_index = 0
            for thing in row:
                print(thing)
                print(thing[0])
                if thing[0] == traveling_to:
                    print("SWAP RECIEVER FOUND")
                    maps.player_tracking[maps.player_cords[1]][maps.player_cords[0]] = [""]
                    maps.player_tracking[row_index][col_index] = ["player"]
                col_index += 1
            row_index += 1
        write_text("STEPPED ON A SWAP TILE!\n\nSENDING TO RECIEVER TILE!")
        talk_button.config(command=refresh)
        g_command = "refresh()"
        space_command = "refresh()"
    elif standing_on.startswith("r"):
        write_text("[SWAP RECIEVER TILE]")
        enable_movement_controls()
def update_party_text():
    member_index = 0
    party_member1.config(text=characters.Current_Party[member_index].DisplayName + "  HP " + str(characters.Current_Party[member_index].Current_HP) + "/" + str(characters.Current_Party[member_index].Max_HP) + "  SP " + str(characters.Current_Party[member_index].Current_SP) + "/" + str(characters.Current_Party[member_index].Max_SP) + "  PR " + str(characters.Current_Party[member_index].Priority))
    if characters.Current_Party[member_index].Current_HP <= 0:
        party_member1.config(fg='grey33')
    elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.33:
        party_member1.config(fg='red')
    elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.66:
        party_member1.config(fg='dark orange')
    else:
        party_member1.config(fg='green2')

    if len(characters.Current_Party) >= 2:
        member_index = 1
        party_member2.config(text=characters.Current_Party[member_index].DisplayName + "  HP " + str(characters.Current_Party[member_index].Current_HP) + "/" + str(characters.Current_Party[member_index].Max_HP) + "  SP " + str(characters.Current_Party[member_index].Current_SP) + "/" + str(characters.Current_Party[member_index].Max_SP) + "  PR " + str(characters.Current_Party[member_index].Priority))
        if characters.Current_Party[member_index].Current_HP <= 0:
            party_member2.config(fg='grey33')
        elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.33:
            party_member2.config(fg='red')
        elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.66:
            party_member2.config(fg='dark orange')
        else:
            party_member2.config(fg='green2')
    else:
        party_member2.config(text="=EMPTY=")

    if len(characters.Current_Party) >= 3:
        member_index = 2
        party_member3.config(text=characters.Current_Party[member_index].DisplayName + "  HP " + str(characters.Current_Party[member_index].Current_HP) + "/" + str(characters.Current_Party[member_index].Max_HP) + "  SP " + str(characters.Current_Party[member_index].Current_SP) + "/" + str(characters.Current_Party[member_index].Max_SP) + "  PR " + str(characters.Current_Party[member_index].Priority))
        if characters.Current_Party[member_index].Current_HP <= 0:
            party_member3.config(fg='grey33')
        elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.33:
            party_member3.config(fg='red')
        elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.66:
            party_member3.config(fg='dark orange')
        else:
            party_member3.config(fg='green2')
    else:
        party_member3.config(text="=EMPTY=")

    if len(characters.Current_Party) >= 4:
        member_index = 3
        party_member4.config(text=characters.Current_Party[member_index].DisplayName + "  HP " + str(characters.Current_Party[member_index].Current_HP) + "/" + str(characters.Current_Party[member_index].Max_HP) + "  SP " + str(characters.Current_Party[member_index].Current_SP) + "/" + str(characters.Current_Party[member_index].Max_SP) + "  PR " + str(characters.Current_Party[member_index].Priority))
        if characters.Current_Party[member_index].Current_HP <= 0:
            party_member4.config(fg='grey33')
        elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.33:
            party_member4.config(fg='red')
        elif characters.Current_Party[member_index].Current_HP <= characters.Current_Party[member_index].Max_HP*0.66:
            party_member4.config(fg='dark orange')
        else:
            party_member4.config(fg='green2')
    else:
        party_member4.config(text="=EMPTY=")

def update_minimap():
    global vision_facing
    cords = maps.return_player_cords()
    minimap_00.config(text=map_icon(maps.current_location[1][cords[1]-2][cords[0]-2][0]))
    minimap_01.config(text=map_icon(maps.current_location[1][cords[1]-2][cords[0]-1][0]))
    minimap_02.config(text=map_icon(maps.current_location[1][cords[1]-2][cords[0]][0]))
    minimap_03.config(text=map_icon(maps.current_location[1][cords[1]-2][cords[0]+1][0]))
    minimap_04.config(text=map_icon(maps.current_location[1][cords[1]-2][cords[0]+2][0]))

    minimap_10.config(text=map_icon(maps.current_location[1][cords[1]-1][cords[0]-2][0]))
    minimap_11.config(text=map_icon(maps.current_location[1][cords[1]-1][cords[0]-1][0]))
    minimap_12.config(text=map_icon(maps.current_location[1][cords[1]-1][cords[0]][0]))
    minimap_13.config(text=map_icon(maps.current_location[1][cords[1]-1][cords[0]+1][0]))
    minimap_14.config(text=map_icon(maps.current_location[1][cords[1]-1][cords[0]+2][0]))

    minimap_20.config(text=map_icon(maps.current_location[1][cords[1]][cords[0]-2][0]))
    minimap_21.config(text=map_icon(maps.current_location[1][cords[1]][cords[0]-1][0]))
    
    minimap_23.config(text=map_icon(maps.current_location[1][cords[1]][cords[0]+1][0]))
    minimap_24.config(text=map_icon(maps.current_location[1][cords[1]][cords[0]+2][0]))

    minimap_30.config(text=map_icon(maps.current_location[1][cords[1]+1][cords[0]-2][0]))
    minimap_31.config(text=map_icon(maps.current_location[1][cords[1]+1][cords[0]-1][0]))
    minimap_32.config(text=map_icon(maps.current_location[1][cords[1]+1][cords[0]][0]))
    minimap_33.config(text=map_icon(maps.current_location[1][cords[1]+1][cords[0]+1][0]))
    minimap_34.config(text=map_icon(maps.current_location[1][cords[1]+1][cords[0]+2][0]))

    minimap_40.config(text=map_icon(maps.current_location[1][cords[1]+2][cords[0]-2][0]))
    minimap_41.config(text=map_icon(maps.current_location[1][cords[1]+2][cords[0]-1][0]))
    minimap_42.config(text=map_icon(maps.current_location[1][cords[1]+2][cords[0]][0]))
    minimap_43.config(text=map_icon(maps.current_location[1][cords[1]+2][cords[0]+1][0]))
    minimap_44.config(text=map_icon(maps.current_location[1][cords[1]+2][cords[0]+2][0]))

    if vision_facing == "North":
        minimap_22.config(text="△")
    elif vision_facing == "South":
        minimap_22.config(text="▽")  
    elif vision_facing == "East":
        minimap_22.config(text="▷")  
    elif vision_facing == "West":
        minimap_22.config(text="◁")  

def map_icon(thing):
    if thing.startswith("T"):
        return "T"
    elif thing.startswith("N") == True:
        return "-"
    elif thing.startswith("C") == True:
        return "C"
    elif thing.startswith("Q") == True:
        return "Q"
    elif thing.startswith("R") == True:
        return "R"
    elif thing.startswith("S") == True:
        return "$"
    elif thing.startswith("H") == True:
        return "H"
    elif thing.startswith("D") == True:
        return "[]"
    elif thing.startswith("P") == True:
        return "P"
    elif thing.startswith("E") == True:
        return "?"
    elif thing.startswith("F") == True:
        return "!"
    elif thing.startswith("---") == True:
        return "■"
    elif thing.startswith("_") == True:
        return "□"
    elif thing.startswith("w") == True or thing.startswith("W") == True:
        return "()"
    elif thing.startswith("s") == True:
        return "⦾"
    elif thing.startswith("r") == True:
        return "⦻"
    elif thing.startswith("000") == True or thing.startswith("n") or thing.startswith("-"):
        return ""
    else:
        return "error"
    
def generate_background():
    global vision_facing
    global bottomest_background_sprite_unform
    global bottomest_background_sprite
    global bottomest_background_image

    global bottomerer_background_sprite
    global bottomerer_background_image
    global bottomer_background_sprite
    global bottomer_background_image
    global bottom_background_sprite
    global bottom_background_image
    global top_background_sprite
    global top_background_image

    cords = maps.return_player_cords()
    if "n" in maps.current_location[1][cords[1]][cords[0]][0]:
        bottomest_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/bottomest_layer/"+maps.current_location[9]+".png").convert("RGBA")
        bottomest_background_sprite = ImageTk.PhotoImage(bottomest_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
        sprites_canvas.itemconfig(bottomest_background_image, image = bottomest_background_sprite)
    else:
        bottomest_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/bottomest_layer/"+maps.current_location[3]+".png").convert("RGBA")
        bottomest_background_sprite = ImageTk.PhotoImage(bottomest_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
        sprites_canvas.itemconfig(bottomest_background_image, image = bottomest_background_sprite)
    print("")
    top = []
    bottom = []
    bottomer = []
    bottomerer = []
    if vision_facing == "North":
        loc = maps.current_location[1][cords[1]-3][cords[0]-2][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]-3][cords[0]-1][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]-3][cords[0]+1][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]-3][cords[0]+2][0]
        bottomerer.append(loc)

        loc = maps.current_location[1][cords[1]-2][cords[0]-2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]-1][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-3][cords[0]][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]+1][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]+2][0]
        bottomer.append(loc)

        loc = maps.current_location[1][cords[1]-1][cords[0]-2][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]-1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]+1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]+2][0]
        bottom.append(loc)
        
        loc = maps.current_location[1][cords[1]][cords[0]-1][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]+1][0]
        top.append(loc)   
    elif vision_facing == "East":
        loc = maps.current_location[1][cords[1]-2][cords[0]+3][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]+3][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]+3][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]+3][0]
        bottomerer.append(loc)
        
        loc = maps.current_location[1][cords[1]-2][cords[0]+2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]+2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]+3][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]+2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]+2][0]
        bottomer.append(loc)
        
        loc = maps.current_location[1][cords[1]-2][cords[0]+1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]+1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]+2][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]+1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]+1][0]
        bottom.append(loc)
        
        loc = maps.current_location[1][cords[1]-1][cords[0]][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]+1][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]][0]
        top.append(loc)
    elif vision_facing == "South":
        loc = maps.current_location[1][cords[1]+3][cords[0]+2][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]+3][cords[0]+1][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]+3][cords[0]-1][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]+3][cords[0]-2][0]
        bottomerer.append(loc)
        
        loc = maps.current_location[1][cords[1]+2][cords[0]+2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]+1][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+3][cords[0]][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]-1][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]-2][0]
        bottomer.append(loc)

        loc = maps.current_location[1][cords[1]+1][cords[0]+2][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]+1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+2][cords[0]][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]-1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]-2][0]
        bottom.append(loc)

        loc = maps.current_location[1][cords[1]][cords[0]+1][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]-1][0]
        top.append(loc)
    elif vision_facing == "West":
        loc = maps.current_location[1][cords[1]+2][cords[0]-3][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]-3][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]-3][0]
        bottomerer.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]-3][0]
        bottomerer.append(loc)
        

        loc = maps.current_location[1][cords[1]+2][cords[0]-2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]-2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]-3][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]-2][0]
        bottomer.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]-2][0]
        bottomer.append(loc)
       
        loc = maps.current_location[1][cords[1]+2][cords[0]-1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]+1][cords[0]-1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]-2][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]-1][0]
        bottom.append(loc)
        loc = maps.current_location[1][cords[1]-2][cords[0]-1][0]
        bottom.append(loc)
        
        
        loc = maps.current_location[1][cords[1]+1][cords[0]][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]][cords[0]-1][0]
        top.append(loc)
        loc = maps.current_location[1][cords[1]-1][cords[0]][0]
        top.append(loc)
        
    letters_to_check = ["T","N","C","D","E","R","H","P","S","Q","F"]

    if(True): #bottomerer layer
        thing = str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"
        walls = ["1000","0100","0010","0001"]
        lst = bottomerer
        ind = 0
        back_spr_num = ""
        # print("bottomerer")
        # print(lst)
        for x in range(4):
            if(lst[ind] == "---" or lst[ind].startswith("_")):
                # spr = Image.open(thing+walls[ind]+".png").convert("RGBA")
                # spr_sides = Image.open(thing+walls[ind]+"sides.png").convert("RGBA")
                back_spr_num = back_spr_num + "1"
            else:
                # spr = Image.open(thing+"0000.png").convert("RGBA")
                back_spr_num = back_spr_num + "0"
            ind += 1
        ind = 0
        print("bottomerer: "+back_spr_num)
        bottomerer_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+back_spr_num+".png").convert("RGBA")
        bottomerer_background_sprite = ImageTk.PhotoImage(bottomerer_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
        print("bottomer: "+str(bottomerer_background_sprite))
        sprites_canvas.itemconfig(bottomerer_background_image, image = bottomerer_background_sprite)
        # bottomerer_background_sprite = ImageTk.PhotoImage((Image.open(str(current_directory)+"/world/"+world_color+"/bottomerer_layer/"+back_spr_num+".png").resize(dimensions,resample=Image.NEAREST)).resize(dimensions,resample=Image.NEAREST))
        # sprites_canvas.itemconfig(bottomerer_background_image, image = bottomerer_background_sprite)
        # for x in range(4):
        #     sprites_canvas.itemconfig(bottomerer_background_images_sides[ind], image = bottomerer_background_sprites_sides[ind])
        #     sprites_canvas.itemconfig(bottomerer_background_images[ind], image = bottomerer_background_sprites[ind])
        #     sprites_canvas.delete(bottomer_background_sprites[ind])
        #     ind += 1
    if(True): #bottomer layer
        thing = str(current_directory)+"/world/"+world_color+"/bottomer_layer/"
        walls = ["10000","01000","00100","00010","00001"]
        lst = bottomer
        ind = 0
        back_spr_num = ""
        for x in range(5):
            print(lst[ind][0])
            if(ind == 1 or ind == 3):
                spr_size = (100,250)
            else:
                spr_size = (60,175)
            if(lst[ind] == "---" or lst[ind].startswith("_")):
                # sprites_canvas.itemconfig(bottomerimg[ind],image=bottomerspr[ind])
                # spr = Image.open(thing+walls[ind]+".png").convert("RGBA")
                # spr_sides = Image.open(thing+walls[ind]+"sides.png").convert("RGBA")
                # bottomer_background_sprites_sides[ind] = ImageTk.PhotoImage(spr_sides.resize(dimensions,resample=Image.NEAREST))
                # bottomer_background_sprites[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                back_spr_num = back_spr_num + "1"
            elif(lst[ind][0] in letters_to_check):
                print(lst[ind][0]+" is in "+str(letters_to_check))
                tile_file = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+lst[ind]+".txt")]
                # spr_sides = Image.open(thing+"00000.png").convert("RGBA")
                # spr = Image.open(thing+"00000.png").convert("RGBA")
                # print(tile_file[0]+" spr_size: "+str(spr_size))
                # bottomer_background_sprites_sides[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                # bottomer_background_sprites[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                back_spr_num = back_spr_num + "0"
                if ind != 0 and ind != 4:
                    if ind != 2:
                        bottomerspr[ind] = ImageTk.PhotoImage(Image.open(current_directory+"/sprites/"+tile_file[0]+".png").convert("RGBA").resize((100,250),resample=Image.NEAREST))
                    else:
                        bottomerspr[ind] = ImageTk.PhotoImage(Image.open(current_directory+"/sprites/"+tile_file[0]+".png").convert("RGBA").resize((60,175),resample=Image.NEAREST))
                    sprites_canvas.itemconfig(bottomerimg[ind],image=bottomerspr[ind])
                # else:
                #     pass
            else:
                # spr_sides = Image.open(thing+"00000.png").convert("RGBA")
                # spr = Image.open(thing+"00000.png").convert("RGBA")
                # bottomer_background_sprites_sides[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                # bottomer_background_sprites[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                back_spr_num = back_spr_num + "0"
            ind += 1
        ind = 0
        print("bottomer: "+back_spr_num)
        bottomer_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/bottomer_layer/"+back_spr_num+".png").convert("RGBA")
        bottomer_background_sprite = ImageTk.PhotoImage(bottomer_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
        sprites_canvas.itemconfig(bottomer_background_image, image = bottomer_background_sprite)
        # for x in range(5):
        #     sprites_canvas.itemconfig(bottomer_background_images_sides[ind], image = bottomer_background_sprites_sides[ind])
        #     sprites_canvas.itemconfig(bottomer_background_images[ind], image = bottomer_background_sprites[ind])
        #     sprites_canvas.delete(bottom_background_sprites[ind])
        #     ind += 1
    if(True): #bottom layer
        thing = str(current_directory)+"/world/"+world_color+"/bottom_layer/"
        walls = ["10000","01000","00100","00010","00001"]
        lst = bottom
        ind = 1
        back_spr_num = ""
        print(lst)
        for x in range(3):
            if(ind == 1 or ind == 3):
                spr_size = (150,375)
            else:
                spr_size = (100,250)
            if(lst[ind] == "---" or lst[ind].startswith("_")):
                # spr_sides = Image.open(thing+walls[ind]+"sides.png").convert("RGBA")
                # spr = Image.open(thing+walls[ind]+".png").convert("RGBA")
                # bottom_background_sprites_sides[ind] = ImageTk.PhotoImage(spr_sides.resize(dimensions,resample=Image.NEAREST))
                # bottom_background_sprites[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                back_spr_num = back_spr_num + "1"
            elif(lst[ind][0] in letters_to_check):
                tile_file = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+lst[ind]+".txt")]
                # spr_sides = Image.open(thing+"00000.png").convert("RGBA")
                # spr = Image.open(thing+"00000.png").convert("RGBA")
                # # print(tile_file[0]+" spr_size: "+str(spr_size))
                # bottom_background_sprites_sides[ind] = ImageTk.PhotoImage(spr_sides.resize(dimensions,resample=Image.NEAREST))
                # bottom_background_sprites[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                back_spr_num = back_spr_num + "0"
                if ind != 0 and ind != 4:
                    if ind != 2:
                        bottomspr[ind] = ImageTk.PhotoImage(Image.open(current_directory+"/sprites/"+tile_file[0]+".png").convert("RGBA").resize((165,420),resample=Image.NEAREST))
                    else:
                        bottomspr[ind] = ImageTk.PhotoImage(Image.open(current_directory+"/sprites/"+tile_file[0]+".png").resize((100*mul,250*mul),resample=Image.NEAREST))
                    sprites_canvas.itemconfig(bottomimg[ind],image=bottomspr[ind])
                # else:
                #     pass
            else:
                # spr_sides = Image.open(thing+"00000.png").convert("RGBA")
                # spr = Image.open(thing+"00000.png").convert("RGBA")
                # bottom_background_sprites_sides[ind] = ImageTk.PhotoImage(spr_sides.resize(dimensions,resample=Image.NEAREST))
                # bottom_background_sprites[ind] = ImageTk.PhotoImage(spr.resize(dimensions,resample=Image.NEAREST))
                back_spr_num = back_spr_num + "0"
            ind += 1
        ind = 1
        print("bottom: "+back_spr_num)
        bottom_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/bottom_layer/"+back_spr_num+".png").convert("RGBA")
        bottom_background_sprite = ImageTk.PhotoImage(bottom_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
        sprites_canvas.itemconfig(bottom_background_image, image = bottom_background_sprite)
        # for x in range(3):
        #     sprites_canvas.itemconfig(bottom_background_images_sides[ind], image = bottom_background_sprites_sides[ind])
        #     sprites_canvas.itemconfig(bottom_background_images[ind], image = bottom_background_sprites[ind])
        #     sprites_canvas.delete(bottom_background_sprites[ind])
        #     ind += 1
    if(True): #top layer
        # thing = str(current_directory)+"/world/"+world_color+"/top_layer/"
        # walls = ["100","010","001"]
        lst = top
        ind = 0
        # print("top")
        # print(lst)
        back_spr_num = ""
        for x in range(3):
            spr_size = (165,420)
            if(lst[ind] == "---" or lst[ind].startswith("_")):
                back_spr_num = back_spr_num + "1"
            elif(lst[ind][0] in letters_to_check):
                tile_file = [line.rstrip('\n') for line in open(current_directory+"/dialogue/"+maps.current_location[4]+"/"+lst[ind]+".txt")]
                back_spr_num = back_spr_num + "0"
                if ind == 1:
                    topspr[ind] = ImageTk.PhotoImage(Image.open(current_directory+"/sprites/"+tile_file[0]+".png").convert("RGBA").resize(spr_size,resample=Image.NEAREST))
                    sprites_canvas.itemconfig(topimg[ind],image=topspr[ind])
            else:
                back_spr_num = back_spr_num + "0"
            ind += 1
        ind = 0
        print("top: "+back_spr_num)
        top_background_sprite_unform = Image.open(str(current_directory)+"/world/"+world_color+"/top_layer/"+back_spr_num+".png").convert("RGBA")
        top_background_sprite = ImageTk.PhotoImage(top_background_sprite_unform.resize(dimensions,resample=Image.NEAREST))
        sprites_canvas.itemconfig(top_background_image, image = top_background_sprite)

def clear_other_npcs_sprites():
    bottomerspr[1] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(bottomerimg[1],image=bottomerspr[1])
    # sprites_canvas.delete(bottomerspr[1])
    bottomerspr[2] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(bottomerimg[2],image=bottomerspr[2])
    # sprites_canvas.delete(bottomerspr[2])
    bottomerspr[3] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(bottomerimg[3],image=bottomerspr[3])
    # sprites_canvas.delete(bottomerspr[3])

    bottomspr[1] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(bottomimg[1],image=bottomspr[1])
    # sprites_canvas.delete(bottomspr[1])
    bottomspr[2] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(bottomimg[2],image=bottomspr[2])
    # sprites_canvas.delete(bottomspr[2])
    bottomspr[3] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(bottomimg[3],image=bottomspr[3])
    # sprites_canvas.delete(bottomspr[3])

    topspr[1] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    sprites_canvas.itemconfig(topimg[1],image=topspr[1])
    # sprites_canvas.delete(topspr[1])

    # ind = 1
    # for x in range(3):
    #     sprites_canvas.delete(bottomerspr[ind])
    #     bottomerspr[ind] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    #     sprites_canvas.itemconfig(bottomerimg[ind],image=bottomerspr[ind])
    #     sprites_canvas.delete(bottomerspr[ind])
    #     ind += 1
    # ind = 1
    # for x in range(3):
    #     sprites_canvas.delete(bottomspr[ind])
    #     bottomspr[ind] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    #     sprites_canvas.itemconfig(bottomimg[ind],image=bottomspr[ind])
    #     sprites_canvas.delete(bottomspr[ind])
    #     ind += 1
    # ind = 1
    # for x in range(1):
    #     sprites_canvas.delete(topspr[ind])
    #     topspr[ind] = PhotoImage(file = str(current_directory)+"/sprites/"+"nothing"+".png")
    #     sprites_canvas.itemconfig(topimg[ind],image=topspr[ind])
    #     sprites_canvas.delete(topspr[ind])
    #     ind += 1
    print("clear_other_npcs_sprites()")

def enable_movement_controls():
    global w_command
    global up_command
    up_button.config(command=move_forwards)
    w_command = "move_forwards()"
    up_command = "move_forwards()"

    global s_command
    global down_command
    down_button.config(command=move_backwards)
    s_command = "move_backwards()"
    down_command = "move_backwards()"

    global a_command
    global left_command
    left_button.config(command=move_left)
    a_command = "move_left()"
    left_command = "move_left()"

    global d_command
    global right_command
    right_button.config(command=move_right)
    d_command = "move_right()"
    right_command = "move_right()"

    global r_command
    equip_button.config(command=open_equip)
    r_command = "open_equip()"

    global t_command
    party_button.config(command=open_party)
    t_command = "open_party()"

    global f_command
    item_button.config(command=open_items)
    f_command = "open_items()"

    global g_command
    global space_command
    talk_button.config(command=open_talk)
    g_command = "open_talk()"
    space_command = "open_talk()"

    global one_command
    save_button.config(command=open_save)
    one_command = "open_save()"

    global two_command
    sidestep_button.config(command=sidestep_toggle)
    two_command = "sidestep_toggle()"

    global three_command
    stat_button.config(command=open_stats)
    three_command = "open_stats()"

    global four_command
    key_button.config(command=open_key_items)
    four_command = "open_key_items()"

did_move = False

def move_forwards():
    disable_inputs()

    global did_move
    did_move = True

    print("move forwards")
    global vision_facing
    move_target = []
    cords = maps.return_player_cords()
    down = 0
    right = 0
    if vision_facing == "North":
        move_target = standing_on = maps.current_location[1][cords[1]-1][cords[0]][0]
        down = -1
    elif vision_facing == "East":
        move_target = standing_on = maps.current_location[1][cords[1]][cords[0]+1][0]
        right = 1
    elif vision_facing == "South":
        move_target = standing_on = maps.current_location[1][cords[1]+1][cords[0]][0]
        down = 1
    elif vision_facing == "West":
        move_target = standing_on = maps.current_location[1][cords[1]][cords[0]-1][0]
        right = -1

    if move_target == "---" or move_target.startswith('_'):
        write_text("A wall is blocking your path\nCannot move forwards")
        enable_movement_controls()
    else:
        maps.move_player(down,right)
        refresh()    

def move_backwards():
    disable_inputs()

    global did_move
    did_move = True

    print("move backwards")
    global vision_facing
    move_target = []
    cords = maps.return_player_cords()
    down = 0
    right = 0
    if vision_facing == "North":
        move_target = standing_on = maps.current_location[1][cords[1]+1][cords[0]][0]
        down = 1
    elif vision_facing == "East":
        move_target = standing_on = maps.current_location[1][cords[1]][cords[0]-1][0]
        right = -1
    elif vision_facing == "South":
        move_target = standing_on = maps.current_location[1][cords[1]-1][cords[0]][0]
        down = -1
    elif vision_facing == "West":
        move_target = standing_on = maps.current_location[1][cords[1]][cords[0]+1][0]
        right = 1

    if move_target == "---" or move_target.startswith('_'):
        write_text("A wall is blocking your path\nCannot move backwards")
        enable_movement_controls()
    else:
        maps.move_player(down,right)
        refresh()

def move_left():
    disable_inputs()
    if sidestepping == True:
        global did_move
        did_move = True
        print("move left")
        global vision_facing
        move_target = []
        cords = maps.return_player_cords()
        down = 0
        right = 0
        if vision_facing == "North":
            move_target = standing_on = maps.current_location[1][cords[1]][cords[0]-1][0]
            right = -1
        elif vision_facing == "East":
            move_target = standing_on = maps.current_location[1][cords[1]-1][cords[0]][0]
            down = -1
        elif vision_facing == "South":
            move_target = standing_on = maps.current_location[1][cords[1]][cords[0]+1][0]
            right = 1
        elif vision_facing == "West":
            move_target = standing_on = maps.current_location[1][cords[1]+1][cords[0]][0]
            down = 1

        if move_target == "---" or move_target.startswith('_'):
            write_text("A wall is blocking your path\nCannot move left")
            enable_movement_controls()
        else:
            maps.move_player(down,right)
            refresh()
    else:
        turn_left()

def move_right():
    disable_inputs()
    if sidestepping == True:
        global did_move
        did_move = True
        print("move right")
        global vision_facing
        move_target = []
        cords = maps.return_player_cords()
        down = 0
        right = 0
        if vision_facing == "North":
            move_target = standing_on = maps.current_location[1][cords[1]][cords[0]+1][0]
            right = 1
        elif vision_facing == "East":
            move_target = standing_on = maps.current_location[1][cords[1]+1][cords[0]][0]
            down = 1
        elif vision_facing == "South":
            move_target = standing_on = maps.current_location[1][cords[1]][cords[0]-1][0]
            right = -1
        elif vision_facing == "West":
            move_target = standing_on = maps.current_location[1][cords[1]-1][cords[0]][0]
            down = -1

        if move_target == "---" or move_target.startswith('_'):
            write_text("A wall is blocking your path\nCannot move right")
            enable_movement_controls()
        else:
            maps.move_player(down,right)
            refresh()
    else:
        turn_right()

multiselect_index = 0

def write_multiselect():
    global multiselect_index
    global temporary_text_to_use_in_multi
    global multi_use_displayname
    global list_to_use_in_multi
    for_char_index = 0
    thing_to_write = temporary_text_to_use_in_multi
    if len(list_to_use_in_multi) == 0:
        thing_to_write = thing_to_write + "\n [EMPTY]"
    for char in list_to_use_in_multi:
        if multi_use_displayname == True:
            thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+list_to_use_in_multi[for_char_index].DisplayName
            for_char_index += 1
        else:
            thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+list_to_use_in_multi[for_char_index]
            for_char_index += 1
    return(thing_to_write)

mutliselect_buying = False

def write_multiselect_with_price():
    global multiselect_index
    global temporary_text_to_use_in_multi
    global multi_use_displayname
    global list_to_use_in_multi
    global mutliselect_buying
    global pawn_mul
    for_char_index = 0
    thing_to_write = temporary_text_to_use_in_multi
    if len(list_to_use_in_multi) == 0:
        thing_to_write = thing_to_write + "\n [EMPTY]"
    for char in list_to_use_in_multi:
        if list_to_use_in_multi[for_char_index].Purchasing_Price > 0:
            if mutliselect_buying == True:
                thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+str(round(list_to_use_in_multi[for_char_index].Purchasing_Price*(maps.current_location[8][0]/100)))+"G "+list_to_use_in_multi[for_char_index].DisplayName
                for_char_index += 1
            else:
                thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+str(round(list_to_use_in_multi[for_char_index].Purchasing_Price*pawn_mul*(maps.current_location[8][0]/100)))+"G "+list_to_use_in_multi[for_char_index].DisplayName
                for_char_index += 1
        else:
            thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+"N/A "+list_to_use_in_multi[for_char_index].DisplayName
            for_char_index += 1
    return(thing_to_write)

def write_multiselect_with_hp():
    global multiselect_index
    global temporary_text_to_use_in_multi
    global multi_use_displayname
    global list_to_use_in_multi
    for_char_index = 0
    thing_to_write = temporary_text_to_use_in_multi
    if len(list_to_use_in_multi) == 0:
        thing_to_write = thing_to_write + "\n [EMPTY]"
    for char in list_to_use_in_multi:
        thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+str(list_to_use_in_multi[for_char_index].Current_HP)+"/"+str(list_to_use_in_multi[for_char_index].Max_HP)+" HP "+list_to_use_in_multi[for_char_index].DisplayName
        for_char_index += 1
    return(thing_to_write)

def write_multiselect_with_sp():
    global multiselect_index
    global temporary_text_to_use_in_multi
    global multi_use_displayname
    global list_to_use_in_multi
    for_char_index = 0
    thing_to_write = temporary_text_to_use_in_multi
    if len(list_to_use_in_multi) == 0:
        thing_to_write = thing_to_write + "\n [EMPTY]"
    for char in list_to_use_in_multi:
        thing_to_write = thing_to_write + "\n" + (">" if multiselect_index == for_char_index else "")+str(list_to_use_in_multi[for_char_index].Current_SP)+"/"+str(list_to_use_in_multi[for_char_index].Max_SP)+" SP "+list_to_use_in_multi[for_char_index].DisplayName
        for_char_index += 1
    return(thing_to_write)

def multiselect_move_up_shop():
    print("move up multi")
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    global text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    if multiselect_index == 0:
        multiselect_index = len(list_to_use_in_multi) - 1
    else:
        multiselect_index -= 1
    write_text(write_multiselect_with_price())

def multiselect_move_down_shop():
    print("move down multi")
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    global text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    if multiselect_index == len(list_to_use_in_multi) - 1:
        multiselect_index = 0
    else:
        multiselect_index += 1
    write_text(write_multiselect_with_price())

def multiselect_move_up():
    print("move up multi")
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    global text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    if multiselect_index == 0:
        multiselect_index = len(list_to_use_in_multi) - 1
    else:
        multiselect_index -= 1
    global multi_char_stat_to_show
    if multi_char_stat_to_show == "HP":
        write_text(write_multiselect_with_hp())
    elif multi_char_stat_to_show == "SP":
        write_text(write_multiselect_with_sp())
    else:
        write_text(write_multiselect())

def multiselect_move_down():
    print("move down multi")
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    global text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    if multiselect_index == len(list_to_use_in_multi) - 1:
        multiselect_index = 0
    else:
        multiselect_index += 1
    global multi_char_stat_to_show
    if multi_char_stat_to_show == "HP":
        write_text(write_multiselect_with_hp())
    elif multi_char_stat_to_show == "SP":
        write_text(write_multiselect_with_sp())
    else:
        write_text(write_multiselect())

text_to_use_in_multi = ""
temporary_text_to_use_in_multi = ""
list_to_use_in_multi = []
multi_use_displayname = True

char_stat_return_to = ""
def print_char_stats():
    disable_inputs()
    global char_stat_return_to
    global multiselect_index
    global list_to_use_in_multi
    char = list_to_use_in_multi[multiselect_index]
    currently_equipped_names = []
    for thing in char.Equipped:
        currently_equipped_names.append(thing.DisplayName)
    effects = "Active Effects:\n"
    if len(char.Effects) > 0:
        print(char.DisplayName+" has active effects")
        effect_index = 0
        for effect in char.Effects:
            if effect_index == 3:
                effects = effects+str(effect[1])+"x"+effect[0]+"("+str(effect[2])+"T)\n"
                effect_index = 0
            else:
                effects = effects+str(effect[1])+"x"+effect[0]+"("+str(effect[2])+"T) "
                effect_index += 1
    else:
        print("no active effects on "+char.DisplayName)
        effects = effects + "N/A"

    write_text(char.DisplayName+"\nLv"+str(char.Level)+" EXP: "+str(char.EXP)+"/1000"+"\n Priority: "+str(char.Priority)+"\nHP: "+str(char.Current_HP)+"/"+str(char.Max_HP)+" ("+str(char.HP_Growth)+"% "+"growth)"+"\nSP: "+str(char.Current_SP)+"/"+str(char.Max_SP)+" ("+str(char.SP_Growth)+"% "+"growth)"+"\n ATK: "+str(char.ATK)+" ("+str(char.ATK_Growth)+"% "+"growth)"+"\n MAG: "+str(char.MAG)+" ("+str(char.MAG_Growth)+"% "+"growth)"+"\n HLG: "+str(char.HLG)+" ("+str(char.HLG_Growth)+"% "+"growth)"+"\n DEF: "+str(char.DEF)+" ("+str(char.DEF_Growth)+"% "+"growth)"+"\n RES: "+str(char.RES)+" ("+str(char.RES_Growth)+"% "+"growth)"+"\n\nCan equip:\n"+str(char.Usable_Weapons).replace("[","").replace("]","").replace("'","")+"\n\nWeak to:\n"+str(char.Weakness).replace("[","").replace("]","").replace("'","")+"\n\n"+effects+"\n\nCurrently equipped:\n"+str(currently_equipped_names).replace("[","").replace("]","").replace("'","")+"\n\n[Right] Return")
    global right_command
    global d_command
    right_button.config(command=eval(char_stat_return_to))
    right_command = char_stat_return_to + "()"
    d_command = char_stat_return_to + "()"

def print_char_stats_battle():
    disable_inputs()
    global char_stat_return_to
    global multiselect_index
    global list_to_use_in_multi
    char = list_to_use_in_multi[multiselect_index]
    currently_equipped_names = []
    for thing in char.Equipped:
        currently_equipped_names.append(thing.DisplayName)
    effects = "Active Effects:\n"
    if len(char.Effects) > 0:
        print(char.DisplayName+" has active effects")
        effect_index = 0
        for effect in char.Effects:
            if effect_index == 3:
                effects = effects+str(effect[1])+"x"+effect[0]+"("+str(effect[2])+"T)\n"
                effect_index = 0
            else:
                effects = effects+str(effect[1])+"x"+effect[0]+"("+str(effect[2])+"T) "
                effect_index += 1
    else:
        print("no active effects on "+char.DisplayName)
        effects = effects + "N/A"

    write_text(char.DisplayName+"\nLv"+str(char.Level)+" EXP: "+str(char.EXP)+"/1000"+"\n Priority: "+str(char.Priority)+"\nHP: "+str(char.Current_HP)+"/"+str(char.Max_HP)+" ("+str(char.HP_Growth)+"% "+"growth)"+"\nSP: "+str(char.Current_SP)+"/"+str(char.Max_SP)+" ("+str(char.SP_Growth)+"% "+"growth)"+"\n ATK: "+str(char.ATK)+" ("+str(char.ATK_Growth)+"% "+"growth)"+"\n MAG: "+str(char.MAG)+" ("+str(char.MAG_Growth)+"% "+"growth)"+"\n HLG: "+str(char.HLG)+" ("+str(char.HLG_Growth)+"% "+"growth)"+"\n DEF: "+str(char.DEF)+" ("+str(char.DEF_Growth)+"% "+"growth)"+"\n RES: "+str(char.RES)+" ("+str(char.RES_Growth)+"% "+"growth)"+"\n\nCan equip:\n"+str(char.Usable_Weapons).replace("[","").replace("]","").replace("'","")+"\n\nWeak to:\n"+str(char.Weakness).replace("[","").replace("]","").replace("'","")+"\n\n"+effects+"\n\nCurrently equipped:\n"+str(currently_equipped_names).replace("[","").replace("]","").replace("'","")+"\n\n[Left] Return")
    global left_command
    global a_command
    left_button.config(command=eval(char_stat_return_to))
    left_command = char_stat_return_to + "()"
    a_command = char_stat_return_to + "()"

def open_equip():
    disable_inputs()
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    char_stat_return_to = "open_equip"
    multiselect_index = 0
    text_to_use_in_multi = "Equipment\n[A] Select character\n[Left] Character Stats\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = characters.All_Recruited_Characters
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global e_command
    b_button.config(command=exit_menu)
    e_command = "exit_menu()"
    global q_command
    a_button.config(command=select_char_equip)
    q_command = "select_char_equip()"
    global left_command
    global a_command
    left_button.config(command=print_char_stats)
    left_command = 'print_char_stats()'
    a_command = 'print_char_stats()'

equip_char = None

def select_char_equip():
    disable_inputs()
    global list_to_use_in_multi
    global multiselect_index
    global equip_char
    print("select_char_equip")
    if len(list_to_use_in_multi) == 0:
        pass
    elif multiselect_index > len(list_to_use_in_multi) - 1:
        multiselect_index = len(list_to_use_in_multi) - 1
    elif list_to_use_in_multi[multiselect_index] in characters.All_Recruited_Characters:
        equip_char = list_to_use_in_multi[multiselect_index]
    write_text(equip_char.DisplayName+" equipped: "+str(len(equip_char.Equipped))+"/3\nEquipment inventory: "+str(len(equipment.equipment_inventory))+"/20\n\n[Up] Remove equip\n[Down] Add equip\n[B] Return")
    global up_command
    global w_command
    up_button.config(command=edit_active_equip)
    up_command = "edit_active_equip()"
    w_command = "edit_active_equip()"
    global down_command
    global s_command
    down_button.config(command=edit_inactive_equip)
    down_command = "edit_inactive_equip()"
    s_command = "edit_inactive_equip()"
    global e_command
    b_button.config(command=open_equip)
    e_command = "open_equip()"

def edit_active_equip():
    disable_inputs()
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global equip_stat_return_to
    equip_stat_return_to = "edit_active_equip"
    multiselect_index = 0
    text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Unequip\n[Left] Equipment Stats\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = equip_char.Equipped
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global e_command
    b_button.config(command=select_char_equip)
    e_command = "select_char_equip()"
    global q_command
    a_button.config(command=unequip_equipment)
    q_command = "unequip_equipment()"
    global left_command
    global a_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_equipment_stats)
        left_command = 'print_equipment_stats()'
        a_command = 'print_equipment_stats()'
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'

equip_stat_return_to = ""
item_stat_return_to = ""

def print_item_stats():
    disable_inputs()
    global item_stat_return_to
    global multiselect_index
    global list_to_use_in_multi
    chosen_item = list_to_use_in_multi[multiselect_index]
    write_text(chosen_item.DisplayName + "\n\n" + "Restore "+ (str((chosen_item.Amount*100)-100) + "% of " if chosen_item.Percent_or_Static == "Percent" else str(chosen_item.Amount) + (" ")) + chosen_item.Stat + "\nTarget: " + ("Single" if chosen_item.Target == "Single" else "Party") + "\n\n" + chosen_item.Description + "\n\n [Right] Return")
    global right_command
    global d_command
    right_button.config(command=eval(item_stat_return_to))
    right_command = item_stat_return_to + "()"
    d_command = item_stat_return_to + "()"

def print_equipment_stats():
    disable_inputs()
    global equip_stat_return_to
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    chosen_equip = list_to_use_in_multi[multiselect_index]
    write_text(chosen_equip.DisplayName + "\n\nEquip Type: " + chosen_equip.Equip_Type + "\nDamage Type: " + chosen_equip.Damage_Type + "\nMove Type: " + chosen_equip.Move_Type + "\nTarget: " + chosen_equip.Target + "\nSP Cost: " + str(chosen_equip.SP_Cost) + "\nPriority: " + str(chosen_equip.Priority) + "\nPWR: " + str(chosen_equip.PWR) + "\nHeal Stat: " + ("N/A" if chosen_equip.Heal_Stat == None else chosen_equip.Heal_Stat) + "\n\n" + chosen_equip.Description + "\n\n [Right] Return")
    global right_command
    global d_command
    right_button.config(command=eval(equip_stat_return_to))
    right_command = equip_stat_return_to + "()"
    d_command = equip_stat_return_to + "()"

def unequip_equipment():
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global equip_stat_return_to
    if 0 > len(list_to_use_in_multi) - 1:
        temporary_text_to_use_in_multi = "There is nothing to unequip"
    elif multiselect_index > len(list_to_use_in_multi) - 1:
        multiselect_index = len(list_to_use_in_multi) - 1
        equipment.equipment_inventory.append(list_to_use_in_multi[multiselect_index])
        list_to_use_in_multi.remove(list_to_use_in_multi[multiselect_index])
        if multiselect_index >= len(list_to_use_in_multi):
            multiselect_index = len(list_to_use_in_multi)-1
        temporary_text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Unequip\n[Left] Equipment Stats\n"
        text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Unequip\n[Left] Equipment Stats\n"
    elif len(equipment.equipment_inventory) >= 20:
        temporary_text_to_use_in_multi = "Inventory is full"
    else:
        equipment.equipment_inventory.append(list_to_use_in_multi[multiselect_index])
        list_to_use_in_multi.remove(list_to_use_in_multi[multiselect_index])
        if multiselect_index >= len(list_to_use_in_multi):
            multiselect_index = len(list_to_use_in_multi)-1
        temporary_text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Unequip\n[Left] Equipment Stats\n"
        text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Unequip\n[Left] Equipment Stats\n"
    global left_command
    global a_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_equipment_stats)
        left_command = 'print_equipment_stats()'
        a_command = 'print_equipment_stats()'
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'
    print(str(len(equip_char.Equipped))+"/3 equipped")
    write_text(write_multiselect())
    
def edit_inactive_equip():
    disable_inputs()
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global equip_stat_return_to
    equip_stat_return_to = "edit_inactive_equip"
    multiselect_index = 0
    text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Equip\n[Left] Equipment Stats\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = equipment.equipment_inventory
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global e_command
    b_button.config(command=select_char_equip)
    e_command = "select_char_equip()"
    global q_command
    a_button.config(command=equip_equipment)
    q_command = "equip_equipment()"
    global left_command
    global a_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_equipment_stats)
        left_command = 'print_equipment_stats()'
        a_command = 'print_equipment_stats()'
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'

def equip_equipment():
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global equip_stat_return_to
    global equip_char
    if 0 > len(list_to_use_in_multi) - 1:
        temporary_text_to_use_in_multi = "There is nothing to equip"
    elif multiselect_index > len(list_to_use_in_multi) - 1:
        multiselect_index = len(list_to_use_in_multi) - 1
        if list_to_use_in_multi[multiselect_index].Equip_Type not in equip_char.Usable_Weapons:
            temporary_text_to_use_in_multi = "Incompatible weapon type"
        elif len(equip_char.Equipped) >= 3:
            temporary_text_to_use_in_multi = "Character equipment slots are full"
        else:
            equip_char.Equipped.append(list_to_use_in_multi[multiselect_index])
            equipment.equipment_inventory.remove(list_to_use_in_multi[multiselect_index])
            if multiselect_index >= len(list_to_use_in_multi):
                multiselect_index = len(list_to_use_in_multi)-1
            temporary_text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Equip\n[Left] Equipment Stats\n"
            text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Equip\n[Left] Equipment Stats\n"
    elif len(equip_char.Equipped) >= 3:
        temporary_text_to_use_in_multi = "Character equipment slots are full"
    elif list_to_use_in_multi[multiselect_index].Equip_Type not in equip_char.Usable_Weapons:
        temporary_text_to_use_in_multi = "Incompatible weapon type"
    else:
        equip_char.Equipped.append(list_to_use_in_multi[multiselect_index])
        equipment.equipment_inventory.remove(list_to_use_in_multi[multiselect_index])
        if multiselect_index >= len(list_to_use_in_multi):
            multiselect_index = len(list_to_use_in_multi)-1
        temporary_text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Equip\n[Left] Equipment Stats\n"
        text_to_use_in_multi = str(len(equip_char.Equipped))+"/3 equipped\n[A] Equip\n[Left] Equipment Stats\n"
    global left_command
    global a_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_equipment_stats)
        left_command = 'print_equipment_stats()'
        a_command = 'print_equipment_stats()'
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'
    print(str(len(equip_char.Equipped))+"/3 equipped")
    write_text(write_multiselect())

def open_party():
    disable_inputs()
    write_text("=Party Edit=\n\n[Up] Active party\n[Down] Inactive party members\n[B] Exit")
    global up_command
    global w_command
    up_button.config(command=edit_active_party)
    up_command = "edit_active_party()"
    w_command = "edit_active_party()"
    global down_command
    global s_command
    down_button.config(command=edit_inactive_party)
    down_command = "edit_inactive_party()"
    s_command = "edit_inactive_party()"
    global e_command
    b_button.config(command=exit_menu)
    e_command = "exit_menu()"

edit_party_index = 0
party_names = []

def edit_active_party():
    disable_inputs()
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    char_stat_return_to = "edit_active_party"
    multiselect_index = 0
    text_to_use_in_multi = str(len(characters.Current_Party))+"/4 party members\n[A] Remove from party\n[Left] Character stats\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = characters.Current_Party
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global e_command
    b_button.config(command=open_party)
    e_command = "open_party()"
    global q_command
    a_button.config(command=remove_char_from_active_party)
    q_command = "remove_char_from_active_party()"
    global left_command
    global a_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_char_stats)
        left_command = 'print_char_stats()'
        a_command = 'print_char_stats()'
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'

def remove_char_from_active_party():
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    global equip_char
    if 0 > len(list_to_use_in_multi) - 1:
        temporary_text_to_use_in_multi = "No character selected\n"
    elif list_to_use_in_multi[multiselect_index].DisplayName == "Protipole":
        temporary_text_to_use_in_multi = "Protipole cannot be removed\n"
    else:
        characters.Unequipped_Characters.append(list_to_use_in_multi[multiselect_index])
        characters.Current_Party.remove(list_to_use_in_multi[multiselect_index])
        if multiselect_index > 0:
            multiselect_index -= 1
        temporary_text_to_use_in_multi = str(len(characters.Current_Party))+"/4 party members\n[A] Remove from party\n[Left] Character stats\n"
        text_to_use_in_multi = str(len(characters.Current_Party))+"/4 party members\n[A] Remove from party\n[Left] Character stats\n"
    global left_command
    global a_command
    global q_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_char_stats)
        left_command = 'print_char_stats()'
        a_command = 'print_char_stats()'
        # a_button.config(command=add_char_to_active_party)
        # q_command = "add_char_to_active_party()"
        
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'
    print(str(len(characters.Current_Party))+"/4 party members\n[A] Remove from party\n[Left] Character stats\n")
    write_text(write_multiselect())

def party_edit_remove():
    global edit_party_index
    global party_names
    if edit_party_index > len(characters.Current_Party) - 1:
        write_text('Selection is empty\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n")
    elif characters.Current_Party[edit_party_index].DisplayName == "Protipole":
        write_text('Protipole cannot be removed\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n")
    else:
        char = characters.Current_Party[edit_party_index]
        characters.Current_Party.remove(char)
        characters.Unequipped_Characters.append(char)
        edit_active_party()

def party_edit_up():
    global edit_party_index
    global party_names
    if edit_party_index == 0:
        edit_party_index = len(party_names) - 1
    else:
        edit_party_index -= 1
    
    if len(party_names) == 4:
        write_text('Select character to remove\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n")
    elif len(party_names) == 8:
        write_text('Select character to add\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n"     +(">" if edit_party_index == 4 else "")+party_names[4]+"\n"     +(">" if edit_party_index == 5 else "")+party_names[5]+"\n"     +(">" if edit_party_index == 6 else "")+party_names[6]+"\n"     +(">" if edit_party_index == 7 else "")+party_names[7]+"\n")

def party_edit_down():
    global edit_party_index
    global party_names
    if edit_party_index == len(party_names) - 1:
        edit_party_index = 0
    else:
        edit_party_index += 1
    
    if len(party_names) == 4:
        write_text('Select character to remove\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n")
    elif len(party_names) == 8:
        write_text('Select character to add\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n"     +(">" if edit_party_index == 4 else "")+party_names[4]+"\n"     +(">" if edit_party_index == 5 else "")+party_names[5]+"\n"     +(">" if edit_party_index == 6 else "")+party_names[6]+"\n"     +(">" if edit_party_index == 7 else "")+party_names[7]+"\n")

def party_edit_add():
    global edit_party_index
    global party_names
    if edit_party_index > len(characters.Current_Party) - 1:
        write_text('Selection is empty\n\n'+(">" if edit_party_index == 0 else "")+party_names[0]+"\n"     +(">" if edit_party_index == 1 else "")+party_names[1]+"\n"     +(">" if edit_party_index == 2 else "")+party_names[2]+"\n"     +(">" if edit_party_index == 3 else "")+party_names[3]+"\n"     +(">" if edit_party_index == 4 else "")+party_names[4]+"\n"     +(">" if edit_party_index == 5 else "")+party_names[5]+"\n"     +(">" if edit_party_index == 6 else "")+party_names[6]+"\n"     +(">" if edit_party_index == 7 else "")+party_names[7]+"\n")
    else:
        char = characters.Unequipped_Characters[edit_party_index]
        characters.Unequipped_Characters.remove(char)
        characters.Current_Party.append(char)
        edit_inactive_party()


def edit_inactive_party():
    disable_inputs()
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    char_stat_return_to = "edit_inactive_party"
    multiselect_index = 0
    text_to_use_in_multi = str(len(characters.Current_Party))+"/4 party members\n[A] Add to party\n[Left] Character stats\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = characters.Unequipped_Characters
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global e_command
    b_button.config(command=open_party)
    e_command = "open_party()"
    global q_command
    a_button.config(command=add_char_to_active_party)
    q_command = "add_char_to_active_party()"
    global left_command
    global a_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_char_stats)
        left_command = 'print_char_stats()'
        a_command = 'print_char_stats()'
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'

def add_char_to_active_party():
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    global equip_char
    if 0 > len(list_to_use_in_multi) - 1:
        temporary_text_to_use_in_multi = "No character selected\n"
    elif len(characters.Current_Party) >= 4:
        temporary_text_to_use_in_multi = "Party is full\n"
    else:
        characters.Current_Party.append(list_to_use_in_multi[multiselect_index])
        characters.Unequipped_Characters.remove(list_to_use_in_multi[multiselect_index])
        if multiselect_index > 0:
            multiselect_index -= 1
        temporary_text_to_use_in_multi = str(len(characters.Current_Party))+"/4 party members\n[A] Add to party\n[Left] Character stats\n"
        text_to_use_in_multi = str(len(characters.Current_Party))+"/4 party members\n[A] Add to party\n[Left] Character stats\n"
    global left_command
    global a_command
    global q_command
    if len(list_to_use_in_multi) > 0:
        left_button.config(command=print_char_stats)
        left_command = 'print_char_stats()'
        a_command = 'print_char_stats()'
        # a_button.config(command=add_char_to_active_party)
        # q_command = "add_char_to_active_party()"
        
    else:
        left_button.config(command=nothing)
        left_command = 'nothing()'
        a_command = 'nothing()'
    print(str(len(characters.Current_Party))+"/4 party members\n[A] Add to party\n[Left] Character stats\n")
    write_text(write_multiselect())


def exit_menu():
    disable_inputs()
    refresh()


def open_talk():
    disable_inputs()
    global dialouge_file
    start_dialogue(dialouge_file)

def open_items():
    disable_inputs()
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global in_shop_list
    in_shop_list = False
    global text_to_use_in_multi
    text_to_use_in_multi = "Item Inventory: "+str(len(equipment.item_inventory))+"/20\nUse item:\n\n[A] Select\n[Left] Stats\n[B] Exit\n----------"
    global temporary_text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    global list_to_use_in_multi
    list_to_use_in_multi = equipment.item_inventory
    global multi_use_displayname
    multi_use_displayname = True
    global item_stat_return_to
    item_stat_return_to = "open_items"
    global multiselect_index
    multiselect_index = 0
    global e_command
    if len(list_to_use_in_multi) <= 0:
        write_text("You don't have any items\n[B] Return")
        b_button.config(command=refresh)
        e_command = "refresh()"
    else:
        write_text(write_multiselect())
        up_button.config(command=multiselect_move_up)
        global up_command
        global w_command
        up_command = 'multiselect_move_up()'
        w_command = 'multiselect_move_up()'
        down_button.config(command=multiselect_move_down)
        global down_command
        global s_command
        down_command = 'multiselect_move_down()'
        s_command = 'multiselect_move_down()'
        b_button.config(command=refresh)
        e_command = "refresh()"
        a_button.config(command=use_item)
        global q_command
        q_command = "use_item()"
        left_button.config(command=print_item_stats)
        global left_command
        global a_command
        left_command = 'print_item_stats()'
        a_command = 'print_item_stats()'

def open_key_items():
    disable_inputs()
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global in_shop_list
    in_shop_list = False
    global text_to_use_in_multi
    text_to_use_in_multi = "Key Items:\n- - - - -\n[A] Use | [B] Exit\n- - - - -"
    global temporary_text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    global list_to_use_in_multi
    list_to_use_in_multi = equipment.key_item_inventory
    global multi_use_displayname
    multi_use_displayname = True
    global item_stat_return_to
    item_stat_return_to = "open_key_items"
    global multiselect_index
    multiselect_index = 0
    global e_command
    set_key_background("key_back")
    if multiselect_index < len(equipment.key_item_inventory):
        set_character_sprite(2,equipment.key_item_inventory[multiselect_index].sprite)
        print("key item sprite set")
    else:
        print("no key item at index")
    if len(list_to_use_in_multi) <= 0:
        write_text("You don't have any KEY ITEMS\n[B] Return")
        b_button.config(command=refresh)
        e_command = "refresh()"
    else:
        write_text(write_multiselect())
        up_button.config(command=key_multiselect_move_up)
        global up_command
        global w_command
        up_command = 'key_multiselect_move_up()'
        w_command = 'key_multiselect_move_up()'
        down_button.config(command=key_multiselect_move_down)
        global down_command
        global s_command
        down_command = 'key_multiselect_move_down()'
        s_command = 'key_multiselect_move_down()'
        b_button.config(command=refresh)
        e_command = "refresh()"
        a_button.config(command=use_key_item)
        global q_command
        q_command = "use_key_item()"

def key_multiselect_move_up():
    print("move up multi")
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    global text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    if multiselect_index == 0:
        multiselect_index = len(list_to_use_in_multi) - 1
    else:
        multiselect_index -= 1
    set_character_sprite(2,equipment.key_item_inventory[multiselect_index].sprite)
    print("key item sprite set")
    write_text(write_multiselect())

def key_multiselect_move_down():
    print("move down multi")
    global multiselect_index
    global list_to_use_in_multi
    global temporary_text_to_use_in_multi
    global text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    if multiselect_index == len(list_to_use_in_multi) - 1:
        multiselect_index = 0
    else:
        multiselect_index += 1
    set_character_sprite(2,equipment.key_item_inventory[multiselect_index].sprite)
    print("key item sprite set")
    write_text(write_multiselect())

multi_char_stat_to_show = ""
item_to_use = None

def use_item():
    disable_inputs()
    global multiselect_index
    global list_to_use_in_multi
    global multi_char_stat_to_show
    global item_to_use
    global q_command
    global space_command
    global g_command
    if len(list_to_use_in_multi)-1 <= multiselect_index:
        multiselect_index = len(list_to_use_in_multi) - 1
    if len(list_to_use_in_multi) == 0:
        write_text("You don't have any items\n[B] Return")
        b_button.config(command=refresh)
        global e_command
        e_command = "refresh()"
    else:
        item_to_use = list_to_use_in_multi[multiselect_index]
        if item_to_use.Target == "Single":
            if item_to_use.Stat == "HP":
                multi_char_stat_to_show = "HP"
            else:
                multi_char_stat_to_show = "SP"
            global select_party_member_text
            select_party_member_text = "Select character to use " + item_to_use.DisplayName + " on:\n\n[A] Select\n[Left] Stats\n[B] Close\n----------"
            disable_inputs()
            select_party_member_to_use_item()
        else:
            disable_inputs()
            for char in characters.Current_Party:
                if char.Current_HP <= 0:
                    pass
                elif item_to_use.Stat == "HP":
                    amount_to_heal = 0
                    if item_to_use.Percent_or_Static == "Static":
                        amount_to_heal = item_to_use.Amount
                    elif item_to_use.Percent_or_Static == "Percent":
                        amount_to_heal = char.Max_HP*(item_to_use.Amount-1)
                    if amount_to_heal + char.Current_HP > char.Max_HP:
                        amount_to_heal -= (amount_to_heal+char.Current_HP)-char.Max_HP
                    amount_to_heal = round(amount_to_heal)
                    char.Current_HP += amount_to_heal
                elif item_to_use.Stat == "SP":
                    amount_to_heal = 0
                    if item_to_use.Percent_or_Static == "Static":
                        amount_to_heal = item_to_use.Amount
                    elif item_to_use.Percent_or_Static == "Percent":
                        amount_to_heal = char.Max_SP*(item_to_use.Amount-1)
                    if amount_to_heal + char.Current_SP > char.Max_SP:
                        amount_to_heal -= (amount_to_heal+char.Current_SP)-char.Max_SP
                    amount_to_heal = round(amount_to_heal)
                    char.Current_SP += amount_to_heal
            write_text(item_to_use.DisplayName+" was used!")
            equipment.item_inventory.remove(item_to_use)
            update_party_text()
            e_command = "open_items()"
            b_button.config(command=open_items)
            q_command = "open_items()"
            a_button.config(command=open_items)
            g_command = "open_items()"
            space_command = "open_items()"
            talk_button.config(command=open_items)

def use_key_item():
    disable_inputs()
    global dialogue
    global dialogue_index
    global multiselect_index
    input_file = equipment.key_item_inventory[multiselect_index].text_file
    dialogue_index = 0
    file_contents = open(current_directory+"/dialogue/key_items/"+input_file+".txt")
    dialogue = [line.rstrip('\n') for line in file_contents]
    print(dialogue)
    perform_dialogue()

select_party_member_text = ""

def select_party_member_to_use_item():
    disable_inputs()
    global multiselect_index
    global list_to_use_in_multi
    multiselect_index = 0
    list_to_use_in_multi = characters.All_Recruited_Characters
    global multi_use_displayname
    multi_use_displayname = True
    global text_to_use_in_multi
    global select_party_member_text
    text_to_use_in_multi = select_party_member_text
    global temporary_text_to_use_in_multi
    temporary_text_to_use_in_multi = text_to_use_in_multi
    global char_stat_return_to
    char_stat_return_to = "select_party_member_to_use_item"
    global multi_char_stat_to_show
    if multi_char_stat_to_show == "HP":
        write_text(write_multiselect_with_hp())
    elif multi_char_stat_to_show == "SP":
        write_text(write_multiselect_with_sp())
    else:
        write_text(write_multiselect())
    up_button.config(command=multiselect_move_up)
    global up_command
    global w_command
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    down_button.config(command=multiselect_move_down)
    global down_command
    global s_command
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    b_button.config(command=open_items)
    global e_command
    e_command = "open_items()"
    a_button.config(command=use_item_on_party_member)
    global q_command
    q_command = "use_item_on_party_member()"
    left_button.config(command=print_char_stats)
    global left_command
    global a_command
    left_command = 'print_char_stats()'
    a_command = 'print_char_stats()'

def use_item_on_party_member():
    disable_inputs()
    global list_to_use_in_multi
    global multiselect_index
    char = list_to_use_in_multi[multiselect_index]
    global item_to_use

    global e_command
    global q_command
    global g_command
    global space_command

    if char.Current_HP <= 0:
        write_text("Can't use items on a defeated character.\n[B] Return")
        e_command = "select_party_member_to_use_item()"
        b_button.config(command=select_party_member_to_use_item)
    elif item_to_use.Stat == "HP":
        amount_to_heal = 0
        if item_to_use.Percent_or_Static == "Static":
            amount_to_heal = item_to_use.Amount
        elif item_to_use.Percent_or_Static == "Percent":
            amount_to_heal = char.Max_HP*(item_to_use.Amount-1)
        if amount_to_heal + char.Current_HP > char.Max_HP:
            amount_to_heal -= (amount_to_heal+char.Current_HP)-char.Max_HP
        amount_to_heal = round(amount_to_heal)
        char.Current_HP += amount_to_heal
        write_text(char.DisplayName+" recovered "+str(amount_to_heal)+" HP!")
        equipment.item_inventory.remove(item_to_use)
        update_party_text()
        e_command = "open_items()"
        b_button.config(command=open_items)
        q_command = "open_items()"
        a_button.config(command=open_items)
        g_command = "open_items()"
        space_command = "open_items()"
        talk_button.config(command=open_items)

    elif item_to_use.Stat == "SP":
        amount_to_heal = 0
        if item_to_use.Percent_or_Static == "Static":
            amount_to_heal = item_to_use.Amount
        elif item_to_use.Percent_or_Static == "Percent":
            amount_to_heal = char.Max_SP*(item_to_use.Amount-1)
        if amount_to_heal + char.Current_SP > char.Max_SP:
            amount_to_heal -= (amount_to_heal+char.Current_SP)-char.Max_SP
        amount_to_heal = round(amount_to_heal)
        char.Current_SP += amount_to_heal
        write_text(char.DisplayName+" recovered "+str(amount_to_heal)+" SP!")
        equipment.item_inventory.remove(item_to_use)
        update_party_text()
        e_command = "open_items()"
        b_button.config(command=open_items)
        q_command = "open_items()"
        a_button.config(command=open_items)
        g_command = "open_items()"
        space_command = "open_items()"
        talk_button.config(command=open_items)
        

def open_save():
    disable_inputs()
    write_text("Save game data?\n-----\n[A] Save\n[B] Cancel")
    global q_command
    a_button.config(command=save_data_from_menu)
    q_command = "save_data_from_menu()"
    global e_command
    b_button.config(command=refresh)
    e_command = "refresh()"

def save_data_from_menu():
    disable_inputs()
    save_data()
    write_text("Game saved")
    global q_command
    global g_command
    global space_command
    a_button.config(command=refresh)
    q_command = "refresh()"
    talk_button.config(command=refresh)
    g_command = "refresh()"
    space_command = "refresh()"


def open_stats():
    disable_inputs()
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    char_stat_return_to = "open_stats"
    multiselect_index = 0
    text_to_use_in_multi = "\n- - - - - - - - - - -\nCharacter Stats\n- - - - - - - - - - -\n\n[Left] Select\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = characters.All_Recruited_Characters
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global e_command
    b_button.config(command=exit_menu)
    e_command = "exit_menu()"
    global left_command
    global a_command
    left_button.config(command=print_char_stats)
    left_command = 'print_char_stats()'
    a_command = 'print_char_stats()'

yes_no_result = False
def yes_no_controls():
    disable_inputs()
    global q_command
    global e_command
    a_button.config(command=choose_yes)
    q_command = "choose_yes()"
    b_button.config(command=choose_no)
    e_command = "choose_no()"

def choose_yes():
    disable_inputs()
    clear_text()
    global yes_no_result
    yes_no_result = True
    print(str(yes_no_result))
    perform_dialogue()

def choose_no():
    disable_inputs()
    clear_text()
    global yes_no_result
    yes_no_result = False
    print(str(yes_no_result))
    perform_dialogue()


def start_menu_control_set():
    disable_inputs()
    global q_command
    q_command = "start_menu_load_save()"
    a_button.config(command=start_menu_load_save)
    global e_command
    e_command = "start_menu_new_game()"
    b_button.config(command=start_menu_new_game)

def start_menu_load_save():
    disable_inputs()
    print("menu load save button pressed")
    load_save()
    

def load_save():
    # global Gold
    # stuff = [
    #     maps.List_of_All_Locations,
    #     characters.List_of_All_Recruitable_Party_Members,
    #     characters.Current_Party,
    #     characters.All_Recruited_Characters,
    #     equipment.equipment_inventory,
    #     equipment.item_inventory,
    #     Gold,
    #     maps.current_location
    # ]
    print("reading save...")
    loaded_thing = []
    with open("save.dat", "rb") as f:
        loaded_thing = pickle.load(f)
    #     for _ in range(pickle.load(f)):
    #         thing.append(pickle.load(f))
    print("finished reading save")
    print("loading save...")
    # thing_index = 0
    # for thing in loaded_thing:
    #     stuff[thing_index] = thing
    #     print(stuff[thing_index])
    #     thing_index += 1
    global Gold
    global vision_facing
    unformatted_locations = loaded_thing[0]
    for unform_loc in unformatted_locations:
        for loc in maps.List_of_All_Locations:
            if unform_loc[4] == loc[4]:
                print("unform_loc and loc match found")
                for map in maps.List_of_All_Maps:
                    if loc[1] == map:
                        print("map match found")
                        thing_index = 0
                        for linething in unform_loc[1]:
                            map[thing_index] = linething
                            thing_index += 1
                        loc[8] = unform_loc[8]
                        #map = unform_loc[1]
                loc[7] = unform_loc[7]

    characters.List_of_All_Recruitable_Party_Members = loaded_thing[1]
    characters.Current_Party = loaded_thing[2]
    characters.All_Recruited_Characters = loaded_thing[3]
    equipment.equipment_inventory = loaded_thing[4]
    equipment.item_inventory = loaded_thing[5]
    Gold = loaded_thing[6]
    maps.current_location = loaded_thing[7]
    maps.player_tracking = loaded_thing[8]
    vision_facing = loaded_thing[9]
    characters.Unequipped_Characters = loaded_thing[10]
    equipment.key_item_inventory = loaded_thing[11]
    print("finished loading save")
    #print(maps.player_tracking)
    if maps.current_location[10] == "safe":
        print("SAVE ZONE, AUTOSAVING...")
        autosave_data()
    else:
        print("ZONE IS NOT SAFE, WILL NOT AUTOSAVE")
    refresh()

def load_autosave():
    print("reading autosave...")
    loaded_thing = []
    with open("autosave.dat", "rb") as f:
        loaded_thing = pickle.load(f)
    print("finished reading save")
    print("loading save...")
    global Gold
    global vision_facing
    unformatted_locations = loaded_thing[0]
    for unform_loc in unformatted_locations:
        for loc in maps.List_of_All_Locations:
            if unform_loc[4] == loc[4]:
                print("unform_loc and loc match found")
                for map in maps.List_of_All_Maps:
                    if loc[1] == map:
                        print("map match found")
                        thing_index = 0
                        for linething in unform_loc[1]:
                            map[thing_index] = linething
                            thing_index += 1
                        loc[8] = unform_loc[8]
                        #map = unform_loc[1]
                loc[7] = unform_loc[7]
    characters.List_of_All_Recruitable_Party_Members = loaded_thing[1]
    characters.Current_Party = loaded_thing[2]
    characters.All_Recruited_Characters = loaded_thing[3]
    equipment.equipment_inventory = loaded_thing[4]
    equipment.item_inventory = loaded_thing[5]
    Gold = loaded_thing[6]
    maps.current_location = loaded_thing[7]
    maps.player_tracking = loaded_thing[8]
    vision_facing = loaded_thing[9]
    characters.Unequipped_Characters = loaded_thing[10]
    equipment.key_item_inventory = loaded_thing[11]
    print("finished loading save")
    refresh()

def save_data():
    global Gold
    global vision_facing
    stuff = [
        maps.List_of_All_Locations,
        characters.List_of_All_Recruitable_Party_Members,
        characters.Current_Party,
        characters.All_Recruited_Characters,
        equipment.equipment_inventory,
        equipment.item_inventory,
        Gold,
        maps.current_location,
        maps.player_tracking,
        vision_facing,
        characters.Unequipped_Characters,
        equipment.key_item_inventory
    ]
    with open("save.dat", "wb") as f:
        pickle.dump(stuff, f)

def autosave_data():
    global Gold
    global vision_facing
    stuff = [
        maps.List_of_All_Locations,
        characters.List_of_All_Recruitable_Party_Members,
        characters.Current_Party,
        characters.All_Recruited_Characters,
        equipment.equipment_inventory,
        equipment.item_inventory,
        Gold,
        maps.current_location,
        maps.player_tracking,
        vision_facing,
        characters.Unequipped_Characters,
        equipment.key_item_inventory
    ]
    with open("autosave.dat", "wb") as f:
        pickle.dump(stuff, f)

def start_menu_new_game():
    if maps.current_location[10] == "safe":
        print("SAVE ZONE, AUTOSAVING...")
        autosave_data()
    else:
        print("ZONE IS NOT SAFE, WILL NOT AUTOSAVE")
    start_dialogue_direct("/dialogue/bieace_castle/intro.txt")

character_to_action_index = 0
def Combat_Start_Player_Turn():
    disable_inputs()
    update_party_text()
    for char in characters.Current_Party:
        if len(char.Effects) > 0:
            for effect in char.Effects:
                effect[2] -= 1
                if effect[2] <= 0:
                    char.Effects.remove(effect)
    global character_to_action_index
    character_to_action_index = 0
    Character_Turn()

check_enemy_stat_return_to = ""
Current_Character = None

def Character_Turn():
    disable_inputs()
    update_party_text()
    global space_command
    global q_command
    global left_command
    global e_command
    global character_to_action_index
    global down_command
    global a_command
    global d_command
    global right_command
    global Current_Character # iwehjrdfoiwqejfidpqwjfdiowqjfiowqjfiowqjfiowqjiowqjfoiwqjfioqwjfiowqj
    if len(characters.Current_Party)-1 >= character_to_action_index:
        Current_Character = characters.Current_Party[character_to_action_index]
        if Current_Character.Current_HP > 0:
            write_text(Current_Character.DisplayName+"'s turn\n-----\n[A] Attack\n[B] Defend\n[Left] Enemy Stats\n[Right] Party Stats")
            #global q_command
            q_command = "Select_Move()"
            a_button.config(command=Select_Move)

            #global e_command
            b_button.config(command=Confirm_Defend)
            e_command = "Confirm_Defend()"

            a_command = "Select_Enemy_to_Check_Stats()"
            left_command = "Select_Enemy_to_Check_Stats()"
            left_button.config(command=Select_Enemy_to_Check_Stats)

            d_command = "Select_Party_Member_to_Check_Stats()"
            right_command = "Select_Party_Member_to_Check_Stats()"
            right_button.config(command=Select_Party_Member_to_Check_Stats)
        else:   
            write_text(Current_Character.DisplayName+" is defeated and cannot act!")    
            talk_button.config(command=Next_Char_Turn)
            a_button.config(command=Next_Char_Turn)
            space_command = "Next_Char_Turn()"
            q_command = "Next_Char_Turn()"
    else:
        write_text("Enemy Turn")
        character_to_action_index = 0
        for enem in current_encounter:
            if len(enem.Effects) > 0:
                for effect in enem.Effects:
                    effect[2] -= 1
                    if effect[2] <= 0:
                        enem.Effects.remove(effect)
        Enemy_Turn()

def Enemy_Turn():
    disable_inputs()
    update_party_text()
    global space_command
    global q_command
    global left_command
    global e_command
    global character_to_action_index
    global down_command
    global a_command
    global d_command
    global right_command
    global current_encounter
    global Current_Character
    global Move_to_Use
    global target
    global Move_Target
    global another
    if len(current_encounter)-1 >= character_to_action_index:
        print("character_to_action_index = "+str(character_to_action_index))
        Current_Character = current_encounter[character_to_action_index]
        moves_possible = 0
        for move in Current_Character.Moves:
            if move[0].SP_Cost <= Current_Character.Current_SP:
                if (Current_Character.Current_HP/Current_Character.Max_HP)*100 >= move[1] and (Current_Character.Current_HP/Current_Character.Max_HP)*100 <= move[2]:
                    print("USABLE "+move[0].DisplayName+" "+str(move[2])+" >= "+str(Current_Character.Current_HP/Current_Character.Max_HP*100)+"HP >= "+str(move[1]))
                    moves_possible += 1
                else:
                    print("NOT USABLE "+move[0].DisplayName+" "+str(move[2])+" >= "+str(Current_Character.Current_HP/Current_Character.Max_HP*100)+"HP >= "+str(move[1]))
                
        if moves_possible == 0:
            write_text(Current_Character.DisplayName+" did nothing")
            character_to_action_index += 1
            talk_button.config(command=Enemy_Turn)
            a_button.config(command=Enemy_Turn)
            space_command = "Enemy_Turn()"
            q_command = "Enemy_Turn()"
        else:
            possible_moves = []
            for move in Current_Character.Moves:
                if move[0].SP_Cost <= Current_Character.Current_SP:
                    if (Current_Character.Current_HP/Current_Character.Max_HP)*100 >= move[1] and (Current_Character.Current_HP/Current_Character.Max_HP)*100 <= move[2]:
                        possible_moves.append(move[0])
            Move_to_Use = possible_moves[random.randint(0,len(possible_moves)-1)]
            print("move to use: "+Move_to_Use.DisplayName)
            total_priority = 0
            possible_targets = []
            for char in characters.Current_Party:
                if char.Current_HP > 0:
                    total_priority += char.Priority
                    current_total_priority = str(total_priority)
                    possible_targets.append([char,int(current_total_priority)])
            if len(possible_targets) >= 1:
                if total_priority > 0:
                    target_priority = str(random.randint(0,total_priority))
                    print(target_priority)
                    print(target_priority)
                    print(target_priority)
                    target = []
                    for char in possible_targets:
                        if char[1] >= int(target_priority):
                            print(char[0].DisplayName+" "+str(char[1])+" greater than or equal to "+target_priority+" [TARGET]")
                            target.append(char[0])
                            break
                        else:
                            print(char[0].DisplayName+" "+str(char[1])+" less than "+target_priority+" [NOT TARGET]")
                    print("target: "+str(target)+" | first displayname: "+target[0].DisplayName)
                else:
                    target = []
                    print("total priority is 0")
                    print("len(possible_targets) = " + str(len(possible_targets)))
                    target.append(possible_targets[random.randint(0,len(possible_targets)-1)][0])
                    print("target: "+str(target)+" | first displayname: "+target[0].DisplayName)
                if Move_to_Use.Target == "Single Ally":
                    print("SINGLE ALLY TARGET")
                    target = None
                    lowest_hp = -1
                    possible_targets = []
                    for enemy in current_encounter:
                        if (enemy.Max_HP-enemy.Current_HP) > lowest_hp:
                            print("new target, "+str(enemy.Max_HP-enemy.Current_HP)+" (hp lost) is more than "+str(lowest_hp))
                            target = [enemy]
                            lowest_hp = (enemy.Max_HP-enemy.Current_HP)
                        else:
                            print("no target change, "+str(enemy.Max_HP-enemy.Current_HP)+" (hp lost) is less than "+str(lowest_hp))
                elif Move_to_Use.Target == "All Allies":
                    target = current_encounter
                elif Move_to_Use.Target == "All Enemies":
                    target = []
                    for char in characters.Current_Party:
                        if char.Current_HP > 0:
                            target.append(char)
                elif Move_to_Use.Target == "Self":
                    target = []
                    target.append(Current_Character)
                Move_Target = target
                print("target: "+str(target)+" | first displayname: "+target[0].DisplayName)
                write_text(Current_Character.DisplayName+" used "+Move_to_Use.DisplayName)
                talk_button.config(command=initialize_enemy_move)
                a_button.config(command=initialize_enemy_move)
                space_command = "initialize_enemy_move()"
                q_command = "initialize_enemy_move()"

            else:
                write_text(Current_Character.DisplayName+" did nothing")
                character_to_action_index += 1
                talk_button.config(command=Enemy_Turn)
                a_button.config(command=Enemy_Turn)
                space_command = "Enemy_Turn()"
                q_command = "Enemy_Turn()"



        
    else:
        write_text("Player Turn")
        for enem in current_encounter:
            enem.Current_Action_Count = 0
        character_to_action_index = 0
        talk_button.config(command=Combat_Start_Player_Turn)
        a_button.config(command=Combat_Start_Player_Turn)
        space_command = "Combat_Start_Player_Turn()"
        q_command = "Combat_Start_Player_Turn()"


def Next_Char_Turn():
    global character_to_action_index
    character_to_action_index += 1
    Character_Turn()

def Confirm_Defend():
    disable_inputs()
    write_text("Defend and reduce PR by 100?\n[A] Defend\n[B] Cancel")
    global q_command
    q_command = "Defend()"
    a_button.config(command=Defend)
    global e_command
    e_command = "Character_Turn()"
    b_button.config(command=Character_Turn)

def Defend():
    disable_inputs()
    global Current_Character
    Current_Character.Priority -= 100
    if Current_Character.Priority < 0:
        Current_Character.Priority = 0
    global perform_move_index
    #perform_move_index += 1
    write_text(Current_Character.DisplayName+" defended")
    update_party_text()
    global q_command
    global space_command
    q_command = "Next_Char_Turn()"
    space_command = "Next_Char_Turn()"
    talk_button.config(command=Next_Char_Turn)
    a_button.config(command=Next_Char_Turn)

def Select_Move():
    disable_inputs()
    global Current_Character
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global equip_stat_return_to
    equip_stat_return_to = "Select_Move"
    multiselect_index = 0
    text_to_use_in_multi = "Select Move\n-----\n[A] Select move\n[Left] Move stats\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = Current_Character.Equipped
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    if len(Current_Character.Equipped) > 0:
        global left_command
        global a_command
        left_button.config(command=print_equipment_stats)
        left_command = "print_equipment_stats()"
        a_command = "print_equipment_stats()"
        global q_command
        a_button.config(command=Move_Has_Been_Selected)
        q_command = "Move_Has_Been_Selected()"
    global e_command
    b_button.config(command=Character_Turn)
    e_command = 'Character_Turn()'

Move_to_Use = None
def Move_Has_Been_Selected ():
    disable_inputs()
    global Move_to_Use
    global list_to_use_in_multi
    global multiselect_index
    Move_to_Use = list_to_use_in_multi[multiselect_index]
    Select_Move_Target()

Move_Target = []
Targeting_Type = "" #Enemy or Ally
Target_All = False
def Select_Move_Target():
    disable_inputs()
    global Move_to_Use
    global Move_Target
    global Current_Character
    global Targeting_Type
    global Target_All
    global multi_char_stat_to_show
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global check_enemy_stat_return_to
    global char_stat_return_to
    global up_command
    global w_command
    global down_command
    global s_command
    global left_command
    global a_command
    global q_command
    global e_command
    global current_encounter
    if Move_to_Use.Target == "Single Enemy":
        Targeting_Type = "Enemy"
        Target_All = False
        multi_char_stat_to_show = None
        check_enemy_stat_return_to = "Select_Move_Target"
        multiselect_index = 0
        text_to_use_in_multi = "Select Target\n-----\n[A] Select target\n[Left] Enemy stats\n"
        temporary_text_to_use_in_multi = text_to_use_in_multi
        list_to_use_in_multi = current_encounter
        multi_use_displayname = True
        write_text(write_multiselect())
        up_button.config(command=multiselect_move_up)
        up_command = 'multiselect_move_up()'
        w_command = 'multiselect_move_up()'
        down_button.config(command=multiselect_move_down)
        down_command = 'multiselect_move_down()'
        s_command = 'multiselect_move_down()'
        left_button.config(command=print_enemy_stats)
        left_command = "print_enemy_stats()"
        a_command = "print_enemy_stats()"
        a_button.config(command=Initialize_Perform_Move)
        q_command = "Initialize_Perform_Move()"
        b_button.config(command=Select_Move)
        e_command = 'Select_Move()'
    elif Move_to_Use.Target == "Single Ally":
        Targeting_Type = "Ally"
        Target_All = False
        multi_char_stat_to_show = None
        char_stat_return_to = "Select_Move_Target"
        multiselect_index = 0
        text_to_use_in_multi = "Select Target\n-----\n[A] Select target\n[Left] Ally stats\n"
        temporary_text_to_use_in_multi = text_to_use_in_multi
        allies_alive = []
        for char in characters.Current_Party:
            if char.Current_HP > 0:
                allies_alive.append(char)
        list_to_use_in_multi = allies_alive
        multi_use_displayname = True
        write_text(write_multiselect())
        up_button.config(command=multiselect_move_up)
        up_command = 'multiselect_move_up()'
        w_command = 'multiselect_move_up()'
        down_button.config(command=multiselect_move_down)
        down_command = 'multiselect_move_down()'
        s_command = 'multiselect_move_down()'
        left_button.config(command=print_char_stats)
        left_command = "print_char_stats()"
        a_command = "print_char_stats()"
        a_button.config(command=Initialize_Perform_Move)
        q_command = "Initialize_Perform_Move()"
        b_button.config(command=Select_Move)
        e_command = 'Select_Move()'
    elif Move_to_Use.Target == "All Enemies":
        Targeting_Type = "Enemy"
        Target_All = True
        Move_Target = []
        for enem in current_encounter:
            Move_Target.append(enem)
        Initialize_Perform_Move()
    elif Move_to_Use.Target == "All Allies":
        Targeting_Type = "Ally"
        Target_All = True
        Move_Target = []
        for char in characters.Current_Party:
            if char.Current_HP > 0:
                Move_Target.append(char)
        Initialize_Perform_Move()
    elif Move_to_Use.Target == "Self":
        Targeting_Type = "Self"
        Target_All = False
        Move_Target = []
        Move_Target.append(Current_Character)
        Initialize_Perform_Move()

perform_move_index = 0

def Initialize_Perform_Move():
    disable_inputs()
    print("Initialize_Perform_Move")
    global Targeting_Type
    global Move_Target
    global list_to_use_in_multi
    global multiselect_index
    global perform_move_index
    global current_encounter
    if Current_Character.Current_SP < Move_to_Use.SP_Cost:
            write_text("Not enought SP")
            global q_command
            a_button.config(command=Select_Move)
            q_command = "Select_Move()"
            global space_command
            talk_button.config(command=Select_Move)
            space_command = "Select_Move()"
            global e_command
            b_button.config(command=Select_Move)
            e_command = "Select_Move()"
    else:
        Current_Character.Current_SP -= Move_to_Use.SP_Cost
        Current_Character.Priority += Move_to_Use.Priority
        update_party_text()
        if Target_All == False and Targeting_Type != "Self":
            Move_Target = []
            Move_Target.append(list_to_use_in_multi[multiselect_index])
        perform_move_index = 0
        Perform_Move()

def initialize_enemy_move():
    disable_inputs()
    print("initialize_enemy_move")
    global Targeting_Type
    global Move_Target
    global list_to_use_in_multi
    global multiselect_index
    global perform_move_index
    global current_encounter
    Current_Character.Current_SP -= Move_to_Use.SP_Cost
    global perform_move_index
    perform_move_index = 0
    update_party_text()
    Enemy_Perform_Move()

another = False

def Enemy_Perform_Again():
    disable_inputs()
    global another
    global q_command
    global space_command
    global Current_Character
    write_text("Another!\n"+Current_Character.DisplayName+" acts again!")
    another = True
    a_button.config(command=Enemy_Turn)
    talk_button.config(command=Enemy_Turn)
    q_command = "Enemy_Turn()"
    space_command = "Enemy_Turn()"

def Enemy_Perform_Move():
    disable_inputs()
    print("Enemy_Perform_Move")
    global perform_move_index
    global Move_Target
    print("Move Target: "+str(Move_Target))
    global Move_to_Use
    global Current_Character
    global space_command
    global q_command
    global target
    global character_to_action_index
    if perform_move_index <= len(Move_Target)-1:
        target = Move_Target[perform_move_index]
        if Move_to_Use.Move_Type == "Physical":
            print("move is physical")
            def_mul = 1
            wkn_mul = 1
            if len(target.Effects) > 0:
                print("checking effects")
                for effect in target.Effects:
                    if effect[0] == "DEF":
                        def_mul = def_mul*effect[1]
                    elif effect[0] == "WKN":
                        wkn_mul = wkn_mul*effect[1]
            atk_mul = 1
            if len(Current_Character.Effects) > 0:
                print("checking effects")
                for effect in Current_Character.Effects:
                    if effect[0] == "ATK":
                        atk_mul = atk_mul*effect[1]
            print("WKN MUL: "+str(wkn_mul))
            if Move_to_Use.Damage_Type in target.Weakness:
                print(((Current_Character.ATK*atk_mul*Move_to_Use.PWR)/(target.DEF*def_mul))*wkn_mul*1.5)
                damage_to_deal = round(((Current_Character.ATK*atk_mul*Move_to_Use.PWR)/(target.DEF*def_mul))*wkn_mul*1.5)
            else:
                print(((Current_Character.ATK*atk_mul*Move_to_Use.PWR)/(target.DEF*def_mul))*wkn_mul)
                damage_to_deal = round(((Current_Character.ATK*atk_mul*Move_to_Use.PWR)/(target.DEF*def_mul))*wkn_mul)
            print("damage to deal: "+str(damage_to_deal))
            if damage_to_deal < 0:
                damage_to_deal = 0
            print("damage to deal: "+str(damage_to_deal))
            hp_before_damage = target.Current_HP
            target.Current_HP -= damage_to_deal
            weakness_text = ""
            if Move_to_Use.Damage_Type in target.Weakness:
                weakness_text = "\nWEAKNESS HIT!\nDealt 1.5x damage!\nInflicted 1.3x Weakness (WKN) for 5 turns!"
                target.Effects.append(["WKN",1.3,5])
            if damage_to_deal > 0:
                write_text("Dealt "+str(damage_to_deal)+" damage to "+target.DisplayName+"!\n"+str(hp_before_damage)+" > "+str(target.Current_HP)+weakness_text)
            else:
                write_text(target.DisplayName+" took no damage!"+weakness_text)
            update_party_text()
            a_button.config(command=Check_If_Player_Dead)
            talk_button.config(command=Check_If_Player_Dead)
            q_command = "Check_If_Player_Dead()"
            space_command = "Check_If_Player_Dead()"
        elif Move_to_Use.Move_Type == "Magic":
            print("move is magic")
            res_mul = 1
            wkn_mul = 1
            if len(target.Effects) > 0:
                print("checking effects")
                for effect in target.Effects:
                    print(effect)
                    if effect[0] == "RES":
                        res_mul = res_mul*effect[1]
                    elif effect[0] == "WKN":
                        wkn_mul = wkn_mul*effect[1]
            mag_mul = 1
            if len(Current_Character.Effects) > 0:
                print("checking effects")
                for effect in Current_Character.Effects:
                    print(effect)
                    if effect[0] == "MAG":
                        mag_mul = mag_mul*effect[1]
            print("WKN MUL: "+str(wkn_mul))
            if Move_to_Use.Damage_Type in target.Weakness:
                print("(("+str(Current_Character.MAG)+"*"+str(Move_to_Use.PWR)+")/("+str(target.RES)+"*"+str(res_mul)+")*"+str(wkn_mul)+"*1.5")
                print(((Current_Character.MAG*mag_mul*Move_to_Use.PWR)/(target.RES*res_mul))*wkn_mul*1.5)
                damage_to_deal = round(((Current_Character.MAG*mag_mul*Move_to_Use.PWR)/(target.RES*res_mul))*wkn_mul*1.5)
            else:
                print("(("+str(Current_Character.MAG)+"*"+str(Move_to_Use.PWR)+")/("+str(target.RES)+"*"+str(res_mul)+")*"+str(wkn_mul))
                print(((Current_Character.MAG*mag_mul*Move_to_Use.PWR)/(target.RES*res_mul))*wkn_mul)
                damage_to_deal = round(((Current_Character.MAG*mag_mul*Move_to_Use.PWR)/(target.RES*res_mul))*wkn_mul)
            if damage_to_deal < 0:
                damage_to_deal = 0
            print("damage to deal: "+str(damage_to_deal))
            hp_before_damage = target.Current_HP
            weakness_text = ""
            target.Current_HP -= damage_to_deal
            if Move_to_Use.Damage_Type in target.Weakness:
                weakness_text = "\nWEAKNESS HIT!\nDealt 1.5x damage!\nInflicted 1.3x Weakness (WKN) for 5 turns!"
                target.Effects.append(["WKN",1.3,5])
            if damage_to_deal > 0:
                write_text("Dealt "+str(damage_to_deal)+" damage to "+target.DisplayName+"!\n"+str(hp_before_damage)+" > "+str(target.Current_HP)+weakness_text)
            else:
                write_text(target.DisplayName+" took no damage!"+weakness_text)
            update_party_text()
            a_button.config(command=Check_If_Player_Dead)
            talk_button.config(command=Check_If_Player_Dead)
            q_command = "Check_If_Player_Dead()"
            space_command = "Check_If_Player_Dead()"
        elif Move_to_Use.Move_Type == "Heal":
            print("move is healing")
            hlg_mul = 1
            if len(Current_Character.Effects) > 0:
                print("checking effects")
                for effect in target.Effects:
                    if effect[0] == "HLG":
                        hlg_mul = hlg_mul*effect[1]
            # amount_to_heal = round((Current_Character.HLG*hlg_mul*Move_to_Use.PWR)/(target.DEF*hlg_mul))
            amount_to_heal = round(Current_Character.HLG*hlg_mul*Move_to_Use.PWR)
            print("amount_to_heal before cut: "+str(amount_to_heal))
            # if amount_to_heal < 0:
            #     amount_to_heal = 0
            if target.Current_HP <= 0:
                write_text(target.DisplayName+" is defeated and can't be healed")
            elif Move_to_Use.Heal_Stat == "HP": 
                print("healing HP")
                hp_before_damage = target.Current_HP
                if amount_to_heal + target.Current_HP > target.Max_HP:
                    amount_to_heal = target.Max_HP - target.Current_HP
                target.Current_HP += amount_to_heal
                if amount_to_heal > 0:
                    write_text("Restored "+str(amount_to_heal)+"HP from "+target.DisplayName+"!\n"+str(hp_before_damage)+" > "+str(target.Current_HP))
                else:
                    write_text(target.DisplayName + " didn't restore HP!")
            elif Move_to_Use.Heal_Stat == "SP":
                print("healing SP")
                sp_before_heal = target.Current_SP
                if amount_to_heal + target.Current_SP > target.Max_SP:
                    amount_to_heal = target.Max_SP - target.Current_SP
                else:
                    write_text(target.DisplayName + " didn't restore SP!")
                target.Current_SP += amount_to_heal
                if amount_to_heal > 0 and Move_to_Use.PWR > 0:
                    write_text("Restored "+str(amount_to_heal)+" SP from "+target.DisplayName+"!\n"+str(sp_before_heal)+" > "+str(target.Current_SP))
                elif Move_to_Use.PWR < 0:
                    write_text("Drained "+str(amount_to_heal*-1)+" SP from "+target.DisplayName+"!\n"+str(sp_before_heal)+" > "+str(target.Current_SP))
                    if target.Current_SP < 0:
                        target.Current_SP = 0
                        print("set SP to 0, was below 0")
            else:
                print("error, no stat to heal")
            update_party_text()
            perform_move_index += 1
            if perform_move_index <= len(Move_Target)-1:
                a_button.config(command=Enemy_Perform_Move)
                talk_button.config(command=Enemy_Perform_Move)
                q_command = "Enemy_Perform_Move()"
                space_command = "Enemy_Perform_Move()"
            else:
                #write_text("But nothing happened!")
                Current_Character.Current_Action_Count += 1
                if Current_Character.Current_Action_Count >= Current_Character.Max_Action_Count:
                    character_to_action_index += 1
                    a_button.config(command=Enemy_Turn)
                    talk_button.config(command=Enemy_Turn)
                    q_command = "Enemy_Turn()"
                    space_command = "Enemy_Turn()"
                else:
                    a_button.config(command=Enemy_Perform_Again)
                    talk_button.config(command=Enemy_Perform_Again)
                    q_command = "Enemy_Perform_Again()"
                    space_command = "Enemy_Perform_Again()"
        elif Move_to_Use.Move_Type == "Boost":
            print(Move_Target)
            print(target)
            thing_to_append = []
            thing_to_append.append(Move_to_Use.Inflict[0])
            thing_to_append.append(float(str(Move_to_Use.Inflict[1])))
            thing_to_append.append(int(str(Move_to_Use.Inflict[2])))
            target.Effects.append(thing_to_append)
            for char in characters.Current_Party:
                print(char.Effects)
            write_text("Inflicted "+str(Move_to_Use.Inflict[1])+"x "+Move_to_Use.Inflict[0]+" on "+target.DisplayName+"\nfor "+str(Move_to_Use.Inflict[2])+" turns")
            update_party_text()
            perform_move_index += 1
            if perform_move_index <= len(Move_Target)-1:
                a_button.config(command=Enemy_Perform_Move)
                talk_button.config(command=Enemy_Perform_Move)
                q_command = "Enemy_Perform_Move()"
                space_command = "Enemy_Perform_Move()"
            else:
                Current_Character.Current_Action_Count += Move_to_Use.Action_Count
                if Current_Character.Current_Action_Count >= Current_Character.Max_Action_Count:
                    character_to_action_index += 1
                a_button.config(command=Enemy_Turn)
                talk_button.config(command=Enemy_Turn)
                q_command = "Enemy_Turn()"
                space_command = "Enemy_Turn()"
        elif Move_to_Use.Move_Type == "Multiboost":
            print(Move_Target)
            print(target)
            effects_print = "Targeted "+target.DisplayName+" and inflicted"
            effect_index = 0
            for effect in Move_to_Use.Inflict:
                print(effect)
                thing_to_append = []
                thing_to_append.append(effect[0])
                thing_to_append.append(float(str(effect[1])))
                thing_to_append.append(int(str(effect[2])))
                target.Effects.append(thing_to_append)
                effects_print = effects_print + "\n"+ str(effect[1])+"x "+effect[0]+" for "+str(effect[2])+" turns"
            # for char in characters.Current_Party:
            #     print(char.Effects)
            #write_text("Inflicted "+str(Move_to_Use.Inflict[1])+"x "+Move_to_Use.Inflict[0]+" on "+target.DisplayName+"\nfor "+str(Move_to_Use.Inflict[2])+" turns")
            write_text(effects_print)
            update_party_text()
            perform_move_index += 1
            if perform_move_index <= len(Move_Target)-1:
                a_button.config(command=Enemy_Perform_Move)
                talk_button.config(command=Enemy_Perform_Move)
                q_command = "Enemy_Perform_Move()"
                space_command = "Enemy_Perform_Move()"
            else:
                Current_Character.Current_Action_Count += Move_to_Use.Action_Count
                if Current_Character.Current_Action_Count >= Current_Character.Max_Action_Count:
                    character_to_action_index += 1
                a_button.config(command=Enemy_Turn)
                talk_button.config(command=Enemy_Turn)
                q_command = "Enemy_Turn()"
                space_command = "Enemy_Turn()"
    else:
        #write_text("But nothing happend!")
        character_to_action_index += Move_to_Use.Action_Count
        a_button.config(command=Enemy_Turn)
        talk_button.config(command=Enemy_Turn)
        q_command = "Enemy_Turn()"
        space_command = "Enemy_Turn()"



target = None

def Perform_Move():
    disable_inputs()
    global perform_move_index
    global Move_Target
    global Move_to_Use
    global Current_Character
    global space_command
    global q_command
    global target
    global character_to_action_index
    if perform_move_index <= len(Move_Target)-1:
        target = Move_Target[perform_move_index]
        if Move_to_Use.Move_Type == "Physical":
            print("move is physical")
            def_mul = 1
            wkn_mul = 1
            if len(target.Effects) > 0:
                print("checking effects")
                for effect in target.Effects:
                    print(effect)
                    if effect[0] == "DEF":
                        def_mul = def_mul*effect[1]
                    elif effect[0] == "WKN":
                        print("has wkn")
                        wkn_mul = wkn_mul*effect[1]
            atk_mul = 1
            if Move_to_Use.DisplayName == "Finale" and target.Weakness[0] == "Ultimate Weapon":
                atk_mul = 999999*3
            if len(Current_Character.Effects) > 0:
                print("checking effects")
                for effect in Current_Character.Effects:
                    print(effect)
                    if effect[0] == "ATK":
                        atk_mul = atk_mul*effect[1]
            print("WKN MUL: "+str(wkn_mul))
            if Move_to_Use.Damage_Type in target.Weakness:
                damage_to_deal = round(((Current_Character.ATK*atk_mul*Move_to_Use.PWR)/(target.DEF*def_mul))*wkn_mul*1.5)
            else:
                damage_to_deal = round(((Current_Character.ATK*atk_mul*Move_to_Use.PWR)/(target.DEF*def_mul))*wkn_mul)
            if damage_to_deal < 0:
                damage_to_deal = 0
            hp_before_damage = target.Current_HP
            target.Current_HP -= damage_to_deal
            weakness_text = ""
            if Move_to_Use.Damage_Type in target.Weakness:
                weakness_text = "\nWEAKNESS HIT!\nDealt 1.5x damage!\nInflicted 1.3x Weakness (WKN) for 5 turns!"
                target.Effects.append(["WKN",1.3,5])
            if damage_to_deal > 0:
                write_text("Dealt "+str(damage_to_deal)+" damage to "+target.DisplayName+"!\n"+str(hp_before_damage)+" > "+str(target.Current_HP)+weakness_text)
            else:
                write_text(target.DisplayName+" took no damage!"+weakness_text)
            a_button.config(command=Check_If_Enemy_Dead)
            talk_button.config(command=Check_If_Enemy_Dead)
            q_command = "Check_If_Enemy_Dead()"
            space_command = "Check_If_Enemy_Dead()"
        elif Move_to_Use.Move_Type == "Magic":
            print("move is magic")
            res_mul = 1
            wkn_mul = 1
            if len(target.Effects) > 0:
                print("checking effects")
                for effect in target.Effects:
                    print(effect)
                    if effect[0] == "RES":
                        res_mul = res_mul*effect[1]
                    elif effect[0] == "WKN":
                        print("has wkn")
                        wkn_mul = wkn_mul*effect[1]
            mag_mul = 1
            if len(Current_Character.Effects) > 0:
                print("checking effects")
                for effect in Current_Character.Effects:
                    print(effect)
                    if effect[0] == "MAG":
                        mag_mul = mag_mul*effect[1]
            print("WKN MUL: "+str(wkn_mul))
            if Move_to_Use.Damage_Type in target.Weakness:
                damage_to_deal = round(((Current_Character.MAG*mag_mul*Move_to_Use.PWR)/(target.RES*res_mul))*wkn_mul*1.5)
            else:
                damage_to_deal = round(((Current_Character.MAG*mag_mul*Move_to_Use.PWR)/(target.RES*res_mul))*wkn_mul)
            if damage_to_deal < 0:
                damage_to_deal = 0
            print("damage to deal: "+str(damage_to_deal))
            hp_before_damage = target.Current_HP
            target.Current_HP -= damage_to_deal
            weakness_text = ""
            if Move_to_Use.Damage_Type in target.Weakness:
                weakness_text = "\nWEAKNESS HIT!\nDealt 1.5x damage!\nInflicted 1.3x Weakness (WKN) for 3 turns!"
                target.Effects.append(["WKN",1.3,5])
            if damage_to_deal > 0:
                write_text("Dealt "+str(damage_to_deal)+" damage to "+target.DisplayName+"!\n"+str(hp_before_damage)+" > "+str(target.Current_HP)+weakness_text)
            else:
                write_text(target.DisplayName+" took no damage!"+weakness_text)
            a_button.config(command=Check_If_Enemy_Dead)
            talk_button.config(command=Check_If_Enemy_Dead)
            q_command = "Check_If_Enemy_Dead()"
            space_command = "Check_If_Enemy_Dead()"
        elif Move_to_Use.Move_Type == "Heal":
            print("move is healing")
            hlg_mul = 1
            if len(Current_Character.Effects) > 0:
                print("checking effects")
                for effect in target.Effects:
                    if effect[0] == "HLG":
                        hlg_mul = hlg_mul*effect[1]
            # amount_to_heal = round((Current_Character.HLG*hlg_mul*Move_to_Use.PWR)/(target.DEF*hlg_mul))
            amount_to_heal = round(Current_Character.HLG*hlg_mul*Move_to_Use.PWR)
            print("amount_to_heal before cut: "+str(amount_to_heal))
            # if amount_to_heal < 0:
            #     amount_to_heal = 0
            if target.Current_HP <= 0:
                write_text(target.DisplayName+" is defeated and can't be healed")
            elif Move_to_Use.Heal_Stat == "HP":
                print("healing HP")
                hp_before_damage = target.Current_HP
                if amount_to_heal + target.Current_HP > target.Max_HP:
                    amount_to_heal = target.Max_HP - target.Current_HP
                target.Current_HP += amount_to_heal
                if amount_to_heal > 0:
                    write_text("Restored "+str(amount_to_heal)+"HP from "+target.DisplayName+"!\n"+str(hp_before_damage)+" > "+str(target.Current_HP))
                else:
                    write_text(target.DisplayName + " didn't restore HP!")
            elif Move_to_Use.Heal_Stat == "SP":
                print("healing SP")
                sp_before_heal = target.Current_SP
                if amount_to_heal + target.Current_SP > target.Max_SP:
                    amount_to_heal = target.Max_SP - target.Current_SP
                else:
                    write_text(target.DisplayName + " didn't restore SP!")
                target.Current_SP += amount_to_heal
                if amount_to_heal > 0 and Move_to_Use.PWR > 0:
                    write_text("Restored "+str(amount_to_heal)+" SP from "+target.DisplayName+"!\n"+str(sp_before_heal)+" > "+str(target.Current_SP))
                elif Move_to_Use.PWR < 0:
                    write_text("Drained "+str(amount_to_heal*-1)+" SP from "+target.DisplayName+"!\n"+str(sp_before_heal)+" > "+str(target.Current_SP))
                    if target.Current_SP < 0:
                        target.Current_SP = 0
                        print("set SP to 0, was below 0")
            else:
                print("error, no stat to heal")
            update_party_text()
            perform_move_index += 1
            if perform_move_index <= len(Move_Target)-1:
                a_button.config(command=Perform_Move)
                talk_button.config(command=Perform_Move)
                q_command = "Perform_Move()"
                space_command = "Perform_Move()"
            else:
                character_to_action_index += 1
                a_button.config(command=Character_Turn)
                talk_button.config(command=Character_Turn)
                q_command = "Character_Turn()"
                space_command = "Character_Turn()"
        elif Move_to_Use.Move_Type == "Boost":
            print(Move_Target)
            print(target)
            thing_to_append = []
            thing_to_append.append(Move_to_Use.Inflict[0])
            thing_to_append.append(float(str(Move_to_Use.Inflict[1])))
            thing_to_append.append(int(str(Move_to_Use.Inflict[2])))
            target.Effects.append(thing_to_append)
            for char in characters.Current_Party:
                print(char.Effects)
            write_text("Inflicted "+str(Move_to_Use.Inflict[1])+"x "+Move_to_Use.Inflict[0]+" on "+target.DisplayName+"\nfor "+str(Move_to_Use.Inflict[2])+" turns")
            update_party_text()
            perform_move_index += 1
            if perform_move_index <= len(Move_Target)-1:
                a_button.config(command=Perform_Move)
                talk_button.config(command=Perform_Move)
                q_command = "Perform_Move()"
                space_command = "Perform_Move()"
            else:
                character_to_action_index += 1
                a_button.config(command=Character_Turn)
                talk_button.config(command=Character_Turn)
                q_command = "Character_Turn()"
                space_command = "Character_Turn()"
        elif Move_to_Use.Move_Type == "Multiboost":
            print(Move_Target)
            print(target)
            effects_print = "Targeted "+target.DisplayName+" and inflicted"
            effect_index = 0
            for effect in Move_to_Use.Inflict:
                print(effect)
                thing_to_append = []
                thing_to_append.append(effect[0])
                thing_to_append.append(float(str(effect[1])))
                thing_to_append.append(int(str(effect[2])))
                target.Effects.append(thing_to_append)
                effects_print = effects_print + "\n"+ str(effect[1])+"x "+effect[0]+" for "+str(effect[2])+" turns"
            # for char in characters.Current_Party:
            #     print(char.Effects)
            #write_text("Inflicted "+str(Move_to_Use.Inflict[1])+"x "+Move_to_Use.Inflict[0]+" on "+target.DisplayName+"\nfor "+str(Move_to_Use.Inflict[2])+" turns")
            write_text(effects_print)
            update_party_text()
            perform_move_index += 1
            if perform_move_index <= len(Move_Target)-1:
                a_button.config(command=Perform_Move)
                talk_button.config(command=Perform_Move)
                q_command = "Perform_Move()"
                space_command = "Perform_Move()"
            else:
                character_to_action_index += 1
                a_button.config(command=Character_Turn)
                talk_button.config(command=Character_Turn)
                q_command = "Character_Turn()"
                space_command = "Character_Turn()"
    else:
        #write_text("But nothing happend!")
        character_to_action_index += 1
        a_button.config(command=Character_Turn)
        talk_button.config(command=Character_Turn)
        q_command = "Character_Turn()"
        space_command = "Character_Turn()"

def Check_If_Player_Dead():
    disable_inputs()
    global target
    global current_encounter
    global current_encounter_all
    global q_command
    global space_command
    global character_to_action_index
    global perform_move_index
    global Move_Target
    global Current_Character
    global Move_to_Use
    print("check if player dead")
    if target.Current_HP <= 0:
        target.Current_HP = 0
        print("player is dead")
        write_text(target.DisplayName + " has been defeated!")
        print(current_encounter_all)
        print(current_encounter)
        a_button.config(command=Check_If_Party_Dead)
        talk_button.config(command=Check_If_Party_Dead)
        q_command = "Check_If_Party_Dead()"
        space_command = "Check_If_Party_Dead()"
    else:
        perform_move_index += 1
        if perform_move_index <= len(Move_Target)-1:
            Enemy_Perform_Move()
        else:
            Current_Character.Current_Action_Count += Move_to_Use.Action_Count
            if Current_Character.Current_Action_Count >= Current_Character.Max_Action_Count:
                character_to_action_index += 1
                Enemy_Turn()
            else:
                Enemy_Perform_Again()

def Check_If_Party_Dead():
    global character_to_action_index
    global Current_Character
    global Move_to_Use
    print('check if party dead')
    number_dead = 0
    for char in characters.Current_Party:
        if char.Current_HP <= 0:
            number_dead += 1
    print("party size: "+str(len(characters.Current_Party)))
    print("number dead: "+str(number_dead))
    if number_dead >= len(characters.Current_Party):
        write_text(
        "===================\n"+
        "==== GAME OVER ====\n"+
        "===================\n"+
        "\n"+
        "[EQUIP] Load Save\n"
        "[PARTY] Auto-Save*\n"
        "[SAVE] Close Game\n\n"
        "*Only use Auto-Save if you are softlocked,\nmake sure to save manually after loading\nan Auto-Save as Auto-Saves are temporary\nand cannot be accessed from the start menu."
        )
        global r_command
        global t_command
        global one_command
        equip_button.config(command=load_save)
        stat_button.config(command=load_autosave)
        save_button.config(command=sys.exit)
        r_command = "load_save()"
        t_command = "load_autosave()"
        one_command = "sys.exit()"
    else:
        Current_Character.Current_Action_Count += Move_to_Use.Action_Count
        if Current_Character.Current_Action_Count >= Current_Character.Max_Action_Count:
            character_to_action_index += 1
            Enemy_Turn()
        else:
            Enemy_Perform_Again()


def Check_If_Enemy_Dead():
    disable_inputs()
    global target
    global current_encounter
    global current_encounter_all
    global q_command
    global space_command
    global character_to_action_index
    global perform_move_index
    global Move_Target
    print("check if enemy dead")
    if target.Current_HP <= 0:
        print("enemy is dead")
        write_text(target.DisplayName + " has been defeated!")
        current_encounter.remove(target)
        print(current_encounter_all)
        print(current_encounter)
        if current_encounter_all.index(target) == 0:
            print("enemy at target_location 0")
            clear_sprite(2)
        elif current_encounter_all.index(target) == 1:
            print("enemy at target_location 1")
            clear_sprite(1)
        elif current_encounter_all.index(target) == 2:
            print("enemy at target_location 2")
            clear_sprite(3)
        a_button.config(command=Get_EXP_From_Enemy)
        talk_button.config(command=Get_EXP_From_Enemy)
        q_command = "Get_EXP_From_Enemy()"
        space_command = "Get_EXP_From_Enemy()"
    else:
        perform_move_index += 1
        if perform_move_index <= len(Move_Target)-1:
            Perform_Move()
        else:
            character_to_action_index += 1
            Character_Turn()

    
def Get_EXP_From_Enemy():
    global target
    global q_command
    global space_command
    global character_to_action_index
    global perform_move_index
    thing_to_print = ""
    for char in characters.Current_Party:
        if char.Current_HP > 0:
            exp_mul = 1
            if char.Level > target.Level:
                exp_mul = ((char.Level - target.Level)*1.75) + 1
            exp_to_gain = round(target.EXP/exp_mul)
            char.EXP += exp_to_gain
            if char.EXP >= 1000:
                char.EXP -= 1000
                char.Level += 1
                print(char.DisplayName)
                atk_before = char.ATK
                char.ATK = round(char.ATK*((char.ATK_Growth+100)/100))
                print("ATK "+str(atk_before)+" > "+str(char.ATK))
                hp_before = char.Max_HP
                char.Max_HP = round(char.Max_HP*((char.HP_Growth+100)/100))
                print("HP "+str(hp_before)+" > "+str(char.Max_HP))
                mag_before = char.MAG
                char.MAG = round(char.MAG*((char.MAG_Growth+100)/100))
                print("MAG "+str(mag_before)+" > "+str(char.MAG))
                hlg_before = char.HLG
                char.HLG = round(char.HLG*((char.HLG_Growth+100)/100))
                print("HLG "+str(hlg_before)+" > "+str(char.HLG))
                sp_before = char.Max_SP
                char.Max_SP = round(char.Max_SP*((char.SP_Growth+100)/100))
                print("SP "+str(sp_before)+" > "+str(char.Max_SP))
                def_before = char.DEF
                char.DEF = round(char.DEF*((char.DEF_Growth+100)/100))
                print("DEF "+str(def_before)+" > "+str(char.DEF))
                res_before = char.RES
                char.RES = round(char.RES*((char.RES_Growth+100)/100))
                print("RES "+str(res_before)+" > "+str(char.RES))
                print("")
                thing_to_print = thing_to_print + char.DisplayName + " leveled up!\n"
            else:
                thing_to_print = thing_to_print + char.DisplayName + " gained " + str(exp_to_gain) + " EXP!\n"
        else:
            thing_to_print = thing_to_print + char.DisplayName + " is defeated...\n"
    global Gold
    Gold += target.Gold
    thing_to_print = thing_to_print+"+"+str(target.Gold)+" Gold"
    filedisplay.config(text="Location: "+maps.current_location[0]+"\nGold: "+str(Gold))
    write_text(thing_to_print)
    global current_encounter
    if len(current_encounter) == 0:
        a_button.config(command=Win_Battle)
        talk_button.config(command=Win_Battle)
        q_command = "Win_Battle()"
        space_command = "Win_Battle()"
    else:
        perform_move_index += 1
        if perform_move_index <= len(Move_Target)-1:
            a_button.config(command=Perform_Move)
            talk_button.config(command=Perform_Move)
            q_command = "Perform_Move()"
            space_command = "Perform_Move()"
        else:
            character_to_action_index += 1
            a_button.config(command=Character_Turn)
            talk_button.config(command=Character_Turn)
            q_command = "Character_Turn()"
            space_command = "Character_Turn()"

battle_during_cutscene = False

def Win_Battle():
    global battle_during_cutscene
    global q_command
    global space_command
    if characters.Protipole.Current_HP < 1:
        characters.Protipole.Current_HP = 1
    write_text("=== Battle Complete ===")
    progress_economy()
    if battle_during_cutscene == True:
        #a_button.config(command=advance_text)
        talk_button.config(command=advance_text)
        #q_command = "advance_text()"
        space_command = "advance_text()"
    else:
        #a_button.config(command=refresh)
        talk_button.config(command=refresh)
        #q_command = "refresh()"
        space_command = "refresh()"


def Instant_Level_Up(char,times):
    for x in range(times):
        print("\n")
        char.Level += 1
        print(char.DisplayName + " Level: "+ str(char.Level))
        atk_before = char.ATK
        char.ATK = round(char.ATK*((char.ATK_Growth+100)/100))
        print("ATK "+str(atk_before)+" > "+str(char.ATK))
        hp_before = char.Max_HP
        char.Max_HP = round(char.Max_HP*((char.HP_Growth+100)/100))
        print("HP "+str(hp_before)+" > "+str(char.Max_HP))
        mag_before = char.MAG
        char.MAG = round(char.MAG*((char.MAG_Growth+100)/100))
        print("MAG "+str(mag_before)+" > "+str(char.MAG))
        hlg_before = char.HLG
        char.HLG = round(char.HLG*((char.HLG_Growth+100)/100))
        print("HLG "+str(hlg_before)+" > "+str(char.HLG))
        sp_before = char.Max_SP
        char.Max_SP = round(char.Max_SP*((char.SP_Growth+100)/100))
        print("SP "+str(sp_before)+" > "+str(char.Max_SP))
        def_before = char.DEF
        char.DEF = round(char.DEF*((char.DEF_Growth+100)/100))
        print("DEF "+str(def_before)+" > "+str(char.DEF))
        res_before = char.RES
        char.RES = round(char.RES*((char.RES_Growth+100)/100))
        print("RES "+str(res_before)+" > "+str(char.RES))
        print("\n")

Instant_Level_Up(characters.Bithecary,4)
Instant_Level_Up(characters.Archle,4)
Instant_Level_Up(characters.Bipouge,7)
Instant_Level_Up(characters.Alls_Ros,8)
    
     

enemy_attack_index = 0

def Select_Enemy_to_Check_Stats():
    disable_inputs()
    global enemy_attack_index
    enemy_attack_index = 0
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global check_enemy_stat_return_to
    check_enemy_stat_return_to = "Select_Enemy_to_Check_Stats"
    multiselect_index = 0
    text_to_use_in_multi = "Check Enemy Stats\n-----\n[Left] Select enemy\n[Right] Return to combat actions\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = current_encounter
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global left_command
    global a_command
    left_button.config(command=print_enemy_stats)
    left_command = "print_enemy_stats()"
    a_command = "print_enemy_stats()"
    global right_command
    global d_command
    right_button.config(command=Character_Turn)
    right_command = 'Character_Turn()'
    d_command = 'Character_Turn()'

def print_enemy_stats():
    print("enemy stats")
    disable_inputs()
    global check_enemy_stat_return_to
    global multiselect_index
    global list_to_use_in_multi
    char = list_to_use_in_multi[multiselect_index]
    currently_equipped_names = ""
    tempindex = 0
    global enemy_attack_index
    for thing in char.Moves:
        if tempindex != 0:
            currently_equipped_names = currently_equipped_names + ","
        if tempindex%3 == 0 and tempindex != 0:
            currently_equipped_names = currently_equipped_names + "\n"
        else:
            currently_equipped_names = currently_equipped_names + " "
        if tempindex == enemy_attack_index:
            currently_equipped_names = currently_equipped_names + ">" + thing[0].DisplayName
        else:
            currently_equipped_names = currently_equipped_names + thing[0].DisplayName
        tempindex += 1
    effects = "Active Effects:\n"
    if len(char.Effects) > 0:
        print(char.DisplayName+" has active effects")
        effect_index = 0
        for effect in char.Effects:
            if effect_index == 3:
                effects = effects+str(effect[1])+"x"+effect[0]+"("+str(effect[2])+"T)\n"
                effect_index = 0
            else:
                effects = effects+str(effect[1])+"x"+effect[0]+"("+str(effect[2])+"T) "
                effect_index += 1
    else:
        print("no active effects on "+char.DisplayName)
        effects = effects + "N/A"
    write_text(char.DisplayName+"\nEXP Level Determinant: "+str(char.Level)+"\nHP: "+str(char.Current_HP)+"/"+str(char.Max_HP)+"\nSP: "+str(char.Current_SP)+"/"+str(char.Max_SP)+"\n ATK: "+str(char.ATK)+"\n MAG: "+str(char.MAG)+"\n HLG: "+str(char.HLG)+"\n DEF: "+str(char.DEF)+"\n RES: "+str(char.RES)+"\n\nWeak to:\n"+str(char.Weakness).replace("[","").replace("]","").replace("'","")+"\n\n"+effects+"\n\nMoves:\n"+str(currently_equipped_names)+"\n\n"+char.Bio+"\n\n[A]/[B] Select Move\n[Right] Check Move\n[Left] Return")
    global right_command
    global d_command
    right_button.config(command=eval(check_enemy_stat_return_to))
    right_command = check_enemy_stat_return_to + "()"
    d_command = check_enemy_stat_return_to + "()"
    global q_command
    a_button.config(command=enemy_attack_index_increase)
    q_command = "enemy_attack_index_increase()"
    global e_command
    b_button.config(command=enemy_attack_index_decrease)
    e_command = "enemy_attack_index_decrease()"
    global left_command
    global a_command
    left_button.config(command=print_enemy_equip)
    left_command = "print_enemy_equip()"
    a_command = "print_enemy_equip()"

def enemy_attack_index_increase():
    disable_inputs()
    print("enemy_attack_index_increase")
    global enemy_attack_index
    global list_to_use_in_multi
    if enemy_attack_index+1 >= len(list_to_use_in_multi[multiselect_index].Moves):
        enemy_attack_index = 0
    else:
        enemy_attack_index += 1
    print_enemy_stats()

def enemy_attack_index_decrease():
    disable_inputs()
    print("enemy_attack_index_decrease")
    global enemy_attack_index
    global list_to_use_in_multi
    if enemy_attack_index-1 <= -1:
        enemy_attack_index = len(list_to_use_in_multi[multiselect_index].Moves)-1
    else:
        enemy_attack_index -= 1
    print_enemy_stats()

def print_enemy_equip():
    disable_inputs()
    global list_to_use_in_multi
    global enemy_attack_index
    global multiselect_index
    chosen_equip = list_to_use_in_multi[multiselect_index].Moves[enemy_attack_index][0]
    hp_min = str(list_to_use_in_multi[multiselect_index].Moves[enemy_attack_index][1])
    hp_max = str(list_to_use_in_multi[multiselect_index].Moves[enemy_attack_index][2])
    write_text(chosen_equip.DisplayName + "\n\nDamage Type: " + chosen_equip.Damage_Type + "\nMove Type: " + chosen_equip.Move_Type + "\nTarget: " + chosen_equip.Target + "\nSP Cost: " + str(chosen_equip.SP_Cost) + "\nPWR: " + str(chosen_equip.PWR) + "\nHeal Stat: " + ("N/A" if chosen_equip.Heal_Stat == None else chosen_equip.Heal_Stat) + "\n\nHP Minimum: " + hp_min + "\nHP Maximum: " + hp_max + "\n\n" + chosen_equip.Description + "\n\n [Right] Return")
    global right_command
    global d_command
    right_button.config(command=print_enemy_stats)
    right_command = "print_enemy_stats()"
    d_command = "print_enemy_stats()"


def Select_Party_Member_to_Check_Stats():
    disable_inputs()
    global multi_char_stat_to_show
    multi_char_stat_to_show = None
    global text_to_use_in_multi
    global temporary_text_to_use_in_multi
    global multiselect_index
    global list_to_use_in_multi
    global multi_use_displayname
    global char_stat_return_to
    char_stat_return_to = "Select_Party_Member_to_Check_Stats"
    multiselect_index = 0
    text_to_use_in_multi = "Check Party Stats\n-----\n[Right] Select ally\n[Left] Return to combat actions\n"
    temporary_text_to_use_in_multi = text_to_use_in_multi
    list_to_use_in_multi = characters.Current_Party
    multi_use_displayname = True
    write_text(write_multiselect())
    global up_command
    global w_command
    up_button.config(command=multiselect_move_up)
    up_command = 'multiselect_move_up()'
    w_command = 'multiselect_move_up()'
    global down_command
    global s_command
    down_button.config(command=multiselect_move_down)
    down_command = 'multiselect_move_down()'
    s_command = 'multiselect_move_down()'
    global right_command
    global d_command
    right_button.config(command=print_char_stats_battle)
    right_command = "print_char_stats_battle()"
    d_command = "print_char_stats_battle()"
    global left_command
    global a_command
    left_button.config(command=Character_Turn)
    left_command = 'Character_Turn()'
    a_command = 'Character_Turn()'
























def Manual_Add_Char(char,lv):
    characters.Unequipped_Characters.append(char)
    characters.All_Recruited_Characters.append(char)
    Instant_Level_Up(char,lv)



screen.bind("<KeyPress>",key_input)
toggle_sidestep_button(True)
start_menu_control_set()


Instant_Level_Up(characters.Protipole,20)#8+3-1+100)
Manual_Add_Char(characters.Startole,12)
Manual_Add_Char(characters.Bipoanderer,20)
Manual_Add_Char(characters.Wicole,20)
Manual_Add_Char(characters.Bithecary,4+3)
Manual_Add_Char(characters.Archle,12+3)
Manual_Add_Char(characters.Alls_Ros,8+3+1)
Manual_Add_Char(characters.Birowth,19)
# Manual_Add_Char(characters.Birowth,13)
Gold += 100000
# maps.player_cords = [9,18]
# maps.current_location = maps.Passway_Village
# maps.current_location = maps.Bandit_Road
maps.current_location = maps.Guardian_Village
maps.player_cords = [4,17]
equipment.equipment_inventory.append(equipment.CigaretteLighter)
characters.Protipole.Equipped = [equipment.Finale,equipment.Disarm,equipment.Healing_Aura] #
characters.Startole.Equipped = [equipment.Spear_of_Staves,equipment.Pierce,equipment.Guard]
characters.Bipoanderer.Equipped = [equipment.Snipe,equipment.Drown]
characters.Archle.Equipped = [equipment.Snipe, equipment.Knife_Rain, equipment.Inferno]
characters.Wicole.Equipped = [equipment.Cryoablate,equipment.Holy_Light,equipment.Drown] #
characters.Bithecary.Equipped = [equipment.Recover,equipment.Rime_Potion,equipment.Healing_Aura]
characters.Bipouge.Equipped = [equipment.Spear_of_Staves,equipment.Holy_Light,equipment.Flood]
characters.Alls_Ros.Equipped = [equipment.Cryoablate,equipment.Drown,equipment.Holy_Light] #
characters.Birowth.Equipped = [equipment.Assault_Rifle,equipment.Pierce,equipment.Shatter]
#LEVEL 17 AT END OF THE LABYRINTH

equipment.key_item_inventory.append(equipment.mysterious_crystals)
equipment.key_item_inventory.append(equipment.humphrey_lore_read)
equipment.key_item_inventory.append(equipment.ecochecker)
equipment.key_item_inventory.append(equipment.bonus_shop_pass_ii)
equipment.key_item_inventory.append(equipment.ultimate_energy_prism)
equipment.key_item_inventory.append(equipment.super_pure_diamond)


equipment.key_item_inventory.append(equipment.virginity_hat)
equipment.key_item_inventory.append(equipment.neville_coin)
equipment.key_item_inventory.append(equipment.virginity_propaganda_signed)



for char in characters.All_Recruited_Characters:
    char.Current_HP = char.Max_HP
    char.Current_SP = char.Max_SP


screen.mainloop()