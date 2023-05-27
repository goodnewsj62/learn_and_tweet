from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Garage():
    def up(self):
        print("raising garage door")
    def down(self):
        print("closing garage door")

    def stop(self):
        print("action stop")
    def lightOn(self):
        print("warning light on")
    def lightOff(self):
        print("warning light off")



class GarageDoorOpenCommand(Command):
    def __init__(self,  garage:Garage) -> None:
        self.garage =  garage

    def execute(self):
        self.garage.lightOn()
        self.garage.up()
        self.garage.stop()
        self.garage.lightOff()


class RemoteInvoker():
    def __init__(self) -> None:
        self.slot = None

    def setCommand(self, command:Command):
        self.slot = command

    def openGarage(self):
        self.slot.execute()


if __name__ == "__main__":
    garage =  Garage()
    mycommand =  GarageDoorOpenCommand(garage)
    invoker =  RemoteInvoker()
    
    invoker.setCommand(mycommand)
    invoker.openGarage()