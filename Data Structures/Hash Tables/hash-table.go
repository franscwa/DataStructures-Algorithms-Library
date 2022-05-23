implement a hash table in go with descriptive comments

package main

import "fmt"

// HashTable is a data structure that stores key-value pairs and uses a hash function
// to determine where to store each key.
type HashTable struct {
	// The array that will store the key-value pairs.
	data [][]string
	// The hash function that will be used to determine where to store each key.
	hashFunc func(string) int
}

// NewHashTable creates a new HashTable with the given array size and hash function.
func NewHashTable(size int, hashFunc func(string) int) *HashTable {
	return &HashTable{
		data:     make([][]string, size),
		hashFunc: hashFunc,
	}
}

// Set inserts the given key-value pair into the HashTable.
func (ht *HashTable) Set(key, value string) {
	// Use the hash function to determine the index in the array to store the key-value pair.
	index := ht.hashFunc(key)
	// Append the key-value pair to the array at the determined index.
	ht.data[index] = append(ht.data[index], key, value)
}

// Get retrieves the value for the given key from the HashTable.
func (ht *HashTable) Get(key string) (string, error) {
	// Use the hash function to determine the index in the array where the key-value pair is stored.
	index := ht.hashFunc(key)
	// Loop through the array at the determined index to find the key-value pair.
	for i := 0; i < len(ht.data[index]); i += 2 {
		// If the key is found, return the value.
		if ht.data[index][i] == key {
			return ht.data[index][i+1], nil
		}
	}
	// If the key is not found, return an error.
	return "", fmt.Errorf("key not found: %s", key)
}

func main() {
	// Create a new HashTable with an array size of 10 and a hash function that returns the remainder of the key's ASCII value divided by 10.
	ht := NewHashTable(10, func(key string) int {
		return int(key[0]) % 10
	})

	// Insert the key-value pairs "foo" => "bar" and "hello" => "world" into the HashTable.
	ht.Set("foo", "bar")
	ht.Set("hello", "world")

	// Retrieve the value for the key "foo" from the HashTable.
	value, err := ht.Get("foo")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(value) // "bar"
	}

	// Retrieve the value for the key "hello" from the HashTable.
	value, err = ht.Get("hello")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(value) // "world"
	}

	// Retrieve the value for the key "goodbye" from the HashTable.
	// This should return an error because the key does not exist in the HashTable.
	value, err = ht.Get("goodbye")
	if err != nil {
		fmt.Println(err) // "key not found: goodbye"
	} else {
		fmt.Println(value)
	}
}