import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

url = 'https://randomfox.ca/floof'

def show_image(image) -> None:
    root = tk.Tk()
    root.title("Fox")

    tk_image = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=tk_image)
    label.pack()

    root.mainloop()

def main() -> None:
    response = requests.get(url)

    try:
        image_url = response.json()["image"]
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        show_image(image)
    except Exception as error:
        print(f'Error: {error}')

if __name__ == '__main__':
    main()
