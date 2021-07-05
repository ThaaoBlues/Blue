from pywinauto import Desktop , application
import webbrowser

webbrowser.open_new("http://www.google.com")



app = application.Application()


def find_window(name):
    for w in Desktop(backend="uia").windows(visible_only=False):
        if name in w.window_text():
            app.connect(title_re = w.window_text())
            app_dialog = app.top_window()
            app_dialog.restore().set_focus()

find_window("Marmiton")