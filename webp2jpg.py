from PIL import Image
import os 
g = os.walk(r"./")  

for path,dir_list,file_list in g:  
    for file_name in file_list: 
        if os.path.splitext(file_name)[1]=='.webp':
            filename = path+'/'+file_name
            im = Image.open(filename)
            if im.mode == "RGBA":
                im.load()  # required for png.split()
                background = Image.new("RGB", im.size, (255, 255, 255))
                background.paste(im, mask=im.split()[3]) 
            save_name = filename.replace('webp', 'jpg')
            im.save('{}'.format(save_name), 'JPEG')
