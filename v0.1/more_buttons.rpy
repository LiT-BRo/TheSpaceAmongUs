screen SpaceBack(): # Back button to bg space
    imagebutton:
        xalign 1
        yalign 1
        xoffset 1750
        yoffset 50
        auto "gui/buttons/back_%s.png"
        action Jump("start")

screen SolarBack(): # Back button to bg space
    imagebutton:
        xalign 1
        yalign 1
        xoffset 1750
        yoffset 50
        auto "gui/buttons/back_%s.png"
        action Jump("solar_pressed")

screen solar_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("solar_more")

screen mercury_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("mercury_more")

screen venus_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("venus_more")

screen earth_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("earth_more")

screen mars_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("mars_more")

screen jupiter_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("jupiter_more")

screen saturn_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("saturn_more")

screen uranus_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("uranus_more")

screen neptune_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("neptune_more")

screen sun_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("sun_more")

screen milkyway_button:
    imagebutton:
        xalign 1.0
        yalign 0.7
        xoffset -50
        yoffset -50
        auto "gui/buttons/more_%s.png"
        action Jump("milkyway_more")

# # # # This ends the game.

screen Finish():
    imagebutton:
        xalign 0.0
        yalign 1.0
        xoffset 10
        yoffset -10
        auto "gui/buttons/finish_%s.png"
        action Jump("complete")

screen Endscreen():
    imagebutton:
        xalign 0.0
        yalign 1.0
        xoffset 10
        yoffset -10
        auto "gui/buttons/quit_%s.png"
        action Jump("endscreen")

screen outro:
    add Movie(play="outro.mp4")

screen invis_return:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "gui/blank.png"
        action Return()
