# 
# travellers.py
# Routines 1D travellers. 


class Traveller: 
    def __init__(self, location=0, speed=0, time=0, destination=0): 
        self.location = location
        self.speed = speed
        self.time = time
        self.destination = destination

    def time_to_target(self): 
        try: 
            return (self.destination - self.location) / speed
        except: 
            raise ValueError(
                'You must make your steps, in order to arrive there. '
                    )


def meet(traveller1, traveller2): 
    time = (
            (traveller2.location - traveller1.location) 
            / (traveller1.speed - traveller2.speed)
           )
    meet_location = traveller1.location + traveller1.speed * time
    # We always write f(x, t) so I place location first. 
    return (meet_location, time)
