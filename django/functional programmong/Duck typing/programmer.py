class Pycharch:
    def open(self):
        print("pycharm open")
    def run(self):
        print("pycharm run")
    def debug(self):
        print("pycharm debug")

class Vs:
    def open(self):
        print("vs open")
    def run(self):
        print("vs run")
    def debug(self):
        print("vs debug")



class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharch()
visual=Vs()
pg=Programmer()
pg.coding(visual)
