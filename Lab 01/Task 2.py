class Server:
    def __init__(self, name):
        self.name = name
        self.load = random.choice(["underload", "balanced","overloaded"])

    def setload(self, load):
        self.load = load

class LoadBalanceraAgent:
    def __init__(self, servers):
        self.servers = servers

    def scan(self):
        for server in self.servers:
            print(f"Server: {server.name} is {server.load}")

        print()

    def balance(self):
        for server in self.servers:
            if server.load == "overloaded":
                print(f"Balancing Server: {server.name} from {server.load} to underload")
                server.load = "underload"

            elif server.load == "underload":
                print(f"Balancing Server: {server.name} from {server.load} to balanced")
                server.load = "balanced"

        print("\n")

    def display(self):
        print("Updated load status of servers")
        for server in self.servers:
            print(f"Server: {server.name} is {server.load}")



a = Server("Server A")
b = Server("Server B")
c = Server("Server C")
d = Server("Server D")
e = Server("Server E")

Servers = [Server("Server A"), Server("Server B"), Server("Server C"), Server("Server D"), Server("Server E")]

loadAg = LoadBalanceraAgent(Servers)

loadAg.scan()
loadAg.balance()
loadAg.display()
