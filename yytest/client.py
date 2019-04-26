#coding=utf-8
import Tkinter as tk
import ttk
from PIL import Image,ImageTk
import io
from urllib2 import urlopen
# var=tk.IntVar
# win=tk.Tk()
# win.title("TV Check the picture")
# ttk.Label(win,text='First').grid(row=0,sticky=tk.E) #First靠右
# ttk.Label(win,text='Second').grid(row=1)
# ttk.Entry(win).grid(row=0,column=1)
# ttk.Entry(win).grid(row=1,column=1)
# button=ttk.Checkbutton(win,text='accept yolu').grid()
#
# #插入图片
# fn=r'D:\pythonscrip\python2\1.gif'
# #photo=tk.PhotoImage(file=filename)
# filename=Image.open(fn)
# photo=ImageTk.PhotoImage(filename)
# label=tk.Label(win,image=photo)
# label.pack()     # 显示
# #label.forget() # 隐藏
# win.mainloop()
root = tk.Tk()
url = "http://i50.tinypic.com/34g8vo5.jpg"
image_bytes = urlopen(url).read()
# internal data file
data_stream = io.BytesIO(image_bytes)
# open as a PIL image object
pil_image = Image.open(data_stream)
# optionally show image info
# get the size of the image
w, h = pil_image.size
# split off image file name
fname = url.split('/')[-1]
sf = "{} ({}x{})".format(fname, w, h)
root.title(sf)
# convert PIL image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(pil_image)
# put the image on a typical widget
label = tk.Label(root, image=tk_image, bg='brown')
label.pack(padx=5, pady=5)
root.mainloop()