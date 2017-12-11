#!/usr/bin/env python3
import tdl

from player import Player

WIDTH, HEIGHT = 50, 40


tdl.setFont('terminal8x8.png')
console = tdl.init(WIDTH, HEIGHT, 'Python RL')

p = Player()
p.position = WIDTH//2, HEIGHT//2

map = [
['#','#','#','#',],
['#',' ',' ','#',],
['#',' ',' ','#',],
['#',' ',' ','#',],
['#',' ',' ','#',],
['#',' ',' ','#',],
['#',' ',' ','#',],
['#','#','#','#',],
]



game_running = True
while game_running:
	console.clear()	

	for x in range (8):
		for y in range(4):
			if map[x][y]:

				console.draw_char(x, y, map[x][y])

	p.draw(console)
	

	tdl.flush()

	print(p.position)
	for event in tdl.event.get():
		p.handle_events(event)
		if event.type == "QUIT":
			game_running = False
 
