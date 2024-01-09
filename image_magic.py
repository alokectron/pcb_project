#image_magic.py

#class Image_Magic:
img_test_count = 0
def init_image_magic(config):
    print("Initing Image Magic ...")
    
def is_pcb(img):
    global img_test_count
    if(img_test_count==10):
        img_test_count=1
    else:
        img_test_count=img_test_count+1
    if(img_test_count ==1):        
        return True
    else:
        return False;

def extract_pcb_img(img):
    return img

def is_good_pcb(img, station_index):
    if(img_test_count%4 == 3):
        return False
    else:
        return True;
