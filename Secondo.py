import math

LIGHT_SPEED = 1.

class Particle:
    def __init__(self, name, mass, charge, momentum = 0.):
        self.name = name
        self.charge = charge
        self.mass = mass
        self.momentum = momentum

    def print_info(self):
        print(f'Particle {self.name}: mass = {self.mass} Mev/c^2, charge = {self.charge} e, momentum = {self.momentum} Mev/c')

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, value):
        if value < 0.:
            print('Negative momentum will be set to 0.')
            self._momentum = 0.
        else:
            self._momentum = value

    @property
    def energy(self):
        return math.sqrt((self.momentum * LIGHT_SPEED)**2 + (self.mass * LIGHT_SPEED**2)**2)

    @energy.setter
    def energy(self, value):
            if value < self.mass:
                print('Energy cant be less than the mass.')
                return
            self.momentum = math.sqrt(value**2 - (self.mass * LIGHT_SPEED**2)**2)/LIGHT_SPEED**2

    @property
    def beta(self):
        if not (self.energy > 0.):
            return 0.
        else:
            return LIGHT_SPEED * self.momentum / self.energy

    @beta.setter
    def beta(self, value):
        if value < 0. or value > 1.:
            print('Bad value.')
            return
        if not value < 1. and self.mass > 0.:
            print('only massless particles can have beta = 1.')
            return
        self.momentum = LIGHT_SPEED * value * self.mass / math.sqrt(1. - value**2)

class Proton(Particle):
    NAME = 'Proton'
    CHARGE = 1.
    MASS = 938.272

    def __init__(self, momentum=0):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


class Alpha(Particle):
    NAME = 'Alpha'
    MASS = 3727.3
    CHARGE = +4.

    def __init__(self, momentum=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)

if __name__ == '__main__':
    proton = Proton(200.)
    proton.print_info()
    proton.beta = 0.8
    proton.print_info()
    alpha = Alpha(20.)
    alpha.energy = 10000.
    alpha.print_info()
