#Just import your libraries or whatever the heck you desire here
import convert


if __name__ == "__main__":
    print("Hola mundo!") #Just testing haha
    import ui
    # The UI comes last on load, hence why it's here.
    # But we shouldn't really be running the UI from its own module,
    # rather, we should import the classes and have the main application here
    # so the communication with the other modules becomes easier.
