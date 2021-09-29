screen SolarUI(): #Buttons

    imagebutton: # SOLAR BUTTON
        xalign 0.3
        yalign 0.0
        xoffset 0
        yoffset 0
        auto "elements/solar_%s.png"
        action Jump("solar_pressed")

screen SolarSystem(): #Solar Screen

    imagebutton: #Mercury
        xpos 477
        ypos 661
        auto "elements/buttons/mercury_%s.png"
        action Jump("mercury_pressed")

    imagebutton: #Venus
        xpos 641
        ypos 603
        auto "elements/buttons/venus_%s.png"
        action Jump("venus_pressed")

    imagebutton: #Earth
        xpos 759
        ypos 537
        auto "elements/buttons/earth_%s.png"
        action Jump("earth_pressed")

    imagebutton: #Mars
        xpos 933
        ypos 530
        auto "elements/buttons/mars_%s.png"
        action Jump("mars_pressed")

    imagebutton: #Jupiter
        xpos 1030
        ypos 410
        auto "elements/buttons/jupiter_%s.png"
        action Jump("jupiter_pressed")

    imagebutton: #Saturn
        xpos 1341
        ypos 459
        auto "elements/buttons/saturn_%s.png"
        action Jump("saturn_pressed")

    imagebutton: #Uranus
        xpos 1566
        ypos 353
        auto "elements/buttons/uranus_%s.png"
        action Jump("uranus_pressed")

    imagebutton: #Neptune
        xpos 1681
        ypos 435
        auto "elements/buttons/neptune_%s.png"
        action Jump("neptune_pressed")

    imagebutton: #Sun
        xpos -7
        ypos 0
        auto "elements/buttons/sun_%s.png"
        action Jump("sun_pressed")
