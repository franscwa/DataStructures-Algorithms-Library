implement a trie in go

package main

import "fmt"

type Trie struct {
	Root *TrieNode
}

type TrieNode struct {
	Children map[rune]*TrieNode
	IsEnd    bool
}

func NewTrie() *Trie {
	return &Trie{Root: &TrieNode{Children: make(map[rune]*TrieNode)}}
}

func (t *Trie) Insert(word string) {
	node := t.Root
	for _, char := range word {
		if _, ok := node.Children[char]; !ok {
			node.Children[char] = &TrieNode{Children: make(map[rune]*TrieNode)}
		}
		node = node.Children[char]
	}
	node.IsEnd = true
}

func (t *Trie) Search(word string) bool {
	node := t.Root
	for _, char := range word {
		if _, ok := node.Children[char]; !ok {
			return false
		}
		node = node.Children[char]
	}
	return node.IsEnd
}

func (t *Trie) StartsWith(prefix string) bool {
	node := t.Root
	for _, char := range prefix {
		if _, ok := node.Children[char]; !ok {
			return false
		}
		node = node.Children[char]
	}
	return true
}

func main() {
	trie := NewTrie()

	trie.Insert("apple")
	fmt.Println(trie.Search("apple"))   // outputs true
	fmt.Println(trie.Search("app"))     // outputs false
	fmt.Println(trie.StartsWith("app")) // outputs true

	trie.Insert("app")
	fmt.Println(trie.Search("app")) // outputs true
}