# Particles-py
this is just a little project to showcase little particles simulators

# purple rain
The purpleRain module is like a digital rain machine that makes it "rain" purple particles on your screen.

It has two main parts:

Drop: This is like a single raindrop. It has properties like color (which is purple), wind intensity (how much the wind affects it), rain intensity (how fast it falls), and length (how long the drop appears). It has two main actions: fall (which makes the drop move) and draw (which makes the drop appear on the screen).

PurpleRain: This is like the cloud that produces the rain. It manages a bunch of Drop instances. It has a get_drops method that creates new Drop instances until the number of drops matches the desired rain intensity. It also has a draw method that makes all the drops appear on the screen, and a reset method that clears all the drops (like stopping the rain).

In the main program, an instance of PurpleRain is created and added to a Window instance. The Window is like the sky or the environment where the rain happens. It's responsible for creating the application window and managing the main event loop (which is like the passage of time in this simulation). The PurpleRain instance is then drawn onto this window, creating the "purple rain" effect.