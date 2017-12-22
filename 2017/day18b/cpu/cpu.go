package cpu

import (
	"strconv"
	"strings"
)

// State keeps track of the state of the CPU.
type State int

const (
	// Running means the CPU can execute instructions.
	Running State = iota
	// Stopped means the CPU stopped
	Stopped = 1
	// Waiting means the CPU is waiting to receive data.
	Waiting = 2
)

// CPU contains the state of a virtual CPU.
type CPU struct {
	registers map[string]int
	code      []string
	pc        int
	state     State
}

// NewCPU makes a new CPU with the given code and id.
func NewCPU(code []string, id int) *CPU {
	c := &CPU{
		registers: map[string]int{"p": id},
		code:      code,
		pc:        0,
		state:     Running,
	}
	return c
}

func (cpu *CPU) get(reg string) int {
	n, e := strconv.Atoi(reg)
	if e != nil {
		return cpu.registers[reg]
	}
	return n
}

// Run runs the CPU until blocked by a rcv command or stops.
func (cpu *CPU) Run(in, out chan int) {
	for {

	}
}

// Execute executes a line of code.
func (cpu *CPU) Execute() {
	var x, y int
	words := strings.Split(cpu.code[cpu.pc], " ")
	switch words[0] {
	case "snd":
		// send data here
	case "set":
		y = cpu.get(words[2])
		cpu.registers[words[1]] = y
		cpu.pc++
	case "add":
		x = cpu.get(words[1])
		y = cpu.get(words[2])
		cpu.registers[words[1]] = x + y
		cpu.pc++
	case "mul":
		x = cpu.get(words[1])
		y = cpu.get(words[2])
		cpu.registers[words[1]] = x * y
		cpu.pc++
	case "mod":
		x = cpu.get(words[1])
		y = cpu.get(words[2])
		cpu.registers[words[1]] = x % y
		cpu.pc++
	case "rcv":
		x = cpu.get(words[1])
		// receive data here
	case "jgz":
		x, y = cpu.get(words[1]), cpu.get(words[2])
		if x > 0 {
			cpu.pc += y
		} else {
			cpu.pc++
		}
	}
}
