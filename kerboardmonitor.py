'''
    monitoring keyboard save as 
        "(key name):|:(timepresstillrelease)"
    as list in file,which u can specified
    and u can choose what module u will use with
        keyboard(default) or pynput
        to use keyboard : keyboard(path)
        to use pynput   : pynput(path)
'''
import time
class mainstring():
    def __init__(self, filename):
        self.infile = open(filename,'a',buffering=1)
        self.keypress=dict()
        self.lastpress=dict()
    def addstring(self,strin):self.infile.write(strin)
    def on_press(self,key,now=None):
        if not now:now=time.time()
        if key not in self.keypress or now-self.lastpress[key]>1:self.keypress[key]=now
        self.lastpress[key]=now
    def on_release(self,key,now=None):
        if not now:now=time.time()
        if key in self.keypress and now-self.lastpress[key]<1:self.addstring(key+':|:'+str(round(now-self.keypress.pop(key),6))+'\n')
def savepathtodesktop():
    import os
    return os.path.join('C:/Users',os.getlogin(),'Desktop/keyboardmonitoringlog.txt')
def keyboard(filename):
    import keyboard
    import threading
    ms=mainstring(filename)
    keyboard.hook(lambda event:ms.on_press(event.name,event.time) if event.event_type[0]=='d' else ms.on_release(event.name,event.time))
    L = threading.enumerate()
    L.remove(threading.main_thread()) 
    for t in L:t.join()
def pynput(filename):
    from pynput import keyboard
    ms=mainstring()
    with keyboard.Listener(on_press=ms.on_press,on_release=ms.on_release)as listener:listener.join()
if __name__=="__main__":keyboard(savepathtodesktop())



