import config.Config as Cfg
import config.core.ConfigLoader as CfgLdr
from varname import nameof

def register_snake_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("Game-Snake")\
        .with_bool(nameof(Cfg.SNAKE_ENABLED))\
        .has_title("Snake enabled")\
        .has_description("If snake is selectable and playable.")\
        .and_then()\
        .with_float(nameof(Cfg.SNAKE_SPEED))\
        .has_min(0)\
        .has_max(1)\
        .has_title("Speed")\
        .has_description("Delay in ms between frames in snake.")\
        .and_then()\
        .end_category()

def register_pong_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("Game-Pong")\
        .with_bool(nameof(Cfg.PONG_ENABLED))\
        .has_title("Pong enabled")\
        .has_description("If pong is selectable and playable.")\
        .and_then()\
        .with_float(nameof(Cfg.PONG_SPEED))\
        .has_min(0)\
        .has_max(1)\
        .has_title("Speed")\
        .has_description("Delay in ms between frames in pong.")\
        .and_then()\
        .end_category()

def register_tetris_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("Game-Tetris")\
        .with_bool(nameof(Cfg.TETRIS_ENABLED))\
        .has_title("Tetris enabled")\
        .has_description("If tetris is selectable and playable.")\
        .and_then()\
        \
        .with_float(nameof(Cfg.TETRIS_SPEED))\
        .has_min(0)\
        .has_max(1)\
        .has_title("Speed")\
        .has_description("Delay in ms between frames in tetris.")\
        .and_then()\
        .end_category()

def register_minesweeper_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("Game-Minesweeper")\
        .with_bool(nameof(Cfg.MINESWEEPER_ENABLED))\
        .has_title("Minesweeper enabled")\
        .has_description("If minesweeper is selectable and playable.")\
        .and_then()\
        .end_category()

def register_draw_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("Animation-Draw")\
        .with_bool(nameof(Cfg.DRAW_ENABLED))\
        .has_title("Draw enabled")\
        .has_description("If the draw-animation is enabled")\
        .and_then()\
        .end_category()

def register_rgb_spiral_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("Animation-RGB-Spiral")\
        .with_bool(nameof(Cfg.RGB_SPIRAL_ENABLED))\
        .has_title("RGB-Spiral enabled")\
        .has_description("If the rgb-spiral-animation is enabled")\
        .and_then()\
        .end_category()

def register_settings_loader(loader: CfgLdr.ConfigLoaderBuilder):
    return loader.in_category("General-Settings")\
        \
        .with_int(nameof(Cfg.LED_PIXEL_SCALE))\
        .has_min(5)\
        .has_max(100)\
        .has_title("PyGame-Pixel-Scale")\
        .has_description("How many Screen-Pixel one Game-Pixel uses")\
        .and_then()\
        \
        .with_int_preset(nameof(Cfg.ESP_BAUD), [115200, 9600])\
        .has_title("Esp-Baud")\
        .has_description("Baud-rate that is used to communicate with the Esp32")\
        .and_then()\
        \
        .with_int(nameof(Cfg.WALL_SIZE_X))\
        .has_min(1)\
        .has_max(10)\
        .has_title("Wall-Size (X)")\
        .has_description("Of how many cubes (on the x axis) does the wall consist?")\
        .and_then()\
        \
        .with_int(nameof(Cfg.WALL_SIZE_Y))\
        .has_min(1)\
        .has_max(10)\
        .has_title("Wall-Size (Y)")\
        .has_description("Of how many cubes (on the y axis) does the wall consist?")\
        .and_then()\
        \
        .with_bool(nameof(Cfg.IS_DEVELOPMENT_ENVIRONMENT))\
        .has_title("Is Dev-Environment?")\
        .has_description("Is the software running in development (True) or production (False) mode?")\
        .and_then()\
        \
        .with_bool(nameof(Cfg.USE_TEST_SCENE))\
        .has_title("Use test scene?")\
        .has_description("Shall the test-screen-scene be loaded instead of the normal start scene?")\
        .and_then()\
        \
        .with_bool(nameof(Cfg.USE_OLD_WS2812B_CONNECTION_TYPE))\
        .has_description("If the old ws2812b connection schema or the new one should be used.")\
        .has_title("Use old WS2812B-Schema?")\
        .and_then()\
        \
        .with_string_preset(nameof(Cfg.BOX_ORIENTATION), ["(X | Y)", "(-X | Y)", "(X | -Y)", "(-X | -Y)"])\
        .has_title("In which Orientation are all the Boxes?")\
        .has_description("Inside a box, which axes must be inverted to match to the normal orientation? (X | Y)")\
        .and_then()\
        \
        .with_bool(nameof(Cfg.BOX_HORIZONTAL)) \
        .has_description("Is the longer side of the boxes parallel to the ground?") \
        .has_title("Are boxes placed horizontal?") \
        .and_then()\
        \
        .end_category()

# Event: When the config-loaders are registered
def register_on_loader():
    loader = CfgLdr.ConfigLoaderBuilder()

    loader = register_settings_loader(loader)
    loader = register_snake_loader(loader)
    loader = register_pong_loader(loader)
    loader = register_tetris_loader(loader)
    loader = register_minesweeper_loader(loader)
    loader = register_rgb_spiral_loader(loader)
    loader = register_draw_loader(loader)

    return loader.build()
