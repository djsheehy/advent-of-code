package particle

import "math"

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
	p.Dy += p.Dy
	p.Dz += p.Dz
}

func abs(x int) int {
	return int(math.Abs(float64(x)))
}

// Distance calculates a particle's Manhattan distance from the origin.
func (p *Particle) Distance() int {
	return abs(p.X) + abs(p.Y) + abs(p.Z)
}
