from boopak.package import *
from boodle import agent
import random

sounds = bimport('com.apertome.jayden_sounds')

intromessup = sounds.beginning_screwup01
introbetterish = sounds.beginning_betterish
longnotes = [sounds.longnote01, sounds.longnote02, sounds.longnote03, sounds.longnote04, sounds.longnote05, sounds.longnote06, sounds.longnote07]
lowish01 = [sounds.lowish_01_dry, sounds.lowish_01_flange_phase]
harmonics01 = sounds.harmonics_long01
arpeggios01 = [sounds.arpeggio_slow01, sounds.arpeggio01]
high01 = [sounds.high01, sounds.high02, sounds.high03, sounds.high04]
lowplodding01 = sounds.low_plodding_01
low01 =  [sounds.low02, sounds.low03, sounds.low04, sounds.low05]
mid01 = sounds.mid01

nummeasures = 4
beatsper = 4
numbeats = nummeasures * beatsper
rate = 0.6

initkickpattern = [1, 0, 0, 0, 1, 0, 0, 0]

# The Jayden class runs the whole thing
class Jayden(agent.Agent):
	name = 'ambient guitar thing'
	def run(self):
		self.sched_agent(IntroScrewup())
		self.sched_agent(IntroBetterish(), 25)
		self.sched_agent(LongNotes(), 20)
		self.sched_agent(LongNotesLowered(), 40)
		self.sched_agent(Lowish01(), 30)
		self.sched_agent(Harmonics01(), 50)
		self.sched_agent(Arpeggios01(), 60)
		self.sched_agent(High01(), 80)
		self.sched_agent(Low01(), 90)
		self.sched_agent(LowPlodding01(), 70)
		self.sched_agent(Mid01(), 55)

class IntroScrewup(agent.Agent):
	name = 'intro screwup'
	def run(self):
		introdur = self.sched_note(intromessup)
		introbdur = self.sched_note(introbetterish, 1, 1, introdur + 2)

class IntroBetterish(agent.Agent):
	name = 'intro betterish'
	def run(self):
		dur = self.sched_note(introbetterish)
		self.resched(random.uniform(dur * 2, dur * 7))

class LongNotes(agent.Agent):
	name = 'random long notes'
	def run(self):
		dur = self.sched_note_pan(random.choice(longnotes), random.uniform(-1, 1))
		self.resched(random.uniform(6, 12))

class LongNotesLowered(agent.Agent):
	name = 'random long notes'
	def run(self):
		dur = self.sched_note_pan(random.choice(longnotes), random.uniform(-0.5, 0.5), 0.5)
		self.resched(random.uniform(10, 15))

class Lowish01(agent.Agent):
	name = 'lowish stuff, randomly flanged'
	def run(self):
		dur = self.sched_note(random.choice(lowish01))
		self.resched(random.uniform(dur+20, dur+30))

class Harmonics01(agent.Agent):
	name = 'long harmonics passage'
	def run(self):
		dur = self.sched_note(harmonics01, 1, 1.2)
		self.resched(random.uniform(dur * 2, dur * 4))

class Arpeggios01(agent.Agent):
	name = 'slow arpeggio'
	def run(self):
		dur = self.sched_note(random.choice(arpeggios01), 1, 1.2)
		self.resched(random.uniform(dur * 2, dur * 4))

class High01(agent.Agent):
	name = 'high thing'
	def run(self):
		dur = self.sched_note_pan(random.choice(high01), random.uniform(-1.4, 1.4), 1, 0.8)
		self.resched(random.uniform(dur * 3, dur * 6))

class Mid01(agent.Agent):
	name = 'mid thing'
	def run(self):
		dur = self.sched_note_pan(mid01, random.uniform(-0.7, 0.7))
		self.resched(random.uniform(dur * 2, dur * 6))

class Low01(agent.Agent):
	name = 'low thing'
	def run(self):
		dur = self.sched_note(random.choice(low01), 1, 1.2)
		self.resched(random.uniform(dur * 1.5, dur * 2))

class LowPlodding01(agent.Agent):
	name = 'low plodding thing'
	def run(self):
		dur = self.sched_note(lowplodding01)
		self.resched(dur + random.uniform(15, 50))


