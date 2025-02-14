class Aether:
    def __init__(self):
        self.name = "Aether"
        self.state = "Initializing"
        self.version = "1.0.0"

    def start(self):
        print(f"{self.name} {self.version} is now active.")
        self.state = "Active"

    def shutdown(self):
        print(f"{self.name} is shutting down...")
        self.state = "Inactive"

if __name__ == "__main__":
    aether = Aether()
    aether.start()
