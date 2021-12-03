package particle

import (
	"fmt"
	"math"
)

// Particle represents a particle with coordinates, velocity and acceleration.
type Particle struct {
	X, Y, Z    int
	Dx, Dy, Dz int
	Ax, Ay, Az int
}

// Move moves and accelerates a particle.
func (p *Particle) Move() {
	p.X += p.Dx
	p.Y += p.Dy
	p.Z += p.Dz
	p.Dx += p.Ax
	p.Dy += p.Ay
	p.Dz += p.Az
	fmt.Printf("%#v\n", p)
}

func abs(x int) int {
	return int(math.Abs(float64(x)))
}

// Distance calculates a particle's Manhattan distance from the origin.
func (p *Particle) Distance() int {
	return abs(p.X) + abs(p.Y) + abs(p.Z)
}

// GetClosest gets the closest distance to the origin.
func (p *Particle) GetClosest() int {
	dist := p.Distance() // current distance
	best := dist         // closest distance
	if p.Dx == 0 && p.Dy == 0 && p.Dz == 0 && p.Ax == 0 && p.Ay == 0 && p.Az == 0 {
		return best
	}
	// move twice to determine velocity and accel.
	p.Move()
	d := p.Distance()
	vel := d - dist // velocity relative to origin
	dist = d
	if dist < best {
		best = dist
	}
	p.Move()
	d = p.Distance()
	if d < best {
		best = d
	}
	vel2 := d - dist
	acc := vel2 - vel // acceleration relative to origin
	dist = d
	for vel < 0 || acc <= 0 {
		d = p.Distance()
		if d < best {
			best = d
		}
		vel = vel2
		vel2 = d - dist
		acc = vel2 - vel
		dist = d
		p.Move()
	}
	return best
}
