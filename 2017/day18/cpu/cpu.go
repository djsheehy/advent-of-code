package cpu

import (
	"strconv"
	"strings"
)

// CPU holds the state of a virtual machine.
type CPU struct {
	registers   map[string]int
	code        []string
	pc          int
	rcvCallback func(int)
	LastSound   int
	Recovered   int
}

// New creates a new CPU.
func New(codes []string, callback func(int)) *CPU {
	return &CPU{
		registers:   make(map[string]int),
		code:        codes,
		rcvCallback: callback,
	}
}

func (cpu *CPU) get(reg string) int {
	n, e := strconv.Atoi(reg)
	if e != nil {
		return cpu.registers[reg]
	}
	return n
}

// Execute executes a line of code. Returns true if still running.
func (cpu *CPU) Execute() bool {
	var x, y int
	words := strings.Split(cpu.code[cpu.pc], " ")
	switch words[0] {
	case "snd":
		cpu.LastSound = cpu.get(words[1])
		cpu.pc++
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
		if x != 0 {
			cpu.Recovered = cpu.LastSound
			cpu.rcvCallback(cpu.Recovered)
		}
		cpu.pc++
	case "jgz":
		x, y = cpu.get(words[1]), cpu.get(words[2])
		if x > 0 {
			cpu.pc += y
		} else {
			cpu.pc++
		}
	}
	return 0 <= cpu.pc && cpu.pc < len(cpu.code)
}
