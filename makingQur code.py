# #making qurcode using python
# import qrcode

# data = "Hello, this is my first QR code!"

# img = qrcode.make(data)

# img.save("my_qr.png")

# print("QR code successfully created!")

# import qrcode

# data = "https://www.google.com"

# img = qrcode.make(data)
# img.save("google_qr.png")

# print("QR code created successfully!")

# import qrcode
# import qrcode.image.svg

# # Data jo QR code mein daalna hai
# data = "Hello, this is my first QR code!"

# # SVG factory ka use karke bina Pillow ke QR banana
# factory = qrcode.image.svg.SvgImage
# img = qrcode.make(data, image_factory=factory)

# # SVG format mein save karein
# img.save("my_qr.svg")

# print("QR code successfully created as my_qr.svg!")

# import qrcode

# data = "Hello Sumit"

# img = qrcode.make(data)
# img.save("my_qr.png")

# print("QR Code created successfully!")


# import qrcode as qr

# img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=1")

# img.save("wscube_youtube.png")

#trying to making a game that make me helpful for student who u are  looking for that type games

# n  = int(input("Enter your favourite words"))

# while n >= len(5):
#     print("You are new gamer level")


#game 1first game 

# lives = 3

# while lives > 0:
#     print("Game is running...")
#     print("lives:", lives)

#     choice = input("Do you want to contine the game")

#     if choice == "no":
#         break

#     lives -= 1
#     print("Game Over!")

#game 2 making monster battle game

# expected_marks = 80
# actual_marks = 65

# difference = abs(expected_marks - actual_marks)

# print("DIfference:", difference)

# print(min(18, 5, 20, 3, 8))

# numbers = [12, 5, 30, 2, 18]

# smallest = min(numbers)

# print(smallest)

# names = ["Ravi", "Aman", "Karan"]

# print(min(names))

# print(max(10, 5, 20, 3, 8))

# a = float(input("Enter first area: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# s = (a + b + c) / 2

# area = (s * ( s-a) * (s - b) * (s -c)) ** 0.5

# print("area of triangle with given side is", round(area, 2))

# principle = float(input("Enter principle amount: "))
# rate = float(input("Enter interest rate: "))
# time = float(input("Enter time: ")) 
# s1 = (principle * rate * time) / 100

# print("simple interest is", s1)

principle = float(input("Enter principle amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: ")) 
amount1 = principle * (1 + rate/100) ** time
amount2 = principle * pow((1 + rate/ 100), time)
print(round(amount2, 2))
c1 = amount2  - principle
print("compound interest", round(c1))
