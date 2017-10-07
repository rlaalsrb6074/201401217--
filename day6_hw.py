Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.shape("turtle")#거북이그래픽모듈을 킨다
>>> bgcolor("black")#그래픽의 배경색을 검은색으로 바꾼다.
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bgcolor("black")#그래픽의 배경색을 검은색으로 바꾼다.
NameError: name 'bgcolor' is not defined
>>> #에러가 나왓으므로 에러를 찾는다 앞에 거북이 명령어를 실행을 안하여 에러가 발생하였다
>>> t.bgcolor("black")#그래픽의 배경색을 검은색으로 바꾼다.
>>> t.color("blue")#거북이의 색을 파란색으로 바꾼다.
>>> angle=69#거북이의 회전값을 69로 놓는다
>>> t.speed(0)#거북이의 속도를 0으로 놓아 가장빠르게한다
>>> for x in range(300):#x를 0부터 299까지바꾸면서 200번 실행한다
	t.fw(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    t.fw(x)#거북이를 x만큼 앞으로 이동시킨다.
AttributeError: module 'turtle' has no attribute 'fw'
>>> #입력줄 2번째에서 에러가 발생하여 수정하여 다시 실행한다
>>> for x in range(300):#x를 0부터 299까지바꾸면서 200번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> t.up()#거북이를 이동시키려하는데 이동시 펜이 칠해지는것이 싫어 거북이 꼬리를 올린다.
>>> t.left(45)#거북이를 왼쪽으로 45도꺽어준다.
>>> t.fd(300)
>>> #거북이를 시작점주변으로 보내기 위해 forward와 left를 실행하였다.
>>> t.color("red")#거북이의 색을 붉은색으로 바꾼다.
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> #실수를 했다. 거북이 꼬리를 올려서 색칠이 되지 않았다.
>>> t.left(80)
>>> t.fd(150)
>>> t.fd(50)
>>> t.down()
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> t.color("purple")
>>> t.up():
	
SyntaxError: invalid syntax
>>> t.up()
>>> t.left(85)
>>> t.fd(200)
>>> t.left(90)
>>> t.left(180)
>>> t.fd(50)
>>> #전의 작업처럼 중심과 인접하게 거북이를 위치해 놓는다.
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> #또 실수를 했다...다시 원점인접하게 보내야고 작업을 해야겠다.
>>> t. left(10)
>>> t.fd(250)
>>> t.left(90)
>>> t.fd(90)
>>> t.down()
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> t.left(30)
>>> t.fd(300)
>>> t.left(90)
>>> t.fd(50)
>>> t.color("yellow")
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> t.left(45)
>>> t.fd(350)
>>> t.color("white")
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> t. left(90)
>>> t.fd(200)
>>> t.color("black")
>>> for x in range(250):#x를 0부터 245까지바꾸면서 250번 실행한다
	t.fd(x)#거북이를 x만큼 앞으로 이동시킨다.
	t.lt(angle)#거북이를 왼쪽으로 이전에 입력시킨 angle(69)만큼 이동시킨다.

	
>>> #이렇게 간단한 그림을 그린이유는 이번 명절때 친가댁에서의 상상을 초월하는 극한 노동과 어르신분들의 현실적인 팩트폭격(일명 잔소리)에 의해 흔적조차 찾아보기 힘든 저의 멘탈을 표현하였습니다.
