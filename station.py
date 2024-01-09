import cv2 as cv
import capture
import time
import image_magic

class Station:
    keep_running = 1
    myconfig = None
    serial_num = 0
    station_index=0

    def init_station(self, config):
        print("Initing station")
        capture.init_cam()
    
    def start_running(self ):        
        self.keep_running = 1
    
    def get_pcb_serial_num(self):
        self.serial_num = self.serial_num+1
        return self.serial_num


    def get_picture(self):
        c = capture.capture() 
        if(c is None):
            print("Error: Could not capture image from camera")
            return None
        else:
            return c;
        
            
    def write_files(self, img, pcb_img, pcb_num):
        print("writing image files to the directory")
        cv.imwrite(f"c{self.station_index}.jpg", img)
        print("writing json to the directory")
        
            
    def do_work(self):
        print("Get Pic")
        img = self.get_picture()
        time.sleep(1)
        print("Check if we have PCB?")
        pcb_img = None
        pcb_num=-1
        if(image_magic.is_pcb(img)):
            print("It is a PCB")
            pcb_img = image_magic.extract_pcb_img(img)
            if(pcb_img is not None):
                print("If we have a PCB, check if it is good or bad") 
                pcb_num = self.get_pcb_serial_num()
                tval = image_magic.is_good_pcb(pcb_img, self.station_index)
                if(tval):
                    print(f"PCB #{pcb_num} is a good PCB")
                else:
                    print(f"PCB #{pcb_num} is a bad PCB")
                print("sending update to db")
                    
        else:
            print("It is not a PCB")
            pcb_img = None
        
        time.sleep(1)

        self.write_files(img, pcb_img, pcb_num)
        
    def shut_down(self):
        print("Shutting down station #1...")
        exit(0)
        
    def main_loop(self):

        while(1):
            if(self.keep_running ==1):
                self.do_work()
                time.sleep(1)
            else:
                time.sleep(1)
                if(self.keep_running== -1):
                    shut_down()

def test():
    stn = Station()
    stn.init_station(None)
    stn.main_loop()
    

if __name__ == '__main__':
    test()        