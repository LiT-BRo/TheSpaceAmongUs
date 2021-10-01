init:
    define slowdiss = Dissolve(0.2)
    define diss = Dissolve(0.4)
    define slowflash = Fade(0.5,1.0,0.5, color="#fff")
    define flash = Fade(0.35,0.,0.35, color="#fff")

screen MilkyUI():
    imagebutton:
        xalign 0.7
        yalign 0.0
        xoffset 0
        yoffset 0
        auto "elements/galaxy_%s.png"
        hover_sound "gui/audio/mouse_hover.ogg"
        activate_sound "gui/audio/mouse_click.ogg"
        action Jump("milkyway_pressed")
