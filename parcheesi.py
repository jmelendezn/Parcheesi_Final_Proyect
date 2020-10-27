from graphics import *
from random import *

class Parcheesi:
    def __init__(self,win):
        """
        docstring
        """
        self.win = win
        self.rec1 = Rectangle(Point(0,0), Point(175,175))
    
        self.rec2 = Rectangle(Point(0,325), Point(175,500))
        
        self.rec3 = Rectangle(Point(325,325), Point(500,500))
        
        self.rec4 = Rectangle(Point(325,0), Point(500,175))
        
        self.recMedio = Rectangle(Point(180,180), Point(320,320))

        self.cir1 = Circle(Point(87.5,87.5),85)
        self.cir2 = Circle(Point(412.5,87.5),85)
        self.cir3 = Circle(Point(412.5,412.5),85)
        self.cir4 = Circle(Point(87.5,412.5),85)
        
        self.recA10 = Rectangle(Point(175,0), Point(225,20))
        self.recA11 = Rectangle(Point(225,0), Point(275,20))
        self.recA12 = Rectangle(Point(275,0), Point(325,20))
        self.recA20 = Rectangle(Point(175,20), Point(225,40))
        self.recA21 = Rectangle(Point(225,20), Point(275,40))
        self.recA22 = Rectangle(Point(275,20), Point(325,40))
        self.recA30 = Rectangle(Point(175,40), Point(225,60))
        self.recA31 = Rectangle(Point(225,40), Point(275,60))
        self.recA32 = Rectangle(Point(275,40), Point(325,60))
        self.recA40 = Rectangle(Point(175,60), Point(225,80))
        self.recA41 = Rectangle(Point(225,60), Point(275,80))
        self.recA42 = Rectangle(Point(275,60), Point(325,80))
        self.recA50 = Rectangle(Point(175,80), Point(225,100))
        self.recA51 = Rectangle(Point(225,80), Point(275,100))
        self.recA52 = Rectangle(Point(275,80), Point(325,100))
        self.recA60 = Rectangle(Point(175,100), Point(225,120))
        self.recA61 = Rectangle(Point(225,100), Point(275,120))
        self.recA62 = Rectangle(Point(275,100), Point(325,120))
        self.recA70 = Rectangle(Point(175,120), Point(225,140))
        self.recA71 = Rectangle(Point(225,120), Point(275,140))
        self.recA72 = Rectangle(Point(275,120), Point(325,140))
        self.recA80 = Rectangle(Point(175,140), Point(225,160))
        self.recA81 = Rectangle(Point(225,140), Point(275,160))
        self.recA82 = Rectangle(Point(275,140), Point(325,160))

        self.recB10 = Rectangle(Point(0,175), Point(20,225))
        self.recB11 = Rectangle(Point(0,225), Point(20,275))
        self.recB12 = Rectangle(Point(0,275), Point(20,325))
        self.recB20 = Rectangle(Point(20,175), Point(40,225))
        self.recB21 = Rectangle(Point(20,225), Point(40,275))
        self.recB22 = Rectangle(Point(20,275), Point(40,325))
        self.recB30 = Rectangle(Point(40,175), Point(60,225))
        self.recB31 = Rectangle(Point(40,225), Point(60,275))
        self.recB32 = Rectangle(Point(40,275), Point(60,325))
        self.recB40 = Rectangle(Point(60,175), Point(80,225))
        self.recB41 = Rectangle(Point(60,225), Point(80,275))
        self.recB42 = Rectangle(Point(60,275), Point(80,325))
        self.recB50 = Rectangle(Point(80,175), Point(100,225))
        self.recB51 = Rectangle(Point(80,225), Point(100,275))
        self.recB52 = Rectangle(Point(80,275), Point(100,325))
        self.recB60 = Rectangle(Point(100,175), Point(120,225))
        self.recB61 = Rectangle(Point(100,225), Point(120,275))
        self.recB62 = Rectangle(Point(100,275), Point(120,325))
        self.recB70 = Rectangle(Point(120,175), Point(140,225))
        self.recB71 = Rectangle(Point(120,225), Point(140,275))
        self.recB72 = Rectangle(Point(120,275), Point(140,325))
        self.recB80 = Rectangle(Point(140,175), Point(160,225))
        self.recB81 = Rectangle(Point(140,225), Point(160,275))
        self.recB82 = Rectangle(Point(140,275), Point(160,325))

        self.recC10 = Rectangle(Point(175,340), Point(225,360))
        self.recC11 = Rectangle(Point(225,340), Point(275,360))
        self.recC12 = Rectangle(Point(275,340), Point(325,360))
        self.recC20 = Rectangle(Point(175,360), Point(225,380))
        self.recC21 = Rectangle(Point(225,360), Point(275,380))
        self.recC22 = Rectangle(Point(275,360), Point(325,380))
        self.recC30 = Rectangle(Point(175,380), Point(225,400))
        self.recC31 = Rectangle(Point(225,380), Point(275,400))
        self.recC32 = Rectangle(Point(275,380), Point(325,400))
        self.recC40 = Rectangle(Point(175,400), Point(225,420))
        self.recC41 = Rectangle(Point(225,400), Point(275,420))
        self.recC42 = Rectangle(Point(275,400), Point(325,420))
        self.recC50 = Rectangle(Point(175,420), Point(225,440))
        self.recC51 = Rectangle(Point(225,420), Point(275,440))
        self.recC52 = Rectangle(Point(275,420), Point(325,440))
        self.recC60 = Rectangle(Point(175,440), Point(225,460))
        self.recC61 = Rectangle(Point(225,440), Point(275,460))
        self.recC62 = Rectangle(Point(275,440), Point(325,460))
        self.recC70 = Rectangle(Point(175,460), Point(225,480))
        self.recC71 = Rectangle(Point(225,460), Point(275,480))
        self.recC72 = Rectangle(Point(275,460), Point(325,480))
        self.recC80 = Rectangle(Point(175,480), Point(225,500))
        self.recC81 = Rectangle(Point(225,480), Point(275,500))
        self.recC82 = Rectangle(Point(275,480), Point(325,500))

        self.recD10 = Rectangle(Point(340,175), Point(360,225))
        self.recD11 = Rectangle(Point(340,225), Point(360,275))
        self.recD12 = Rectangle(Point(340,275), Point(360,325))
        self.recD20 = Rectangle(Point(360,175), Point(380,225))
        self.recD21 = Rectangle(Point(360,225), Point(380,275))
        self.recD22 = Rectangle(Point(360,275), Point(380,325))
        self.recD30 = Rectangle(Point(380,175), Point(400,225))
        self.recD31 = Rectangle(Point(380,225), Point(400,275))
        self.recD32 = Rectangle(Point(380,275), Point(400,325))
        self.recD40 = Rectangle(Point(400,175), Point(420,225))
        self.recD41 = Rectangle(Point(400,225), Point(420,275))
        self.recD42 = Rectangle(Point(400,275), Point(420,325))
        self.recD50 = Rectangle(Point(420,175), Point(440,225))
        self.recD51 = Rectangle(Point(420,225), Point(440,275))
        self.recD52 = Rectangle(Point(420,275), Point(440,325))
        self.recD60 = Rectangle(Point(440,175), Point(460,225))
        self.recD61 = Rectangle(Point(440,225), Point(460,275))
        self.recD62 = Rectangle(Point(440,275), Point(460,325))
        self.recD70 = Rectangle(Point(460,175), Point(480,225))
        self.recD71 = Rectangle(Point(460,225), Point(480,275))
        self.recD72 = Rectangle(Point(460,275), Point(480,325))
        self.recD80 = Rectangle(Point(480,175), Point(500,225))
        self.recD81 = Rectangle(Point(480,225), Point(500,275))
        self.recD82 = Rectangle(Point(480,275), Point(500,325))

        self.rectA = [self.recA10,self.recA11,self.recA12,self.recA20,self.recA21,self.recA22,self.recA30,self.recA31,self.recA32,self.recA40,self.recA41,self.recA42,self.recA50,self.recA51,self.recA52,self.recA60,self.recA61,self.recA62,self.recA70,self.recA71,self.recA72,self.recA80,self.recA81,self.recA82]
        self.rectB = [self.recB10,self.recB11,self.recB12,self.recB20,self.recB21,self.recB22,self.recB30,self.recB31,self.recB32,self.recB40,self.recB41,self.recB42,self.recB50,self.recB51,self.recB52,self.recB60,self.recB61,self.recB62,self.recB70,self.recB71,self.recB72,self.recB80,self.recB81,self.recB82]
        self.rectC = [self.recC10,self.recC11,self.recC12,self.recC20,self.recC21,self.recC22,self.recC30,self.recC31,self.recC32,self.recC40,self.recC41,self.recC42,self.recC50,self.recC51,self.recC52,self.recC60,self.recC61,self.recC62,self.recC70,self.recC71,self.recC72,self.recC80,self.recC81,self.recC82]
        self.rectD = [self.recD10,self.recD11,self.recD12,self.recD20,self.recD21,self.recD22,self.recD30,self.recD31,self.recD32,self.recD40,self.recD41,self.recD42,self.recD50,self.recD51,self.recD52,self.recD60,self.recD61,self.recD62,self.recD70,self.recD71,self.recD72,self.recD80,self.recD81,self.recD82]

        self.b01  = 0
        self.b02  = 0
        self.b03  = 0
        self.b04  = 0
        self.b05  = 0
        self.b06  = 0
        self.b07  = 0
        self.b08  = 0
        self.b09  = 0
        self.b10  = 0
        self.b11  = 0
        self.b12  = 0
        self.b13  = 0
        self.b14  = 0
        self.b15  = 0
        self.b16  = 0
        self.b17  = 0
        self.b18  = 0
        self.b19  = 0
        self.b20  = 0
        self.b21  = 0
        self.b22  = 0
        self.b23  = 0
        self.b24  = 0
        self.b25  = 0
        self.b26  = 0
        self.b27  = 0
        self.b28  = 0
        self.b29  = 0
        self.b30  = 0
        self.b31  = 0
        self.b32  = 0
        self.b33  = 0
        self.b34  = 0
        self.b35  = 0
        self.b36  = 0
        self.b37  = 0
        self.b38  = 0
        self.b39  = 0
        self.b40  = 0
        self.b41  = 0
        self.b42  = 0
        self.b43  = 0
        self.b44  = 0
        self.b45  = 0
        self.b46  = 0
        self.b47  = 0
        self.b48  = 0
        self.b49  = 0
        self.b50  = 0
        self.b51  = 0
        self.b52  = 0
        self.b53  = 0
        self.b54  = 0
        self.b55  = 0
        self.b56  = 0
        self.b57  = 0
        self.b58  = 0
        self.b59  = 0
        self.b60  = 0
        self.b61  = 0
        self.b62  = 0
        self.b63  = 0
        self.b64  = 0
        self.b65  = 0
        self.b66  = 0
        self.b67  = 0
        self.b68  = 0

        self.board = [self.b01,self.b02,self.b03,self.b04,self.b05,self.b06,self.b07,self.b08,self.b09,self.b10,self.b11,self.b12,self.b13,self.b14,self.b15,
        self.b16,self.b17,self.b18,self.b19,self.b20,self.b21,self.b22,self.b23,self.b24,self.b25,self.b26,self.b27,self.b28,self.b29,self.b30,self.b31,self.b32,
        self.b33,self.b34,self.b35,self.b36,self.b37,self.b38,self.b39,self.b40,self.b41,self.b42,self.b43,self.b44,self.b45,self.b46,self.b47,self.b48,self.b49,
        self.b50,self.b51,self.b52,self.b53,self.b54,self.b55,self.b56,self.b57,self.b58,self.b59,self.b60,self.b61,self.b62,self.b63,self.b64,self.b65,self.b66,self.b67,self.b68]

        self.starting_point = [0,51,34,17]
        self.posicion_actual = [0,51,34,17]

        self.movidas1 = 0
        self.movidas2 = 0
        self.movidas3 = 0
        self.movidas4 = 0
        self.posicion = [self.movidas1,self.movidas2,self.movidas3,self.movidas4]

        self.turno = 0
        self.jugadores = ["Jugador #1", "Jugador #2", "Jugador #3", "Jugador #4"]
        



    def draw_game(self):
        
        self.win.setCoords(-100,-100,600,700)
        self.win.setBackground(color_rgb(255,252,242))

        # Parcheesi Title
        title = Text(Point(250,640),"PARCHEESI")
        title.setSize(30)
        title.setStyle("bold")
        title.draw(self.win)

        # Board Rect
        rec = Rectangle(Point(0,0),Point(500,500))
        rec.draw(self.win)

        # Dado Buttom
        buttom_dado = Rectangle(Point(440,-80),Point(580,-20))
        buttom_dado.draw(self.win)
        text_dado = Text(Point(510,-50),'TIRAR DADOS')
        text_dado.draw(self.win)

        # Color rectangulos
        self.recMedio.setFill(color_rgb(205,108,107))
        self.rec1.setFill(color_rgb(255,213,0))
        self.rec2.setFill(color_rgb(0,80,157))
        self.rec3.setFill(color_rgb(239,35,60))
        self.rec4.setFill(color_rgb(122,199,79))

        self.cir1.setFill(color_rgb(255,252,242))
        self.cir2.setFill(color_rgb(255,252,242))
        self.cir3.setFill(color_rgb(255,252,242))
        self.cir4.setFill(color_rgb(255,252,242))

        self.recA11.setFill(color_rgb(144,224,239))
        self.recA21.setFill(color_rgb(230,57,70))
        self.recA31.setFill(color_rgb(230,57,70))
        self.recA41.setFill(color_rgb(230,57,70))
        self.recA50.setFill(color_rgb(144,224,239))
        self.recA51.setFill(color_rgb(230,57,70))
        self.recA52.setFill(color_rgb(144,224,239))
        self.recA61.setFill(color_rgb(230,57,70))
        self.recA71.setFill(color_rgb(230,57,70))
        self.recA81.setFill(color_rgb(230,57,70))

        self.recB11.setFill(color_rgb(144,224,239))
        self.recB21.setFill(color_rgb(230,57,70))
        self.recB31.setFill(color_rgb(230,57,70))
        self.recB41.setFill(color_rgb(230,57,70))
        self.recB50.setFill(color_rgb(144,224,239))
        self.recB51.setFill(color_rgb(230,57,70))
        self.recB52.setFill(color_rgb(144,224,239))
        self.recB61.setFill(color_rgb(230,57,70))
        self.recB71.setFill(color_rgb(230,57,70))
        self.recB81.setFill(color_rgb(230,57,70))

        self.recC11.setFill(color_rgb(230,57,70))
        self.recC21.setFill(color_rgb(230,57,70))
        self.recC31.setFill(color_rgb(230,57,70))
        self.recC40.setFill(color_rgb(144,224,239))
        self.recC41.setFill(color_rgb(230,57,70))
        self.recC42.setFill(color_rgb(144,224,239))
        self.recC51.setFill(color_rgb(230,57,70))
        self.recC61.setFill(color_rgb(230,57,70))
        self.recC71.setFill(color_rgb(230,57,70))
        self.recC81.setFill(color_rgb(144,224,239))

        self.recD11.setFill(color_rgb(230,57,70))
        self.recD21.setFill(color_rgb(230,57,70))
        self.recD31.setFill(color_rgb(230,57,70))
        self.recD40.setFill(color_rgb(144,224,239))
        self.recD41.setFill(color_rgb(230,57,70))
        self.recD42.setFill(color_rgb(144,224,239))
        self.recD51.setFill(color_rgb(230,57,70))
        self.recD61.setFill(color_rgb(230,57,70))
        self.recD71.setFill(color_rgb(230,57,70))
        self.recD81.setFill(color_rgb(144,224,239))


        # Draw
        self.rec1.draw(self.win)
        self.rec2.draw(self.win)
        self.rec3.draw(self.win)
        self.rec4.draw(self.win)
        
        self.recMedio.draw(self.win)

        self.cir1.draw(self.win)
        self.cir2.draw(self.win)
        self.cir3.draw(self.win)
        self.cir4.draw(self.win)
        
        
        for A in self.rectA:
            A.draw(self.win)

        for B in self.rectB:
            B.draw(self.win)

        for C in self.rectC:
            C.draw(self.win)

        for D in self.rectD:
            D.draw(self.win)
        
        
        


    def estado_juego(self):
        print("\n------------------------------------------------------------------")
        print("ESTADO DEL JUEGO \n")
        for x in range(4):
            print(self.jugadores[x] + ' Se encuentra en la posicion: ', self.posicion[x])

        print(self.board)
        print("------------------------------------------------------------------\n")



    def not_graphic(self):
        c = False
        texto_turno = Text(Point(200,-50),'')
        texto_output = Text(Point(250,550),'')
        texto_output.draw(self.win)
        texto_turno.draw(self.win)

        ganador = False
        while ganador == False:
            # input(self.jugadores[self.turno] + ' entre la letra t para tirar los dados.\n')
            # dado1 = randrange(1,7)
            # dado2 = randrange(1,7)

            texto_turno.setText(self.jugadores[self.turno] + ' haga click en el boton para tirar los dados.\n')
            print(self.jugadores[self.turno] + ' haga click en el boton para tirar los dados.\n')
            
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()

            while not 440 <= x <= 580 or not -80 <= y <= -20:
                # x < 440 and x > 580 and y < -80 and y > -20
                # not 440 <= x <= 580 and not -80 <= y <= -20
                print(self.jugadores[self.turno] + ' haga click en el boton para tirar los dados.\n')
                click = self.win.getMouse()
                x = click.getX()
                y = click.getY()
            
            dado1 = randrange(1,7)
            dado2 = randrange(1,7)
            
            if self.posicion[self.turno] == 0:
                if dado1 == 5 or dado2 == 5 or dado1 + dado2 == 5:
                    self.posicion[self.turno] = 1
                    self.board[self.starting_point[self.turno]] = self.board[self.starting_point[self.turno]] + 1
                    texto_output.setText('\nSus resultados fueron ' + str(dado1) + ' y ' + str(dado2) +' asi que usted logro entrar al tablero')
                    print('\nSus resultados fueron ', str(dado1), ' y ', str(dado2),' asi que usted logro entrar al tablero')
                else:
                    texto_output.setText('\nSus resultados fueron ' + str(dado1) + ' y ' +  str(dado2) + ' lo que significa que usted no logro conseguir un 5 \n en ninguno de los dos dados y la suma de ambos tampoco resultaba ser 5. \n Usted se mantuvo en la posicion 0')
                    print('\nSus resultados fueron ', str(dado1), ' y ', str(dado2), ' lo que significa que usted no logro conseguir un 5 \n en ninguno de los dos dados y la suma de ambos tampoco resultaba ser 5. \n Usted se mantuvo en la posicion 0')
            else:
                suma_dados = dado1 + dado2
                self.posicion[self.turno] = self.posicion[self.turno] + suma_dados
                self.board[self.posicion_actual[self.turno]] = self.board[self.posicion_actual[self.turno]] - 1
                self.posicion_actual[self.turno] = self.posicion_actual[self.turno] + suma_dados
                if self.posicion_actual[self.turno] >= 68:
                    self.posicion_actual[self.turno] = 0
                self.board[self.posicion_actual[self.turno]] = self.board[self.posicion_actual[self.turno]] + 1
                texto_output.setText("\nSus resultados fueron " +  str(dado1) +  " y " +  str(dado2) +  " lo que significa que usted se movio " +  str(suma_dados) +  "veces.")
                print("\nSus resultados fueron " +  str(dado1) +  " y " +  str(dado2) +  " lo que significa que usted se movio " +  str(suma_dados) +  "veces.")

            print('\n',self.posicion_actual[self.turno],'\n')

            
            self.estado_juego()
            if self.posicion[self.turno] >= 72:
                ganador = True
            elif self.turno == 3:
                self.turno = 0
            else:
                self.turno = self.turno + 1

        texto_output.setText('')
        texto_ganador = Text(Point(250,550),"FELICIDADES " + self.jugadores[self.turno] + " USTED HA GANADO")
        texto_ganador.setStyle('bold')
        texto_ganador.setSize(15)
        texto_ganador.draw(self.win)
        print("FELICIDADES " + self.jugadores[self.turno] + " USTED HA GANADO")

    def movimientos_graficos(self):
        board_points =[Point()]
        pass

    def tirar_dado (self,x,y):
        

        if 440 <= x <= 580 and -80 <= y <= -20:
            dado1 = randrange(1,7)
            dado2 = randrange(1,7)
            return dado1,dado2

            


def main():
    win = GraphWin('Game', 600,700)
    game = Parcheesi(win)
    game.draw_game()
    game.not_graphic()

    win.getMouse()

main()