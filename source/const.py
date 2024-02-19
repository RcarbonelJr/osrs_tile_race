# Board
TILE_SCALE = .5

TILE_WIDTH = int(128 * TILE_SCALE)
TILE_HEIGHT = int(128 * TILE_SCALE)

ROW_COUNT = 15
COULMN_COUNT = 15

BOARD_WIDTH = TILE_WIDTH * ROW_COUNT
BOARD_HEIGHT = TILE_HEIGHT * COULMN_COUNT

# Side panel
SIDE_PANEL_WIDTH = 350
SIDE_PANEL_HEIGHT = 960

# Window
WINDOW_WIDTH = int(BOARD_WIDTH + SIDE_PANEL_WIDTH)
WINDOW_HEIGHT = int(BOARD_HEIGHT)

WINDOW_TITLE = "Old School Runescape: Tile Race"