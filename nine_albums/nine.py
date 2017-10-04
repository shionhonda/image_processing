from PIL import Image

# Load and resize JPEG pictures
img1 = Image.open("./1.jpg")
img1 = img1.resize((200, 200))
img2 = Image.open("./2.jpg")
img2 = img2.resize((200, 200))
img3 = Image.open("./3.jpg")
img3 = img3.resize((200, 200))
img4 = Image.open("./4.jpg")
img4 = img4.resize((200, 200)) 
img5 = Image.open("./5.jpg")
img5 = img5.resize((200, 200))
img6 = Image.open("./6.jpg")
img6 = img6.resize((200, 200)) 
img7 = Image.open("./7.jpg")
img7 = img7.resize((200, 200))
img8 = Image.open("./8.jpg")
img8 = img8.resize((200, 200))
img9 = Image.open("./9.jpg")
img9 = img9.resize((200,200)) 

# New canvas
canvas = Image.new('RGB', (600, 600), (255, 255, 255))

# Paste pictures on the canvas
canvas.paste(img1, (0 ,0))
canvas.paste(img2, (200, 0))
canvas.paste(img3, (400, 0))
canvas.paste(img4, (0 ,200))   
canvas.paste(img5, (200, 200)) 
canvas.paste(img6, (400, 200))
canvas.paste(img7, (0 ,400))   
canvas.paste(img8, (200, 400)) 
canvas.paste(img9, (400, 400)) 
canvas.save('nine.jpg')     
