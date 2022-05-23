package main

import "fmt"

type tree struct {
    value int
    left, right *tree
}

func main() {
    var t tree
    t.value = 1
    t.left = &tree{2, nil, nil}
    t.right = &tree{3, nil, nil}
    fmt.Println(t.value)
    fmt.Println(t.left.value)
    fmt.Println(t.right.value)
}