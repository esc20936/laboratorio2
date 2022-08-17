from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend

width = 960
height = 540

rend = Renderer(width, height)

rend.dirLight = V3(1,0,0)

# rend.active_texture = Texture("marioT.bmp")
rend.active_shader = textureBlend

rend.glLoadModel("models/sphere.obj",
                 translate = V3(0, 0, 0),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(0,0,0))


rend.glFinish("output.bmp")

