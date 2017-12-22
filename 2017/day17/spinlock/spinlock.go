package spinlock

import "container/ring"

type SpinLock struct {
	buffer, pos *ring.Ring
	value       int
}

func New() *SpinLock {
	s := new(SpinLock)
	s.buffer = ring.New(1)
	s.buffer.Value = 0
	s.pos = s.buffer
	return s
}

func (s *SpinLock) Step(n int) {
	for i := 0; i < n; i++ {
		s.pos = s.pos.Next()
	}
	s.value++
	r := ring.New(1)
	r.Value = s.value
	s.pos.Link(r)
	s.pos = r
}

func (s *SpinLock) NextValue() int {
	return s.pos.Next().Value.(int)
}

func (s *SpinLock) SecondValue() int {
	return s.buffer.Next().Value.(int)
}
