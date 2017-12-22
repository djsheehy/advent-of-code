package tree

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

// Tree contains a tree of nodes and keeps track of their connections.
type Tree struct {
	root     *Node
	parentOf map[string]string
	nodeMap  map[string]*Node
}

// NewTree creates a new Tree.
func NewTree() *Tree {
	t := Tree{parentOf: make(map[string]string),
		nodeMap: make(map[string]*Node)}
	return &t
}

// Node is a node in the Tree.
type Node struct {
	Name        string
	Weight      int
	totalWeight int
	Parent      *Node
	Children    []string
	ChildNodes  []*Node
}

func (n *Node) String() string {
	kids := strings.Join(n.Children, ", ")
	if len(n.Children) == 0 {
		kids = "nil"
	}
	var parent string
	if n.Parent == nil {
		parent = "nil"
	} else {
		parent = n.Parent.Name
	}
	return fmt.Sprintf(
		`Name: %s
Weight: %d
Parent: %s
Children: %s`, n.Name, n.Weight, parent, kids)
}

// Parse takes a string with the right format and generates a Node.
func Parse(line string) *Node {
	pattern := regexp.MustCompile(`([a-z]+) \((\d+)\)`)
	node := new(Node)
	matches := pattern.FindStringSubmatch(line)
	node.Name = matches[1]
	weight, _ := strconv.Atoi(matches[2])
	node.Weight = weight
	split := strings.Split(line, " -> ")
	if len(split) > 1 {
		children := strings.Split(split[1], ", ")
		node.Children = children
	} else {
		node.Children = make([]string, 0)
	}

	return node
}

// FindNode looks up a node in the tree. Returns nil if not found.
func (t *Tree) FindNode(name string) *Node {
	node, ok := t.nodeMap[name]
	if ok {
		return node
	}
	return nil
}

// AddNode adds a Node to the Tree.
func (t *Tree) AddNode(n *Node) {
	// if another node has me as a child, hook me up
	if parent, ok := t.parentOf[n.Name]; ok {
		n.Parent = t.FindNode(parent)
	}
	t.nodeMap[n.Name] = n

	// for each child, make the new node its parent
	for _, child := range n.Children {
		t.parentOf[child] = n.Name
		// if the child node itself exists, hook it up to its parent
		cnode := t.FindNode(child)
		if cnode != nil {
			cnode.Parent = n
		}
	}
}

// GetRoot picks a random node, then walks up the tree until it reaches the root.
func (t *Tree) GetRoot() *Node {
	if t.root != nil {
		return t.root
	}
	var node *Node
	for _, n := range t.nodeMap {
		node = n
		break
	}
	for node.Parent != nil {
		node = node.Parent
	}
	t.root = node
	t.buildTree(node)
	return node
}

func (t *Tree) buildTree(root *Node) {
	root.ChildNodes = make([]*Node, len(root.Children))
	for i, name := range root.Children {
		root.ChildNodes[i] = t.FindNode(name)
	}
	for _, child := range root.ChildNodes {
		t.buildTree(child)
	}
}

// GetWeight gets the weight of a node by adding its own weight and the weight of its children.
func (n *Node) GetWeight() int {
	weight := n.Weight
	if n.totalWeight > weight {
		return n.totalWeight
	}
	for _, child := range n.ChildNodes {
		weight += child.GetWeight()
	}
	n.totalWeight = weight
	return weight
}

func (n *Node) isBalanced() bool {
	if len(n.ChildNodes) == 0 {
		return true
	}
	w := n.ChildNodes[0].GetWeight()
	for _, n := range n.ChildNodes[1:] {
		if n.GetWeight() != w {
			return false
		}
	}
	return true
}

func (n *Node) getMajorityWeight() int {
	// handle edge cases
	if len(n.ChildNodes) == 0 {
		return n.Weight
	}
	if len(n.ChildNodes) == 1 {
		return n.ChildNodes[0].GetWeight()
	}

	weightSet := make(map[int]bool)
	var ans int
	for _, c := range n.ChildNodes {
		if ok := weightSet[c.GetWeight()]; ok {
			ans = c.GetWeight()
			break
		}
		weightSet[c.GetWeight()] = true
	}
	return ans
}

// GetBadNode gets the child node that throws off the balance.
func (n *Node) GetBadNode(sibling int) (*Node, int) {
	// if leaf node, there are is no bad node. But this won't be reached, because I know there's a bad node.
	if len(n.ChildNodes) == 0 {
		return nil, -1
	}

	// scan children for the one node that doesn't match.
	maj := n.getMajorityWeight()
	var bad *Node
	for _, c := range n.ChildNodes {
		if c.GetWeight() != maj {
			bad = c
			break
		}
	}
	// if no bad node found, the current node is guilty.
	if bad == nil {
		return n, sibling
	}
	// if bad node's children are balanced, bad node is guilty.
	if bad.isBalanced() {
		return bad, maj
	}
	// otherwise, keep looking
	return bad.GetBadNode(maj)
}
