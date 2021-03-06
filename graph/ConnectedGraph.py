'''
	 using Breadth-First Search Algorithm (BFS)
'''

def is_connected(g):
	start_node = list(g.keys())[0]
	color = {v: 'white' for v in g.keys()}
	color[start_node] = 'gray'
	S = [start_node]
	while len(S) != 0:
		u = S.pop()
		for v in g[u]:
			if color[v] == 'white':
				color[v] = 'gray'
				S.append(v)
			color[u] = 'black'
	return list(color.values()).count('black') == len(g.keys())
