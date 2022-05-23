package main

func twoPointerExample(s string, t string) bool {
    
    // set two pointers, i and j, to the start of each string
    i := 0
    j := 0
    
    // continue looping while both pointers are within the bounds of their respective strings
    for i < len(s) && j < len(t) {
        
        // if the characters at pointers i and j match
        if s[i] == t[j] {
            
            // advance both pointers
            i++
            j++
            
        // if the characters at pointers i and j don't match
        } else {
            
            // return false since we know the strings are not equal
            return false
        }
    }
    
    // return true since we've reached the end of both strings and they are equal
    return true
}