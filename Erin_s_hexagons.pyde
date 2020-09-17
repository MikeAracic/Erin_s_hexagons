size(200, 200)
hexagon_radius=10
sqrt_3_2=sqrt(3)/2
s = createShape()
s.beginShape()
s.fill(0, 0, 255)
s.stroke(255)
#s.noStroke()
s.vertex(-hexagon_radius, 0)
s.vertex(hexagon_radius*-.5, sqrt_3_2*hexagon_radius*-1)
s.vertex(hexagon_radius*+.5, sqrt_3_2*hexagon_radius*-1)
s.vertex(hexagon_radius, 0)
s.vertex(hexagon_radius*+.5, sqrt_3_2*hexagon_radius*+1)
s.vertex(hexagon_radius*-.5, sqrt_3_2*hexagon_radius*+1)
s.endShape(CLOSE)
shape(s, hexagon_radius*1, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*4, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*7, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*10, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*13, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*16, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*19, hexagon_radius*sqrt_3_2)
shape(s, hexagon_radius*2.5, hexagon_radius*sqrt_3_2*2)
shape(s, hexagon_radius*5.5, hexagon_radius*sqrt_3_2*2)
shape(s, hexagon_radius*8.5, hexagon_radius*sqrt_3_2*2)
shape(s, hexagon_radius*11.5, hexagon_radius*sqrt_3_2*2)
shape(s, hexagon_radius*14.5, hexagon_radius*sqrt_3_2*2)
shape(s, hexagon_radius*17.5, hexagon_radius*sqrt_3_2*2)
for hex_y in range (1, 20,2):
    println(hex_y)
    for hex_x in range (1,21,3):
        shape(s, hexagon_radius*hex_x, hex_y*hexagon_radius*sqrt_3_2)
        shape(s, 1.5*hexagon_radius+(hexagon_radius*hex_x), hexagon_radius*sqrt_3_2*(hex_y+1))    
