# -*-coding: utf-8
from turtle import *
import random


def key_left():
    my.seth(180)  # turtle.seth(to_angle) 거북이 각도 설정
    my.fd(onestep)  # fd: 향한 방향으로 onestep 만큼 이동
    if (my.xcor() < -300):  # xcor()  x 좌표 반환
        my.setx(-300)  # 맵 탈출 제어


# 오른쪽 이동
def key_right():
    my.seth(0)
    my.fd(onestep)
    if (my.xcor() > 300):
        my.setx(300)

    # 위쪽 이동


def key_up():
    my.seth(90)
    my.fd(onestep)
    if (my.ycor() > 300):
        my.sety(300)


# 아래쪽 이동
def key_down():
    my.seth(270)
    my.fd(onestep)
    if (my.ycor() < -290):
        my.sety(-290)


def draw():
    alive = True
    while (alive):
        listen()
        if (my.xcor() >= 250 and my.xcor() <= 270 and my.ycor() <= -250 and my.ycor() >= -270):
            print(" Your Turtle is Dead!")
            alive = False
        update()


def main():
    global onestep
    onestep = 20

    setup(600, 600)  # 600 * 600

    global my
    my = Turtle()
    my.shape("turtle")
    my.up()  # up : 펜을 올려서 그림을 그리지 않음. up 이 없으면 그림그림
    my.setpos(-250, 250)

    onkey(key_right, "Right")
    onkey(key_left, "Left")
    onkey(key_up, "Up")
    onkey(key_down, "Down")

    endPointPainter = Turtle()
    endPointPainter.up()
    # 도착지점을 그림
    endPointPainter.setpos(250, -250)
    endPointPainter.down()
    endPointPainter.seth(0)
    endPointPainter.fd(20)
    endPointPainter.seth(270)
    endPointPainter.fd(20)
    endPointPainter.seth(180)
    endPointPainter.fd(20)
    endPointPainter.seth(90)
    endPointPainter.fd(20)
    endPointPainter.ht()  # 거북이숨기기

    draw()


if __name__ == "__main__":
    main()