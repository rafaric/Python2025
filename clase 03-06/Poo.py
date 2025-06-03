class Personaje:
  def __init__(self, nombre, armadura, vida, fuerza):
    self.nombre = nombre
    self.armadura = armadura
    self.vida = vida
    self.fuerza = fuerza
  
  def atributos(self):
    print(self.nombre,":", sep="")
    print("-Fuerza:", self.fuerza)
    print("-Armadura:", self.armadura)
    print("-Vida:", self.vida)

  def esta_vivo(self):
    return self.vida > 0 ## True o False

  def morir(self):
    self.vida = 0
    print(self.nombre, "ha muerto.")

  def daño(self, enemigo):
    return self.fuerza - enemigo.armadura

  def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
    if enemigo.esta_vivo():
      print("Vida de", enemigo.nombre, "es", enemigo.vida)
    else:
      enemigo.morir()


class Guerrero(Personaje):
  def __init__(self, nombre, armadura, vida, fuerza, espada):
    super().__init__(nombre, armadura, vida, fuerza)
    self.espada = espada
  
  def atributos(self):
    super().atributos()
    print("-Espada:", self.espada)
  
  def daño(self, enemigo):
    return self.fuerza*self.espada - enemigo.armadura

class Mago(Personaje):
  def __init__(self, nombre, armadura, vida, fuerza, varita):
    super().__init__(nombre, armadura, vida, fuerza)
    self.varita = varita

  def atributos(self):
    super().atributos()
    print("-Varita:", self.varita)
  
  def daño(self, enemigo):
    return self.fuerza*self.varita - enemigo.armadura
  
  def atacar(self, enemigo):
    super().atacar(enemigo)
    self.vida = self.vida + 1




def combate(jugador1, jugador2):
  turno = 0
  while jugador1.esta_vivo() and jugador2.esta_vivo():
    print("\nTurno", turno)
    print(">>> Acción de ", jugador1.nombre,":",sep="")
    jugador1.atacar(jugador2)
    print(">>> Acción de ", jugador2.nombre,":",sep="")
    jugador2.atacar(jugador1)
    turno = turno + 1
  if jugador1.esta_vivo():
    print("\nHa ganado", jugador1.nombre, " Felicidades!")
  elif jugador2.esta_vivo():
    print("\nHa ganado", jugador2.nombre, " Felicidades!")
  else:
    print("\nEmpate")


nombre_personaje = input("Ingrese el nombre de su personaje")
Warrior = Guerrero(nombre_personaje, 100, 100, 100, 3)

MagoOscuro = Mago("Mago Oscuro", 300, 100, 40, 5)


Warrior.atributos()
MagoOscuro.atributos()

combate(Warrior, MagoOscuro)

