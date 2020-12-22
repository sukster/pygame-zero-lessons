# Sirka a vyska hraciho okna
WIDTH = 800
HEIGHT = 600

# Obrazek mimozemstana
alien = Actor('alien')

# Pozice mimozemstana v okne na ose x a y
alien.x = 400
alien.y = 300

# Co se ma zmenit kdyz hrac stiskne klavesu
def update():
    if (keyboard.up):
        alien.y = alien.y - 1
    if (keyboard.down):
        alien.y = alien.y + 1
    if (keyboard.left):
        alien.x = alien.x - 1
    if (keyboard.right):
        alien.x = alien.x + 1

# Vykresli znovu mimozemstana se zmenami
def draw():
    screen.clear()
    alien.draw()