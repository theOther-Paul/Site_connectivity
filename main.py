import asyncio
import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo, showerror, showwarning
import web_check
import tkcap
import time
from tkinter import Menu


# global variable


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.style = ttk.Style(self)

    def change_theme(self, theme):
        self.get_screenshot(self.master)
        self.style.theme_use(theme)
        showinfo(title="Theme changed", message=f"Currently using {theme} theme")
        self.get_screenshot(self.master)

    @staticmethod
    def get_screenshot(master):
        cap = tkcap.CAP(master)
        cap.capture(f'ui_testing/shot {time.time()}.bmp')


def check(url):
    if asyncio.run(web_check.site_is_online(url)) is True:
        showinfo(title="Site online", message=f"{url} is online. If your browser doesn't display the page, please check the browser configuration.")
    else:
        showerror(title="Site offline", message=f"{url} appears to be offline. Please try again later.")


def error_message(url):
    if web_check.check_site_address(url) is None:
        showwarning(title="Insufficient parameters", message=f"To test a connection with a site, you must provide a URL. {url} is not a valid url.")
    if web_check.check_site_address(url):
        check(url)
    else:
        if web_check.check_site(url) is False:
            showerror(title="Site nonexistent", message=f"Unfortunately, the {url} entered is not a valid website. Please try again.")
        else:
            check(url)


def enable_partial_url(choice, url, mute=True):
    if mute is True:
        # web_check.fill_address_elements(url)
        pass
    else:
        if choice is True:
            check(web_check.fill_address_elements(url))
        else:
            error_message(url)


def get_help():
    import webbrowser
    webbrowser.open("feature/get_help.html")


def main():
    root: ThemedTk = ThemedTk()
    app = Window(root)
    # Window general settings
    root.wm_title("Site connectivity checker")
    # root.geometry("650x200+20+25")
    # root.resizable(False, False)
    root.iconbitmap('./assets/nm_no_connection.ico')
    """
    bg image src
    bg = ImageTk.PhotoImage(Image.open('assets/main_bg.jpg'))

    bg image display
    label_bg = ttk.Label(image=bg)
    label_bg.image = bg
    label_bg.place(x=0, y=0)
    """

    # window elements

    # menu
    main_menu = Menu(root)
    root.config(menu=main_menu)
    theme_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Themes", menu=theme_menu)
    extra_themes = root.get_themes()

    # new menu option
    main_menu.add_command(label='Help', command=lambda: get_help())

    for t in extra_themes:
        theme_menu.add_command(label=t, command=lambda t=t: app.change_theme(t))

    # app banner
    ttk.Label(text="Check Any URL Connection", anchor='n', justify=CENTER, font=("Helvetica", 20, "bold")).grid(row=1, rowspan=2, column=0, columnspan=3, pady=25)

    # label
    ttk.Label(text="Url to check", font=("Roboto", 13)).grid(row=3)

    # Textbox
    url = tk.StringVar()
    ui_url = ttk.Entry(textvariable=url, width=40)

    # Button
    ttk.Button(root, text="Check Connection", command=lambda: enable_partial_url(partial_bool.get(), ui_url.get(), mute=False)).grid(row=3, column=2, padx=10)
    ui_url.grid(row=3, column=1, padx=10)

    # checkbox implementation
    partial_bool = BooleanVar()
    partial = ttk.Checkbutton(root, text="Autocomplete URL elements", variable=partial_bool, onvalue=True, offvalue=False, command=lambda: enable_partial_url(partial_bool.get(), ui_url.get(), mute=True))
    partial.grid(row=4, columnspan=3, pady=15, sticky="n")

    # speedtest button implementation
    down_speed = StringVar()
    up_speed = StringVar()

    down_speed_label = ttk.Label(root, text=f"", textvariable=down_speed)
    up_speed_label = ttk.Label(root, text=f"", textvariable=up_speed)

    ttk.Button(root, text="Check Internet Speed", command=lambda: web_check.get_speed(down_speed, up_speed)).grid(row=4, column=2, padx=10)

    down_speed_label.grid(row=5, column=2, columnspan=2)
    up_speed_label.grid(row=6, column=2, columnspan=2)

    # display zone
    app.mainloop()


if __name__ == '__main__':
    main()
