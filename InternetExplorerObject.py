import win32com.client
from shutil import copyfile

internetObj=win32com.client.Dispatch("InternetExplorer.Application")

internetObj.Navigate("https://www.google.co.il/search?q=aaa&safe=strict&rls=ig&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQ3OHr9IPgAhVdRBUIHcEWCtAQ_AUIDigB&biw=837&bih=514")