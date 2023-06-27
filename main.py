from engine.run.run import Run

if __name__=="__main__":
    gravity_toggle = True
    full_screen = False

    run = Run(gravity_toggle=gravity_toggle, full_screen=full_screen)
    run.run()