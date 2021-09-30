init:
    define slowdiss = Dissolve(0.8)
    define diss = Dissolve(0.4)
    pass

###########################
## SCRIPT #################
###########################

label start: #Scene 1 - Space
# Location Planning == Transtition will be like:
# Space -> Solar System -> Some Planets -> Solar System -> Space -> Milky Way -> Anywhere
    hide screen SolarUI
    hide screen SpaceBack
    hide screen SolarBack
    hide screen SolarSystem
    hide screen solar_button
    hide screen milkyway_button
    call variables from _call_variables

    if seen_space: # 2  # If been here dont show transition
        scene bg space
        show screen SolarUI
        show screen Endscreen() # Quit Button

    if not seen_milkyway and seen_space == True: # 2  #Following the Location Planning
        pause(1)
        show screen MilkyUI with slowdiss
        a "Now, see that galaxy at the top? Click on it and let's travel to The Milky Way!"
        call screen MilkyUI()

    if seen_total == 12: # Finish Button
        hide screen Endscreen
        show screen Finish()

    if seen_milkyway: # 3  #
        show screen MilkyUI
        a "So, what's on your mind? The Solar System or The Milky Way Galaxy..."
        call screen MilkyUI()

    if not seen_space: # 1
        scene bg space
        pause(3)
        a "Hey there, Welcome to the space!\n(To continue, click anywhere on the screen or press spacebar)"
        a "The name is Neil and I'll be your guide for the game. So, buckle up!"
        $ seen_total += 1
        $ seen_space = True
        show screen SolarUI() with slowdiss
        a "See that sun on the top. Click it and we shall travel to the Solar System at the speed of light."
        # hide screen SolarUI
    call screen SolarUI() #lock screen

label solar_pressed:
    hide screen Finish
    hide screen Endscreen
    hide screen solar_button
    hide screen SolarSystem
    hide screen SolarUI
    hide screen SolarBack
    hide screen mercury_button
    hide screen venus_button
    hide screen earth_button
    hide screen mars_button
    hide screen jupiter_button
    hide screen saturn_button
    hide screen uranus_button
    hide screen neptune_button
    hide screen sun_button
    call variables from _call_variables_1
    scene bg solar with slowdiss
    pause(2)

    if not seen_solar:
        a "Welcome to the Solar System! The massive system of the nine major planets revolving around the sun."
        $ seen_total += 1
        $ seen_solar = True
        show screen SolarSystem


    if not seen_solar_more:
        a "To know about the planets click on them and to know more about the solar system click the 'More Button'.\nTo hide my message press the spacebar."
        show screen solar_button with slowdiss

    show screen SolarSystem()
    call screen SpaceBack() with diss


label solar_more:
    hide screen SpaceBack
    hide screen solar_button
    hide screen SolarSystem
    call variables from _call_variables_2
    scene bg solar with slowdiss
    a "The term 'Solar' refers to 'of the Sun'. The Solar System is centered around the Sun, the shining ball in the sky."
    a "It includes the family of nine planets orbiting the Sun, as well as the moons of these planets, and smaller objects, such as comets, asteroids, and bits of space rock."
    a "The powerful pull of an invisible force called gravity of the sun stops these bodies from flying off into deepest space."
    $ seen_solar_more = True
    jump solar_pressed
    # call screen SolarBack() with diss

label mercury_pressed: # Mercury Animation with Buttons(More and Back)
    # hide screen SolarSystem
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_3
    scene bg mercury with slowdiss
    pause(2)

    if not seen_mercury:
        a "This is planet Mercury, it looks very much like our Earth's Moon. Mercury is also the fastest planet revolving around the sun, in our solar system."
        a "It's about the same size and it's covered in craters, where bits of space rock have crash-Landed on its surface."
        $ seen_total += 1
        $ seen_mercury = True
        show screen SolarBack with slowdiss

    if not seen_mercury_more:
        show screen mercury_button with slowdiss
        a "To know more facts and in-depth knowledge about mercury, click the 'More Button' on the bottom right."
    call screen SolarBack() with slowdiss

label mercury_more: # More fax on Mercury
    hide screen SolarBack
    hide screen mercury_button
    call variables from _call_variables_4
    scene bg mercury with slowdiss
    a "Speaking of size, Mercury is only about a third the size of the Earth. But, Pluto is even smaller. If you could put them on the scales, it would take 21 Plutos to balance one Mercury."
    a "The biggest crater is the Caloris Basin, which is about 800 miles across."
    a "Mercury also has huge plains, rotting hills, deep gorges, chasms, and cliffs."
    a "Mercury doesn't have any weather, because it has no air and hardly any atmosphere."
    a "That means there are no clouds to shield the surface of the planet from the baking-hot Sun during the day, or to keep in the heat at night. There is no wind or rain on Mercury, either. "
    a "Mercury zooms around the Sun in just 88 days, at an incredible 107,000 mph. That makes it faster than any space rocket ever invented."
    a "Alright! That's all I know about Mercury, wanna head back?\nClick the back button on the top."
    $ seen_mercury_more = True
    call screen SolarBack() with diss

label venus_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_5
    scene bg venus with slowdiss
    pause(2)

    if not seen_venus:
        a "Hey, That's hot!\nHaha this is Planet Venus my friend. The hottest planet in the Solar System!"
        a "Talking about mass, Venus is smaller than the Earth by just a tiny fraction. In other words, Venus's mass is about four-fifths of Earth's."
        $ seen_total += 1
        $ seen_venus = True
        show screen SolarBack with slowdiss

    if not seen_venus_more:
        show screen venus_button with slowdiss
        a "To know more, click the 'More Button' on the bottom right.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label venus_more:
    hide screen SolarBack
    hide screen venus_button
    call variables from _call_variables_6
    scene bg venus with slowdiss
    a "Here's the strange part! Heard of the 'Evening Star'?"
    a "Yes it's the same 'Red Planet' being referred to! It's called so because of the amount of light it reflects back."
    a "It's so bright that it's amongst the first points of light we see shining in the sky as it gets dark."
    a "Venus spins on its axis very slowly, but orbits the Sun more quickly than Earth. A day on Venus Is 243 Earth-days, but a year is only 225 Earth-days."
    a "Okay! Let's check something else now.\nClick the back button on the top."
    $ seen_venus_more = True
    call screen SolarBack() with diss

label earth_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_7
    scene bg earth with slowdiss
    pause(2)

    if not seen_earth:
        n "Aahh! Finally... fresh air! Yep, That's our home, the only planet with existence of life The planet Earth."
        n "The only planet with all essence of life built into. Also known as the 'Blue Planet', for about three-quarters of the Earth's surface is just water!"
        $ seen_total += 1
        $ seen_earth = True
        show screen SolarBack() with slowdiss

    if not seen_earth_more:
        show screen earth_button with slowdiss
        n "Wanna know more? Click the 'More Button'.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label earth_more:
    hide screen SolarBack
    hide screen earth_button
    call variables from _call_variables_8
    scene bg earth with slowdiss
    $ seen_earth_more = True
    n "\"Earth was once inhabitable.\" Yes! It's true. At the point of time during the creation of Earth, it was just a violent wasteland with only lava and craters as it's surface."
    n "It is over millions of years that the planet cooled down, oceans were formed and oxygen was made. It is said that the first life on Earth appeared about 3 billion years ago."
    n "Our planet like a 'giant magnet'! It is so because at the center of the Earth is a core of a molten metal called iron, which makes our planet like a giant magnet."
    n "This is what pulls the needle on a compass towards the magnetic North Pole."
    n "Time to go, just a sec let me have my last breath of natural oxygen... 'inhales and exhales'\nOkay, let's go! (Clisk on the 'Back Button')"
    call screen SolarBack()

label mars_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_9
    scene bg mars with slowdiss
    pause(2)

    if not seen_mars:
        a "This is Planet Mars. The planet looks rusty red because its surface is covered with iron-rich soil and rock."
        a "There are no seas on Mars, and it is very cold. Temperature on the planet are very erratic when compared to Earth."
        $ seen_total += 1
        $ seen_mars = True
        show screen SolarBack() with slowdiss

    if not seen_mars_more:
        show screen mars_button with slowdiss
        a "Wanna know more? Click the 'More Button'.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label mars_more:
    hide screen SolarBack
    hide screen mars_button
    call variables from _call_variables_10
    scene bg mars with slowdiss
    a "Long ago, Mars had flowing rivers of water, so there could have been life once, and there may be fossils buried underground."
    a "Its south pole is mostly 'dry ice', which is frozen CO2 gas. At the north pole there may be frozen water, mixed with the frozen CO2. There may be frozen water underground Mars, too."
    a "Mars's two tiny moons, Deimos and Phobos, are not round like our Moon. They look more like jacket potatoes! They might have been asteroids (space rocks) that Mars captured with its gravity."
    a "There's a record-breaking volcano on Mars! The Olympus-Mons, it is about 370 miles across and measures over 15 miles high. It's the Solar System's biggest volcano. Long ago it spurted out rivers of black lava."
    $ seen_mars_more = True
    call screen SolarBack() with diss

label jupiter_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_11
    scene bg jupiter with slowdiss
    pause(2)

    if not seen_jupiter:
        a "Isn't that huge! This is the largest planet in our Solar System!"
        a "Also known as the gas giant, about 90\% \of it is made out of gasses hydrogen and helium"
        $ seen_total += 1
        $ seen_jupiter = True
        show screen SolarBack() with slowdiss

    if not seen_jupiter_more:
        show screen jupiter_button with slowdiss
        a "Click the 'More Button'.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label jupiter_more:
    hide screen SolarBack
    hide screen jupiter_button
    call variables from _call_variables_12
    scene bg jupiter with slowdiss
    a "Jupiter is so big, that all the other planets in our solar system could fit inside it! If it was any bigger it's magnetic field might start collisions with other planets, so much so as the sun."
    a "There is always a violent storm in it's atmosphere, the Great Red Spot is amongst the largest of them. It is said that it has been raging since 300 Years!"
    $ seen_jupiter_more = True
    call screen SolarBack() with diss

label saturn_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_13
    scene bg saturn with slowdiss
    pause(2)

    if not seen_saturn:
        a "And here is Saturn, one of the only few planets with rings!"
        a "While they may look like solid rings, they are made up of millions of chunks of ice and rock."
        $ seen_total += 1
        $ seen_saturn = True
        show screen SolarBack() with slowdiss

    if not seen_saturn_more:
        show screen saturn_button with slowdiss
        a "You know the drill right!\nClick the 'More Button' for more facts.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label saturn_more:
    hide screen SolarBack
    hide screen saturn_button
    call variables from _call_variables_14
    scene bg saturn with slowdiss

    a "To simplify talking about the rings, scientists refer to each ring by a letter. The brightest of the entire ring are the rings A, B and C."
    a "Saturn is made up of liquid and gas, with a small rocky centre. It is so light in mass that, if there were an ocean big enough the planet, Saturn would float like a boat..."
    a "Saturn has 18 known moons. Amongst which, the biggest of them is Titan, it is the second largest moon in the solar system."
    $ seen_saturn_more = True
    call screen SolarBack() with diss

label uranus_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_15
    scene bg uranus with slowdiss
    pause(2)

    if not seen_uranus:
        a "Welcome to Uranus!"
        a "Unlike other planets, planet Uranus does not have ice at its poles!"
        $ seen_total += 1
        $ seen_uranus = True
        show screen SolarBack() with slowdiss

    if not seen_uranus_more:
        show screen uranus_button with slowdiss
        a "To know more, click the 'More Button'.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label uranus_more:
    hide screen SolarBack
    hide screen uranus_button
    call variables from _call_variables_16
    scene bg uranus with slowdiss
    a "The planet has 17 known moons. All of which are named after the characters from English literature. Such as: Oberon, Titania, etc..."
    a "The planet is tilted at such an angle that summer at it's south pole lasts over 42 years!"
    a "Last but not the least, this planet is made mainly from methane, hydrogen and helium."
    $ seen_uranus_more = True
    call screen SolarBack() with diss

label neptune_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_17
    scene bg neptune with slowdiss
    pause(2)

    if not seen_neptune:
        a "Here's the planet with ever-changing appearance, the planet Neptune."
        $ seen_total += 1
        $ seen_neptune = True
        show screen SolarBack() with slowdiss

    if not seen_neptune_more:
        show screen neptune_button with slowdiss
        a "Click the 'More Button'to know more.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label neptune_more:
    hide screen SolarBack
    hide screen neptune_button
    call variables from _call_variables_18
    scene bg neptune with slowdiss
    a "It's appearance is ever changing for the reason that in its atmosphere, extremely high-speed winds rip across the planet all the time."
    a "Also, the Dark Spots which are storms of gases on the planet's atmosphere explain why it looks like it is changing."
    a "Neptune has 14 known moons, among which Triton and Nereid are the recognized ones."
    a "Triton is one of the coldest places ever recorded! It's temperature is just 98°F away from being the lowest possible temperature in the entire universe."
    $ seen_neptune_more = True
    call screen SolarBack() with diss

label sun_pressed:
    hide screen solar_button
    hide screen SpaceBack
    hide screen SolarSystem
    call variables from _call_variables_19
    scene bg sun with slowdiss
    pause(2)

    if not seen_sun:
        a "It is one of the smallest stars composed of hydrogen and helium."
        a "In terms of size it is massive, It can fit over one million planets the size of Earth!"
        $ seen_total += 1
        $ seen_sun = True
        show screen SolarBack() with slowdiss

    if not seen_sun_more:
        show screen sun_button with slowdiss
        a "Wanna know more? Click the 'More Button'.\nTo go back click the 'Back Button'."
    call screen SolarBack() with slowdiss

label sun_more:
    hide screen SolarBack
    hide screen sun_button
    call variables from _call_variables_20
    scene bg sun with slowdiss
    a "The Sun accounts for 99.86\% \of the mass in the solar system"
    a "It is travelling at about 220 km per second!"
    a "The Sun rotates in the opposite direction than that of the Earth."
    a "Temperatures inside the Sun can reach as high as 15 million degrees Celsius!"
    $ seen_sun_more = True
    call screen SolarBack() with diss

label milkyway_pressed:
    hide screen Finish
    hide screen Endscreen
    hide screen solar_button
    hide screen SolarSystem
    hide screen SolarUI
    hide screen SolarBack
    hide screen MilkyUI
    call variables from _call_variables_21
    scene bg milky with slowdiss
    pause(2)

    if not seen_milkyway:
        a "Welcome to the home of our solar system!"
        a "It's shaped like a disc and its diameter is 120000 light years!"
        $ seen_total += 1
        $ seen_milkyway = True
        show screen SpaceBack with slowdiss

    if not seen_milkyway_more:
        show screen milkyway_button with slowdiss
        a "To know more, click the 'More Button'.\nTo go back click the 'Back Button'."
    call screen SpaceBack() with slowdiss

label milkyway_more:
    hide screen SpaceBack
    hide screen milkyway_button
    call variables from _call_variables_22
    scene bg milky with slowdiss
    a "It has a warped shaped because of the influence of our neighbourhood galaxies."
    a "It has over 200 billion stars!"
    a "There is also a huge black hole at the centre of our galaxy"
    a "The Milky Way, along with everything else in the universe, is moving through space and it is almost as old as the universe itself..."
    $ seen_milkyway_more = True
    call screen SpaceBack()

# # # # This ends the game.

label endscreen:
    hide screen SolarUI
    hide screen MilkyUI
    hide screen Endscreen
    hide screen Finish
    scene black with slowdiss
    a "Thank you for playing The Space Among Us, do make sure to check our GitHub for further updates...\n(Click to Continue)"
    scene bg outro with slowdiss
    pause(23)
    n "(Click to end game.)"
    return

label complete:
    hide screen SolarUI
    hide screen MilkyUI
    hide screen Endscreen
    hide screen Finish
    scene black with slowdiss
    a "Congratulations! You've completed the game..."
    a "Thank you for playing The Space Among Us, do make sure to check our GitHub for further updates...\n(Click to Continue)"
    scene bg outro with diss
    pause(23)
    n "(Click to end game.)"
    return

label splashscreen:
    screen black
    pause(2)
    show intro with slowdiss
    play music "gui/music/calm-bgmusic.mp3"
    pause(4.5)
    hide intro with slowdiss
    screen black
    pause(2)
    return
