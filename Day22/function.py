def go_up(paddle):
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down(paddle):
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

