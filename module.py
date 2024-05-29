import win32clipboard

def copy_to_clipboard(string):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(string)
    win32clipboard.CloseClipboard()

def copy_from_clipboard():
    win32clipboard.OpenClipboard()
    return win32clipboard.GetClipboardData()
