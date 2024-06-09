from turtle import *




# ძირითადი ტურტლის შექმნა
speed(2)
penup()
goto(-100, -100)
pendown()
color("gray")
begin_fill()

# მთავარი კორპუსის დახატვა
forward(200)  # ქვედა მხარე
left(90)
forward(100)  # მარცხენა მხარე
left(90)
forward(200)  # ზედა მხარე
left(90)
forward(100)  # მარჯვენა მხარე
left(90)
end_fill()

# მარცხენა კოშკის დახატვა
penup()
goto(-130, 0)
pendown()
begin_fill()
forward(60)  # ქვედა მხარე
left(90)
forward(100)  # მარცხენა მხარე
left(90)
forward(60)  # ზედა მხარე
left(90)
forward(100)  # მარჯვენა მხარე
left(90)
end_fill()

# მარჯვენა კოშკის დახატვა
penup()
goto(70, 0)
pendown()
begin_fill()
forward(60)  # ქვედა მხარე
left(90)
forward(100)  # მარცხენა მხარე
left(90)
forward(60)  # ზედა მხარე
left(90)
forward(100)  # მარჯვენა მხარე
left(90)
end_fill()

# მარცხენა კოშკის სახურავის დახატვა
penup()
goto(-130, 100)
pendown()
color("black")
begin_fill()
left(30)
forward(60)
left(120)
forward(60)
left(120)
forward(60)
left(120)
end_fill()
right(30)

# მარჯვენა კოშკის სახურავის დახატვა
penup()
goto(70, 100)
pendown()
begin_fill()
left(30)
forward(60)
left(120)
forward(60)
left(120)
forward(60)
left(120)
end_fill()
right(30)

# კარის დახატვა
penup()
goto(-30, -100)
pendown()
color("brown")
begin_fill()
forward(60)  # ქვედა მხარე
left(90)
forward(60)  # მარცხენა მხარე
left(90)
forward(60)  # ზედა მხარე
left(90)
forward(60)  # მარჯვენა მხარე
left(90)
end_fill()


exitonclick()