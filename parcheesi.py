from graphics import *
from random import *

class Parcheesi:
    def __init__(self,win):
        """
        Se inicializan variables o objetos importantes que se estara utilizando en las diferentes funciones de la clase
        """

        self.win = win
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
        self.b69  = 0
        self.b70  = 0
        self.b71  = 0
        self.b72  = 0
        self.b73  = 0
        self.b74  = 0
        self.b75  = 0
        self.b76  = 0
        self.b77  = 0
        self.b78  = 0
        self.b79  = 0
        self.b80  = 0
        self.b81  = 0
        self.b82  = 0
        self.b83  = 0
        self.b84  = 0
        self.b85  = 0
        self.b86  = 0
        self.b87  = 0
        self.b88  = 0
        self.b89  = 0
        self.b90  = 0
        self.b91  = 0
        self.b92  = 0
        self.b93  = 0
        self.b94  = 0
        self.b95  = 0
        self.b96  = 0
        self.b97  = 0


        self.board = [self.b01,self.b02,self.b03,self.b04,self.b05,self.b06,self.b07,self.b08,self.b09,self.b10,self.b11,self.b12,self.b13,self.b14,self.b15,
        self.b16,self.b17,self.b18,self.b19,self.b20,self.b21,self.b22,self.b23,self.b24,self.b25,self.b26,self.b27,self.b28,self.b29,self.b30,self.b31,self.b32,
        self.b33,self.b34,self.b35,self.b36,self.b37,self.b38,self.b39,self.b40,self.b41,self.b42,self.b43,self.b44,self.b45,self.b46,self.b47,self.b48,self.b49,
        self.b50,self.b51,self.b52,self.b53,self.b54,self.b55,self.b56,self.b57,self.b58,self.b59,self.b60,self.b61,self.b62,self.b63,self.b64,self.b65,self.b66,self.b67,self.b68,
        self.b69,self.b70,self.b71,self.b72,self.b73,self.b74,self.b75,self.b76,self.b77,self.b78,self.b79,self.b80,self.b81,self.b82,self.b83,self.b84,self.b85,self.b86,
        self.b87,self.b88,self.b89,self.b90,self.b91,self.b92,self.b93,self.b94,self.b95,self.b96,self.b97]
        # Posicion cuando consiguen un 5 para salir
        self.starting_point = [0,51,34,17]
        self.posicion_actual = [0,51,34,17]
        # Se contabiliza cuantas veces se ha movido una pieza
        self.movidas1 = 0
        self.movidas2 = 0
        self.movidas3 = 0
        self.movidas4 = 0
        self.posicion = [self.movidas1,self.movidas2,self.movidas3,self.movidas4]
        # Numero de turno y su nombre
        self.turno = 0
        self.jugadores = ["Jugador #1", "Jugador #2", "Jugador #3", "Jugador #4"]
        # Movimentos de jugador 
        self.ubicacion = [Point(312.5,90),Point(90,187.5),Point(187.5,410),Point(410,312.5)]
        self.cir_player1 = Circle(self.ubicacion[0],5)
        self.cir_player2 = Circle(self.ubicacion[1],5)
        self.cir_player3 = Circle(self.ubicacion[2],5)
        self.cir_player4 = Circle(self.ubicacion[3],5)

        self.piezas = [self.cir_player1,self.cir_player2,self.cir_player3,self.cir_player4]

        self.conteo = [0,0,0,0]


        



    def draw_game(self):
        """
        Funcion que se encarga de dibujar la ventana grafica que se va a utilizar para jugar Parcheesi
        """
        self.win.setCoords(-100,-100,600,700)
        self.win.setBackground(color_rgb(255,252,242))

        # Parcheesi Title
        title = Text(Point(250,640),"PARCHEESI")
        title.setSize(30)
        title.setStyle("bold")
        title.draw(self.win)

        # Nombre de los jugadores
        p1 = Text(Point(415,90),"JUGADOR #1")
        p2 = Text(Point(90,90),"JUGADOR #2")
        p3 = Text(Point(90,415),"JUGADOR #3")
        p4 = Text(Point(415,415),"JUGADOR #4")
        pl = [p1,p2,p3,p4]
        

        # Board Rect
        rec = Rectangle(Point(0,0),Point(500,500))
        rec.draw(self.win)

        # Dado Buttom
        buttom_dado = Rectangle(Point(440,-80),Point(580,-20))
        buttom_dado.setFill(color_rgb(7,160,195))
        buttom_dado.draw(self.win)
        text_dado = Text(Point(510,-50),'TIRAR DADOS')
        text_dado.setStyle('bold')
        text_dado.setFill('white')
        text_dado.draw(self.win)

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

        rectA = [recA10,recA11,recA12,recA20,recA21,recA22,recA30,recA31,recA32,recA40,recA41,recA42,recA50,recA51,recA52,recA60,recA61,recA62,recA70,recA71,recA72,recA80,recA81,recA82]
        rectB = [recB10,recB11,recB12,recB20,recB21,recB22,recB30,recB31,recB32,recB40,recB41,recB42,recB50,recB51,recB52,recB60,recB61,recB62,recB70,recB71,recB72,recB80,recB81,recB82]
        rectC = [recC10,recC11,recC12,recC20,recC21,recC22,recC30,recC31,recC32,recC40,recC41,recC42,recC50,recC51,recC52,recC60,recC61,recC62,recC70,recC71,recC72,recC80,recC81,recC82]
        rectD = [recD10,recD11,recD12,recD20,recD21,recD22,recD30,recD31,recD32,recD40,recD41,recD42,recD50,recD51,recD52,recD60,recD61,recD62,recD70,recD71,recD72,recD80,recD81,recD82]

        # Color rectangulos
        recMedio.setFill(color_rgb(205,108,107))
        rec1.setFill(color_rgb(255,213,0)) # Player 2
        rec2.setFill(color_rgb(0,80,157))
        rec3.setFill(color_rgb(239,35,60))
        rec4.setFill(color_rgb(122,199,79)) # Player 1

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

        self.color_player = [color_rgb(122,199,79),color_rgb(255,213,0),color_rgb(0,80,157),color_rgb(239,35,60)]
        self.cir_player1.setFill(self.color_player[0])
        self.cir_player2.setFill(self.color_player[1])
        self.cir_player3.setFill(self.color_player[2])
        self.cir_player4.setFill(self.color_player[3])

        # Draw
        rec1.draw(self.win)
        rec2.draw(self.win)
        rec3.draw(self.win)
        rec4.draw(self.win)
        
        recMedio.draw(self.win)

        cir1.draw(self.win)
        cir2.draw(self.win)
        cir3.draw(self.win)
        cir4.draw(self.win)
        
        
        for A in rectA:
            A.draw(self.win)

        for B in rectB:
            B.draw(self.win)

        for C in rectC:
            C.draw(self.win)

        for D in rectD:
            D.draw(self.win)

        for j in pl:
            j.setStyle('bold')
            j.setSize(12)
            j.draw(self.win)
        
        


    def estado_juego(self):
        """
        Funcion que se encarga de imprimir el estado del juego, indicando en que posicion se encuentra cada jugador
        """
        print("\n------------------------------------------------------------------")
        print("ESTADO DEL JUEGO \n")
        for x in range(4):
            print(self.jugadores[x] + ' Se encuentra en la posicion: ', self.posicion[x])
            print('Conteo: ', self.conteo)

        print(self.board)
        print("------------------------------------------------------------------\n")



    def the_game(self):
        """
        Funcion que se encarga de ejecutar el juego de Parcheesi
        """
        
        texto_turno = Text(Point(200,-50),'')
        texto_output = Text(Point(250,570),'')
        texto_output.draw(self.win)
        texto_turno.draw(self.win)

        ganador = False
        while ganador == False:
            texto_turno.setText(self.jugadores[self.turno] + ' haga click en el boton para tirar los dados.\n')
            print(self.jugadores[self.turno] + ' haga click en el boton para tirar los dados.\n')
            
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()

            while not 440 <= x <= 580 or not -80 <= y <= -20:
                # print(self.jugadores[self.turno] + ' haga click en el boton para tirar los dados.\n')
                click = self.win.getMouse()
                x = click.getX()
                y = click.getY()
            
            dado1 = randrange(1,7)
            dado2 = randrange(1,7)
            
            
            if self.posicion[self.turno] == 0: # Si se encuentra en la posicion 0
                if dado1 == 5 or dado2 == 5 or dado1 + dado2 == 5: # Si consigue un 5 puede ir a la posicion 1 
                    self.posicion[self.turno] = 1
                    
                    self.board[self.starting_point[self.turno]] = self.board[self.starting_point[self.turno]] + 1
                    self.movimientos_graficos()
                    texto_output.setText("\n" + self.jugadores[self.turno] +'\nSus resultados fueron ' + str(dado1) + ' y ' + str(dado2) +' asi que usted logro entrar al tablero')

                else: # Si no consigue un 5 se queda en la posicion 0
                    texto_output.setText("\n" + self.jugadores[self.turno] +'\nSus resultados fueron ' + str(dado1) + ' y ' +  str(dado2) + ' lo que significa que usted no logro conseguir un 5 \n en ninguno de los dos dados y la suma de ambos tampoco resultaba ser 5. \n Usted se mantuvo en la posicion 0')
            else: # Si ya no esta en la posicion 0 
                suma_dados = dado1 + dado2
                # Se mueve la pieza en el board
                self.board[self.posicion_actual[self.turno]] = self.board[self.posicion_actual[self.turno]] - 1

                for suma in range(suma_dados):
                    self.posicion_actual[self.turno] = self.posicion_actual[self.turno] + 1
                    self.posicion[self.turno] = self.posicion[self.turno] + 1
                    if self.posicion_actual[self.turno] == 68 and self.posicion[self.turno] < 63:
                        self.posicion_actual[self.turno] = 0
                        self.movimientos_graficos()
                    elif self.posicion[self.turno] == 65:
                        if self.turno == 0:
                            self.posicion_actual[self.turno] = 69
                        elif self.turno == 1:
                            self.posicion_actual[self.turno] = 90
                        elif self.turno == 2:
                            self.posicion_actual[self.turno] = 83
                        elif self.turno == 3:
                            self.posicion_actual[self.turno] = 76
                        self.for_the_win()
                    elif self.posicion_actual[self.turno] >= 69:
                        self.for_the_win()
                    else:
                        self.movimientos_graficos()

                    if self.posicion[self.turno] >= 72:
                        break
                try:
                    self.board[self.posicion_actual[self.turno]] = self.board[self.posicion_actual[self.turno]] + 1
                except IndexError:
                    print("no se pudo anadir")


                texto_output.setText("\n" + self.jugadores[self.turno] + "\nSus resultados fueron " +  str(dado1) +  " y " +  str(dado2) +  " lo que significa que usted se movio " +  str(suma_dados) +  " veces.")

            print('\n Posicion Actual Value: ',self.posicion_actual[self.turno],'\n')

            
            
            # Si hay ganador, el juego se acaba. Si no lo hay cambia el turno.
            if self.posicion[self.turno] >= 72:
                self.conteo[self.turno] = self.conteo[self.turno] + 1
                self.posicion_actual[self.turno] = self.starting_point[self.turno]
                self.posicion[self.turno] = 0
                # self.piezas[self.turno].undraw()
                self.piezas[self.turno] = Circle(self.ubicacion[self.turno],5)
                self.piezas[self.turno].setFill(self.color_player[self.turno])
                # self.piezas[self.turno].draw(self.win)
                if self.conteo[self.turno] == 4:
                    ganador = True
                    print('hoal')
                else:
                    if self.turno == 3:
                        self.turno = 0
                    else:
                        self.turno = self.turno + 1
            elif self.turno == 3:
                self.turno = 0
            else:
                self.turno = self.turno + 1
            # Se imprime un estado del juego
            self.estado_juego()

        texto_output.setText('')
        texto_ganador = Text(Point(250,550),"FELICIDADES " + self.jugadores[self.turno] + " USTED HA GANADO")
        texto_ganador.setStyle('bold')
        texto_ganador.setSize(15)
        texto_ganador.draw(self.win)
        print("FELICIDADES " + self.jugadores[self.turno] + " USTED HA GANADO")

    def movimientos_graficos(self):
        """
        Funcion que se encarga de mover las piezas alrededor del board
        """
        if self.posicion[self.turno] == 1:
            if self.board[self.starting_point[self.turno]] == 0:
                
                self.piezas[self.turno].draw(self.win)
            else:
                
                self.piezas[self.turno].draw(self.win)
        else:
            if self.posicion_actual[self.turno] == 0:
                self.piezas[self.turno].undraw()
                self.piezas[self.turno] = Circle(Point(312.5,90),5)
                self.piezas[self.turno].setFill(self.color_player[self.turno])
                self.piezas[self.turno].draw(self.win)
            elif 1 <= self.posicion_actual[self.turno] <=3:
                self.piezas[self.turno].move(0,20)
            elif self.posicion_actual[self.turno] == 4: # Cambio de lado
                self.piezas[self.turno].move(37.5,40)
            elif 5 <= self.posicion_actual[self.turno] < 12:
                self.piezas[self.turno].move(20,0)
            elif 12 <= self.posicion_actual[self.turno] <=13:
                self.piezas[self.turno].move(0,61)
            elif 14 <= self.posicion_actual[self.turno] <21:
                self.piezas[self.turno].move(-20,0)
            elif self.posicion_actual[self.turno] == 21: # Cambio de lado
                self.piezas[self.turno].move(-40,39)
            elif 22 <= self.posicion_actual[self.turno] <29:
                self.piezas[self.turno].move(0,20)
            elif 29 <= self.posicion_actual[self.turno] <=30:
                self.piezas[self.turno].move(-61,0)
            elif 31 <= self.posicion_actual[self.turno] <38:
                self.piezas[self.turno].move(0,-20)
            elif self.posicion_actual[self.turno] == 38: # Cambio de lado
                self.piezas[self.turno].move(-38,-39)
            elif 39 <= self.posicion_actual[self.turno] <46:
                self.piezas[self.turno].move(-20,0)
            elif 46 <= self.posicion_actual[self.turno] <=47:
                self.piezas[self.turno].move(0,-61)
            elif 48 <= self.posicion_actual[self.turno] <55:
                self.piezas[self.turno].move(20,0)
            elif self.posicion_actual[self.turno] == 55: # Cambio de lado
                self.piezas[self.turno].move(39,-39)
            elif 56 <= self.posicion_actual[self.turno] <63:
                self.piezas[self.turno].move(0,-20)
            elif 63 <= self.posicion_actual[self.turno] <=64:
                self.piezas[self.turno].move(61,0)
            elif 65 <= self.posicion_actual[self.turno] <67:
                self.piezas[self.turno].move(0,20)
            

    def for_the_win(self):
        """
        Funcion que se encarga de mover las piezas cuando ya completaron la vuelta y estan en la recta final
        """

        if self.turno == 0:
            if 69 <= self.posicion_actual[self.turno] <76: # For the win 1
                self.piezas[self.turno].move(0,20)
            elif 76 <= self.posicion_actual[self.turno]:
                if self.conteo[self.turno] == 0:
                    self.piezas[self.turno].move(20,80)
                elif self.conteo[self.turno] == 1:
                    self.piezas[self.turno].move(40,80)
                elif self.conteo[self.turno] == 2:
                    self.piezas[self.turno].move(40,60)
                else:
                    self.piezas[self.turno].move(20,60)
        elif self.turno == 1:
            if 90 <= self.posicion_actual[self.turno] <97: # For the win 2
                self.piezas[self.turno].move(20,0)
            elif 97 <= self.posicion_actual[self.turno]:
                if self.conteo[self.turno] == 0:
                    self.piezas[self.turno].move(80,-20)
                elif self.conteo[self.turno] == 1:
                    self.piezas[self.turno].move(80,-40)
                elif self.conteo[self.turno] == 2:
                    self.piezas[self.turno].move(60,-40)
                else:
                    self.piezas[self.turno].move(60,-20)
        elif self.turno == 2:
            if 83 == self.posicion_actual[self.turno]: # For the win 3
                self.piezas[self.turno].move(0,-20)
            elif 84 <= self.posicion_actual[self.turno] <90: # For the win 3
                self.piezas[self.turno].move(0,-20)
            elif 90 <= self.posicion_actual[self.turno]:
                if self.conteo[self.turno] == 0:
                    self.piezas[self.turno].move(-20,-80)
                elif self.conteo[self.turno] == 1:
                    self.piezas[self.turno].move(-40,-80)
                elif self.conteo[self.turno] == 2:
                    self.piezas[self.turno].move(-40,-60)
                else:
                    self.piezas[self.turno].move(-20,-60)
        elif self.turno == 3:
            if 76 <= self.posicion_actual[self.turno] <83: # For the win 4
                self.piezas[self.turno].move(-20,0)
            elif 83 <= self.posicion_actual[self.turno]:
                if self.conteo[self.turno] == 0:
                    self.piezas[self.turno].move(-80,20)
                elif self.conteo[self.turno] == 1:
                    self.piezas[self.turno].move(-80,40)
                elif self.conteo[self.turno] == 2:
                    self.piezas[self.turno].move(-60,40)
                else:
                    self.piezas[self.turno].move(-60,20)
                
                    

            


def main():
    win = GraphWin('Parcheesi: The Game', 600,700)
    game = Parcheesi(win)
    game.draw_game()
    game.the_game()

    win.getMouse()

main()
