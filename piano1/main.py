import random
from boopak.package import *
from boodle import agent
from boodle import stereo

water = bimport('org.boodler.old.water')

piano = bimport('com.apertome.pianosounds1')

low = [ piano.low_menacing, piano.lowphrase, piano.plod01_low_only, piano.plod02, piano.drone_low ]

# take out piano.mid_weird2
mid = [ piano.mid_weird1, piano.mid_phrase, piano.mid2_longphrase ]

mid_reversed = [ piano.mid_weird1_reversed, piano.mid_phrase_reversed, piano.mid2_longphrase_reversed ]

mid_reverb = [ piano.med_reverb_phrase_x2, piano.med_reverb_phrase,  piano.med_reverb_phrase_soft_x2, piano.med_reverb_phrase_soft, piano.drone_med, piano.med_reverb_long_phrase ]

mid_all = mid + mid_reversed + mid_reverb

high = [ piano.high, piano.high_descent, piano.high2_onenote, piano.high4_longphrase ]

high_reversed = [ piano.high_reversed, piano.high_descent_reversed, piano.high2_onenote_reversed, piano.high4_longphrase_reversed ]

mid_high = mid + high

abstract = [ piano.abstract1, piano.abstract2, piano.thud ]
#abstract = [ piano.abstract1, piano.abstract2, piano.bang01 ]

full_range = [ piano.plod02 ]

class Piano1(agent.Agent):
    def run(self):
        low_ag = Low()
        self.sched_agent(low_ag)
        high_ag = High()
        #high_chan = self.new_channel()
        high_reverse_ag = HighReverse()
        mid_high_ag = MidHigh()
        high_delay = random.uniform(3, 10)
        self.sched_agent(high_ag, delay=high_delay)
        #self.sched_agent(mid_high_ag, delay=high_delay)
        mid_ag = Mid()
        mid_delay = high_delay * 2
        self.sched_agent(mid_ag, delay=mid_delay)
        self.sched_agent(high_reverse_ag, delay=mid_delay)
        abstract_ag = Abstract()
        abstract_delay = random.uniform(10, 20)
        self.sched_agent(abstract_ag, delay=abstract_delay)
        full_range_ag = FullRange()
        #full_range_delay = 30 * random.uniform(0.75, 1.25)
        full_range_delay = abstract_delay * 2
        #self.sched_agent(full_range_ag, delay=full_range_delay)



class Low(agent.Agent):
    def run(self):
        pan = random.uniform(-0.5, 0.5)
        dur = self.sched_note_pan(random.choice(low), pan=pan)
        #delay = random.uniform(0.25, 0.75)
        delay = random.uniform(1, 2) * dur
        self.resched(delay)

class MidHigh(agent.Agent):
    def run(self):
        pitches = [ 0.5, 1, 2 ]
        dur = self.sched_note(random.choice(mid_high))
        #dur = self.sched_note(random.choice(mid_high), pitch=random.choice(pitches))
        #delay = random.uniform(0.25, 0.75)
        delay = random.uniform(1, 2) * dur
        may_overlap = True
        if not may_overlap:
            self.resched(delay)
        else:
            # 1 in y chance there will be overlapping notes
            chance = 1.0/20;
            rand = random.uniform(0, 1)
            if rand >= chance:
                short_delay = random.uniform(0,0.5)
                self.resched(short_delay)
            else:
                self.resched(delay)

class High(agent.Agent):
    def run(self):
        pan = random.uniform(-2, 2)
        pan = -1
        #chan = self.new_channel_pan(stereo.fixed(pan))
        #self.set_pan(pan)
        dur = self.sched_note_pan(random.choice(high), pan=stereo.shift(pan))
        #delay = random.uniform(0.25, 0.75)
        delay = random.uniform(1, 1.5) * dur
        may_overlap = False
        if not may_overlap:
            self.resched(delay)
        else:
            # 1 in y chance there will be overlapping notes
            chance = 1.0/20;
            rand = random.uniform(0, 1)
            if rand <= chance:
                short_delay = random.uniform(0,0.5)
                self.resched(short_delay)
            else:
                self.resched(delay)
        #self.resched(delay)

class HighReverse(agent.Agent):
    def run(self):
        pan = random.uniform(-1, 1)
        pan = 1
        #chan = self.new_channel_pan(stereo.fixed(pan))
        dur = self.sched_note_pan(random.choice(high_reversed), pan=pan)
        #delay = random.uniform(0.25, 0.75)
        delay = random.uniform(2, 4) * dur
        self.resched(delay)

class Mid(agent.Agent):
    def run(self):
        pan = random.uniform(-1, 1)
        dur = self.sched_note_pan(random.choice(mid_all), stereo.shift(pan))
        #dur = self.sched_note(random.choice(mid))
        #delay = random.uniform(0.25, 0.75)
        delay = random.uniform(1, 2) * dur
        self.resched(delay)

class Abstract(agent.Agent):
    def run(self):
        pan = random.uniform(-2, 2)
        dur = self.sched_note_pan(random.choice(abstract), pan=pan)
        delay = random.uniform(5, 20)
        #delay = random.uniform(0.75, 1.25) * dur
        self.resched(delay)

class FullRange(agent.Agent):
    def run(self):
        dur = self.sched_note(random.choice(full_range))
        #delay = random.uniform(0.25, 10)
        delay = random.uniform(1.5, 4) * dur
        self.resched(delay)



class Example(agent.Agent):
    def run(self):
        #chan = self.new_channel_pan(-1)

        #self.sched_note(water.droplet_bloink, chan=chan)
        self.sched_note_pan(water.droplet_plink, pan=stereo.shift(-2))
        #chan.set_pan(-1, 0.05)

