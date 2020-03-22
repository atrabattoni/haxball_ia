import key


def moveTowardBall(xp, yp, xb, yb):
    if xb > xp:
        if yb > yp:
            key.rightup()
        elif yb < yp:
            key.downright()
        else:
            key.right()
    elif xb < xp:
        if yb > yp:
            key.upleft()
        elif yb < yp:
            key.leftdown()
        else:
            key.left()
    else:
        if yb > yp:
            key.up()
        elif yb < yp:
            key.down()
        else:
            key.null()
