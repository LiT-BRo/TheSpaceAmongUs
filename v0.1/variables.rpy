init:
    define a = Character("Astronaut Neil", image="neil_astro", color="#009900")
    define n = Character("Neil", image="neil", color="#990000")

    image side neil = im.Scale("images/characters/neil normal.png", 211, 210, xoffset=190, yoffset=-56)
    image side neil_astro = im.Scale("images/characters/neil astro.png", 235, 235, xoffset=180, yoffset=-50)

    image intro = "gui/intro.png"
    image bg outro = Movie(play="gui/outro.webm")

    image bg space = Movie(play="bg space.webm")
    image bg mercury = Movie(play="planets/bg mercury.webm")
    image bg venus = Movie(play="planets/bg venus.webm")
    image bg earth = Movie(play="planets/bg earth.webm")
    image bg mars = Movie(play="planets/bg mars.webm")
    image bg jupiter = Movie(play="planets/bg jupiter.webm")
    image bg saturn = Movie(play="planets/bg saturn.webm")
    image bg uranus = Movie(play="planets/bg uranus.webm")
    image bg neptune = Movie(play="planets/bg neptune.webm")
    image bg sun = Movie(play="planets/bg sun.webm")
    image bg solar = Movie(play="planets/bg solar.webm")
    image bg milky = Movie(play="planets/bg milky.webm")

label variables:
    define seen_space            = False
    define seen_solar            = False
    define seen_mercury          = False
    define seen_venus            = False
    define seen_earth            = False
    define seen_mars             = False
    define seen_jupiter          = False
    define seen_saturn           = False
    define seen_uranus           = False
    define seen_neptune          = False
    define seen_sun              = False
    define seen_milkyway         = False
    define seen_total            = 0 #12

    define seen_mercury_more     = False
    define seen_venus_more       = False
    define seen_earth_more       = False
    define seen_mars_more        = False
    define seen_jupiter_more     = False
    define seen_saturn_more      = False
    define seen_uranus_more      = False
    define seen_neptune_more     = False
    define seen_sun_more         = False
    define seen_milkyway_more    = False
    define seen_solar_more       = False
