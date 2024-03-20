import noise
import numpy as np


def generate_chunk(x, y, width=50, height=50, scale=10.0):
    world_map = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            value = noise.pnoise2(x / scale + i / scale,
                                  y / scale + j / scale,
                                  octaves=12,
                                  persistence=0.5,
                                  lacunarity=2.0,
                                  repeatx=1024,
                                  repeaty=1024,
                                  base=42)
            world_map[i][j] = int((value + 1) * 1.5)
    return world_map


# Generate a chunk at position (0, 0)
chunk = generate_chunk(0, 0)

# Convert the chunk to a list of strings
chunk_as_strings = [''.join(map(str, row)) for row in chunk.astype(int)]

# Save the chunk to a file
with open('../content/maps/world_map.map', 'w') as f:
    f.write('\n'.join(chunk_as_strings))
