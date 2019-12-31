import arcade

QUANT_LINHAS = 3
QUANT_COLUNAS = 3

ALTURA_BLOCO = 30
LARGURA_BLOCO = 30

ESPESSURA_MARGEM = 5

LARGURA_TELA = (LARGURA_BLOCO + ESPESSURA_MARGEM) * QUANT_COLUNAS + ESPESSURA_MARGEM
ALTURA_TELA = (ALTURA_BLOCO + ESPESSURA_MARGEM) * QUANT_LINHAS + ESPESSURA_MARGEM
TITULO_TELA = "2048 by Matheus Muriel"


class Game(arcade.Window):

  def __init__(self, altura, largura, titulo):
    super().__init__(largura, altura, titulo)
    self.grid = []

    for i in range(QUANT_LINHAS):
      self.grid.append([])
      for j in range(QUANT_COLUNAS):
        self.grid[i].append(0)

    arcade.set_background_color(arcade.color.BLACK)

  def on_draw(self):
    arcade.start_render()

    for i in range(QUANT_LINHAS):
      for j in range(QUANT_COLUNAS):
        if self.grid[i][j] == 1:
          color = arcade.color.GREEN
        else:
          color = arcade.color.WHITE

        x = (ESPESSURA_MARGEM + LARGURA_BLOCO) * j + ESPESSURA_MARGEM + LARGURA_BLOCO // 2
        y = (ESPESSURA_MARGEM + ALTURA_BLOCO) * i + ESPESSURA_MARGEM + ALTURA_BLOCO // 2

        arcade.draw_rectangle_filled(x, y, LARGURA_BLOCO, ALTURA_BLOCO, color)

  def on_mouse_press(self, x, y, button, modifiers):
    column = int(x // (LARGURA_BLOCO + ESPESSURA_MARGEM))
    row = int(y // (ALTURA_BLOCO + ESPESSURA_MARGEM))

    if row < QUANT_LINHAS and column < QUANT_COLUNAS:
      if self.grid[row][column] == 0:
        self.grid[row][column] = 1
      else:
        self.grid[row][column] = 0

def main():
  Game(ALTURA_TELA, LARGURA_TELA, TITULO_TELA)
  arcade.run()

if __name__ == "__main__":
  main()