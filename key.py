'''
Control the keyboard.
'''

import pyautogui as pag
pag.PAUSE = 0


def up():
    pag.keyDown('w')
    pag.keyUp('a')
    pag.keyUp('s')
    pag.keyUp('d')


def left():
    pag.keyUp('w')
    pag.keyDown('a')
    pag.keyUp('s')
    pag.keyUp('d')


def down():
    pag.keyUp('w')
    pag.keyUp('a')
    pag.keyDown('s')
    pag.keyUp('d')


def right():
    pag.keyUp('w')
    pag.keyUp('a')
    pag.keyUp('s')
    pag.keyDown('d')


def upleft():
    pag.keyDown('w')
    pag.keyDown('a')
    pag.keyUp('s')
    pag.keyUp('d')


def leftdown():
    pag.keyUp('w')
    pag.keyDown('a')
    pag.keyDown('s')
    pag.keyUp('d')


def downright():
    pag.keyUp('w')
    pag.keyUp('a')
    pag.keyDown('s')
    pag.keyDown('d')


def rightup():
    pag.keyDown('w')
    pag.keyUp('a')
    pag.keyUp('s')
    pag.keyDown('d')


def null():
    pag.keyUp('w')
    pag.keyUp('a')
    pag.keyUp('s')
    pag.keyUp('d')
