import win32file
from win32con import FILE_NOTIFY_CHANGE_FILE_NAME, WAIT_OBJECT_0
import win32event
from os import listdir, path

folder_path = r"C:\Users\Horim\Desktop\tempInternetFiles\Temporary Internet Files" #r"C:\Users\Horim\AppData\Local\Microsoft\Windows\Temporary Internet Files"

handle=win32file.FindFirstChangeNotification(folder_path, True, FILE_NOTIFY_CHANGE_FILE_NAME)
old_files= listdir(folder_path)
image_extensions=[".png", ".jpg", ".gif", 'bmp']

# while True:
#     result = win32event.WaitForSingleObject(handle, -1)
#     added = []
#     # print WAIT_OBJECT_0
#     if result==WAIT_OBJECT_0:
#         new_files= listdir(folder_path)
#         for f in new_files:
#             file_name, file_extension = path.splitext(f)
#             if file_extension in image_extensions:
#                 added.append(f)
#         print "added: {0}".format(added)
#         old_files = new_files
#
#         win32file.FindNextChangeNotification(handle)
#
# win32file.FindCloseChangeNotification(handle)

print (path.splitext(listdir(folder_path)[1]))
