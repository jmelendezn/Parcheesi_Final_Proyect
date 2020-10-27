from graphics import *

def main():
    win = GraphWin('Game', 600,700)
    win.setCoords(-100,-100,600,700)
    win.setBackground(color_rgb(255,252,242))

    # Parcheesi Title
    title = Text(Point(250,640),"PARCHEESI")
    title.setSize(30)
    title.setStyle("bold")
    title.draw(win)

    # Board Rect
    rec = Rectangle(Point(0,0),Point(500,500))
    rec.draw(win)
    
    # Creacion
    rec1 = Rectangle(Point(0,0), Point(175,175))
    
    rec2 = Rectangle(Point(0,325), Point(175,500))
    
    rec3 = Rectangle(Point(325,325), Point(500,500))
    
    rec4 = Rectangle(Point(325,0), Point(500,175))
    
    recMedio = Rectangle(Point(180,180), Point(320,320))

    cir1 = Circle(Point(87.5,87.5),85)
    cir2 = Circle(Point(412.5,87.5),85)
    cir3 = Circle(Point(412.5,412.5),85)
    cir4 = Circle(Point(87.5,412.5),85)
    
    recA10 = Rectangle(Point(175,0), Point(225,20))
    recA11 = Rectangle(Point(225,0), Point(275,20))
    recA12 = Rectangle(Point(275,0), Point(325,20))
    recA20 = Rectangle(Point(175,20), Point(225,40))
    recA21 = Rectangle(Point(225,20), Point(275,40))
    recA22 = Rectangle(Point(275,20), Point(325,40))
    recA30 = Rectangle(Point(175,40), Point(225,60))
    recA31 = Rectangle(Point(225,40), Point(275,60))
    recA32 = Rectangle(Point(275,40), Point(325,60))
    recA40 = Rectangle(Point(175,60), Point(225,80))
    recA41 = Rectangle(Point(225,60), Point(275,80))
    recA42 = Rectangle(Point(275,60), Point(325,80))
    recA50 = Rectangle(Point(175,80), Point(225,100))
    recA51 = Rectangle(Point(225,80), Point(275,100))
    recA52 = Rectangle(Point(275,80), Point(325,100))
    recA60 = Rectangle(Point(175,100), Point(225,120))
    recA61 = Rectangle(Point(225,100), Point(275,120))
    recA62 = Rectangle(Point(275,100), Point(325,120))
    recA70 = Rectangle(Point(175,120), Point(225,140))
    recA71 = Rectangle(Point(225,120), Point(275,140))
    recA72 = Rectangle(Point(275,120), Point(325,140))
    recA80 = Rectangle(Point(175,140), Point(225,160))
    recA81 = Rectangle(Point(225,140), Point(275,160))
    recA82 = Rectangle(Point(275,140), Point(325,160))

    recB10 = Rectangle(Point(0,175), Point(20,225))
    recB11 = Rectangle(Point(0,225), Point(20,275))
    recB12 = Rectangle(Point(0,275), Point(20,325))
    recB20 = Rectangle(Point(20,175), Point(40,225))
    recB21 = Rectangle(Point(20,225), Point(40,275))
    recB22 = Rectangle(Point(20,275), Point(40,325))
    recB30 = Rectangle(Point(40,175), Point(60,225))
    recB31 = Rectangle(Point(40,225), Point(60,275))
    recB32 = Rectangle(Point(40,275), Point(60,325))
    recB40 = Rectangle(Point(60,175), Point(80,225))
    recB41 = Rectangle(Point(60,225), Point(80,275))
    recB42 = Rectangle(Point(60,275), Point(80,325))
    recB50 = Rectangle(Point(80,175), Point(100,225))
    recB51 = Rectangle(Point(80,225), Point(100,275))
    recB52 = Rectangle(Point(80,275), Point(100,325))
    recB60 = Rectangle(Point(100,175), Point(120,225))
    recB61 = Rectangle(Point(100,225), Point(120,275))
    recB62 = Rectangle(Point(100,275), Point(120,325))
    recB70 = Rectangle(Point(120,175), Point(140,225))
    recB71 = Rectangle(Point(120,225), Point(140,275))
    recB72 = Rectangle(Point(120,275), Point(140,325))
    recB80 = Rectangle(Point(140,175), Point(160,225))
    recB81 = Rectangle(Point(140,225), Point(160,275))
    recB82 = Rectangle(Point(140,275), Point(160,325))

    recC10 = Rectangle(Point(175,340), Point(225,360))
    recC11 = Rectangle(Point(225,340), Point(275,360))
    recC12 = Rectangle(Point(275,340), Point(325,360))
    recC20 = Rectangle(Point(175,360), Point(225,380))
    recC21 = Rectangle(Point(225,360), Point(275,380))
    recC22 = Rectangle(Point(275,360), Point(325,380))
    recC30 = Rectangle(Point(175,380), Point(225,400))
    recC31 = Rectangle(Point(225,380), Point(275,400))
    recC32 = Rectangle(Point(275,380), Point(325,400))
    recC40 = Rectangle(Point(175,400), Point(225,420))
    recC41 = Rectangle(Point(225,400), Point(275,420))
    recC42 = Rectangle(Point(275,400), Point(325,420))
    recC50 = Rectangle(Point(175,420), Point(225,440))
    recC51 = Rectangle(Point(225,420), Point(275,440))
    recC52 = Rectangle(Point(275,420), Point(325,440))
    recC60 = Rectangle(Point(175,440), Point(225,460))
    recC61 = Rectangle(Point(225,440), Point(275,460))
    recC62 = Rectangle(Point(275,440), Point(325,460))
    recC70 = Rectangle(Point(175,460), Point(225,480))
    recC71 = Rectangle(Point(225,460), Point(275,480))
    recC72 = Rectangle(Point(275,460), Point(325,480))
    recC80 = Rectangle(Point(175,480), Point(225,500))
    recC81 = Rectangle(Point(225,480), Point(275,500))
    recC82 = Rectangle(Point(275,480), Point(325,500))

    recD10 = Rectangle(Point(340,175), Point(360,225))
    recD11 = Rectangle(Point(340,225), Point(360,275))
    recD12 = Rectangle(Point(340,275), Point(360,325))
    recD20 = Rectangle(Point(360,175), Point(380,225))
    recD21 = Rectangle(Point(360,225), Point(380,275))
    recD22 = Rectangle(Point(360,275), Point(380,325))
    recD30 = Rectangle(Point(380,175), Point(400,225))
    recD31 = Rectangle(Point(380,225), Point(400,275))
    recD32 = Rectangle(Point(380,275), Point(400,325))
    recD40 = Rectangle(Point(400,175), Point(420,225))
    recD41 = Rectangle(Point(400,225), Point(420,275))
    recD42 = Rectangle(Point(400,275), Point(420,325))
    recD50 = Rectangle(Point(420,175), Point(440,225))
    recD51 = Rectangle(Point(420,225), Point(440,275))
    recD52 = Rectangle(Point(420,275), Point(440,325))
    recD60 = Rectangle(Point(440,175), Point(460,225))
    recD61 = Rectangle(Point(440,225), Point(460,275))
    recD62 = Rectangle(Point(440,275), Point(460,325))
    recD70 = Rectangle(Point(460,175), Point(480,225))
    recD71 = Rectangle(Point(460,225), Point(480,275))
    recD72 = Rectangle(Point(460,275), Point(480,325))
    recD80 = Rectangle(Point(480,175), Point(500,225))
    recD81 = Rectangle(Point(480,225), Point(500,275))
    recD82 = Rectangle(Point(480,275), Point(500,325))

    # Color rectangulos
    recMedio.setFill(color_rgb(205,108,107))
    rec1.setFill(color_rgb(255,213,0))
    rec2.setFill(color_rgb(0,80,157))
    rec3.setFill(color_rgb(239,35,60))
    rec4.setFill(color_rgb(122,199,79))

    cir1.setFill(color_rgb(255,252,242))
    cir2.setFill(color_rgb(255,252,242))
    cir3.setFill(color_rgb(255,252,242))
    cir4.setFill(color_rgb(255,252,242))

    recA11.setFill(color_rgb(144,224,239))
    recA21.setFill(color_rgb(230,57,70))
    recA31.setFill(color_rgb(230,57,70))
    recA41.setFill(color_rgb(230,57,70))
    recA50.setFill(color_rgb(144,224,239))
    recA51.setFill(color_rgb(230,57,70))
    recA52.setFill(color_rgb(144,224,239))
    recA61.setFill(color_rgb(230,57,70))
    recA71.setFill(color_rgb(230,57,70))
    recA81.setFill(color_rgb(230,57,70))

    recB11.setFill(color_rgb(144,224,239))
    recB21.setFill(color_rgb(230,57,70))
    recB31.setFill(color_rgb(230,57,70))
    recB41.setFill(color_rgb(230,57,70))
    recB50.setFill(color_rgb(144,224,239))
    recB51.setFill(color_rgb(230,57,70))
    recB52.setFill(color_rgb(144,224,239))
    recB61.setFill(color_rgb(230,57,70))
    recB71.setFill(color_rgb(230,57,70))
    recB81.setFill(color_rgb(230,57,70))

    recC11.setFill(color_rgb(230,57,70))
    recC21.setFill(color_rgb(230,57,70))
    recC31.setFill(color_rgb(230,57,70))
    recC40.setFill(color_rgb(144,224,239))
    recC41.setFill(color_rgb(230,57,70))
    recC42.setFill(color_rgb(144,224,239))
    recC51.setFill(color_rgb(230,57,70))
    recC61.setFill(color_rgb(230,57,70))
    recC71.setFill(color_rgb(230,57,70))
    recC81.setFill(color_rgb(144,224,239))

    recD11.setFill(color_rgb(230,57,70))
    recD21.setFill(color_rgb(230,57,70))
    recD31.setFill(color_rgb(230,57,70))
    recD40.setFill(color_rgb(144,224,239))
    recD41.setFill(color_rgb(230,57,70))
    recD42.setFill(color_rgb(144,224,239))
    recD51.setFill(color_rgb(230,57,70))
    recD61.setFill(color_rgb(230,57,70))
    recD71.setFill(color_rgb(230,57,70))
    recD81.setFill(color_rgb(144,224,239))


    # Draw
    rec1.draw(win)
    rec2.draw(win)
    rec3.draw(win)
    rec4.draw(win)
    
    recMedio.draw(win)

    cir1.draw(win)
    cir2.draw(win)
    cir3.draw(win)
    cir4.draw(win)
    
    rectA = [recA10,recA11,recA12,recA20,recA21,recA22,recA30,recA31,recA32,recA40,recA41,recA42,recA50,recA51,recA52,recA60,recA61,recA62,recA70,recA71,recA72,recA80,recA81,recA82]
    for A in rectA:
        A.draw(win)

    rectB = [recB10,recB11,recB12,recB20,recB21,recB22,recB30,recB31,recB32,recB40,recB41,recB42,recB50,recB51,recB52,recB60,recB61,recB62,recB70,recB71,recB72,recB80,recB81,recB82]
    for B in rectB:
        B.draw(win)

    rectC = [recC10,recC11,recC12,recC20,recC21,recC22,recC30,recC31,recC32,recC40,recC41,recC42,recC50,recC51,recC52,recC60,recC61,recC62,recC70,recC71,recC72,recC80,recC81,recC82]
    for C in rectC:
        C.draw(win)

    rectD = [recD10,recD11,recD12,recD20,recD21,recD22,recD30,recD31,recD32,recD40,recD41,recD42,recD50,recD51,recD52,recD60,recD61,recD62,recD70,recD71,recD72,recD80,recD81,recD82]
    for D in rectD:
        D.draw(win)

    



    win.getMouse()

main()


