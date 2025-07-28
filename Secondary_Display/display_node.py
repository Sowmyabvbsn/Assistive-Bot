#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageTk
# import rospy

class SecondaryDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistive Bot - Secondary Display")
        self.root.geometry("800x480")
        self.root.configure(bg='black')

        # Load map
        self.map_img = Image.open("assets/mall_map.png")
        self.map_img = self.map_img.resize((500, 400), Image.ANTIALIAS)
        self.map_tk = ImageTk.PhotoImage(self.map_img)

        # Load banner
        self.banner_img = Image.open("assets/banner_sample.jpg")
        self.banner_img = self.banner_img.resize((250, 100), Image.ANTIALIAS)
        self.banner_tk = ImageTk.PhotoImage(self.banner_img)

        # Display map
        self.map_label = tk.Label(root, image=self.map_tk)
        self.map_label.place(x=20, y=40)

        # Display banner
        self.banner_label = tk.Label(root, image=self.banner_tk)
        self.banner_label.place(x=550, y=40)

        # Discount highlight
        self.info_label = tk.Label(root, text="Discount: Store A - 50%", fg="white", bg="black", font=("Helvetica", 16))
        self.info_label.place(x=550, y=180)

    def update_banner(self, new_image_path):
        new_img = Image.open(new_image_path)
        new_img = new_img.resize((250, 100), Image.ANTIALIAS)
        self.banner_tk = ImageTk.PhotoImage(new_img)
        self.banner_label.config(image=self.banner_tk)

if __name__ == '__main__':
    rospy.init_node('secondary_display_node', anonymous=True)
    root = tk.Tk()
    app = SecondaryDisplay(root)
    root.mainloop()
