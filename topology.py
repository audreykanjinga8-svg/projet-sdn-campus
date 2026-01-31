from mininet.topo import Topo
from mininet.link import TCLink

class CampusTopo(Topo):
    def build(self):

        core = self.addSwitch('s1')
        it = self.addSwitch('s2')
        admin = self.addSwitch('s3')
        lab = self.addSwitch('s4')

        self.addLink(core, it, cls=TCLink, bw=100)
        self.addLink(core, admin, cls=TCLink, bw=50)
        self.addLink(core, lab, cls=TCLink, bw=20)

        for i in range(1, 4):
            host = self.addHost(f'h_it{i}')
            self.addLink(host, it)

topos = {
    'campus': CampusTopo
}
