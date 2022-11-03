import win32gui

def winEnumHandler(hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        #checks for all open windows, producing the name of the window + the hwnd
        print (win32gui.GetWindowText( hwnd ))

        if win32gui.GetWindowText( hwnd ) == 'VALORANT  ':
            #need to find a way to automatically transfer this value to hwnd_input in app.py
            val_hwnd = hex( hwnd )

win32gui.EnumWindows( winEnumHandler, None )