import win32file
from win32con import FILE_NOTIFY_CHANGE_FILE_NAME, WAIT_OBJECT_0
import win32event
from os import listdir

path = r"C:\Users\Horim\Desktop\checkadd" #r"C:\Users\Horim\Desktop\tempInternetFiles\Temporary Internet Files" #r"C:\Users\Horim\AppData\Local\Microsoft\Windows\Temporary Internet Files"

handle=win32file.FindFirstChangeNotification(path, False, FILE_NOTIFY_CHANGE_FILE_NAME)
old_files= listdir(path)

while True:
    next_handle= win32file.FindNextChangeNotification(handle)

    result = win32event.WaitForSingleObject(handle, -1)
    print hex(result)
    # print WAIT_OBJECT_0
    if result==WAIT_OBJECT_0:
        new_files= listdir(path)
        added=[f for f in new_files if f not in old_files]
        print "added: {0}".format(added)
        old_files = new_files

        #win32file.FindNextChangeNotification(handle)

win32file.FindCloseChangeNotification(handle)
