#implement a hash table in python with descriptive comments

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""

        # Hash value = (ASCII value of first letter * 100) + ASCII value of second letter
        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value

    def store(self, string):
        """Input a string that's stored in
        the table."""

        # Calculate hash value
        hash_value = self.calculate_hash_value(string)

        # If the hash value is already in the table,
        # append the string to the list at that slot
        if self.table[hash_value] != None:
            self.table[hash_value].append(string)
        # Otherwise, insert a new key-value pair into the table
        else:
            self.table[hash_value] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""

        # Calculate hash value
        hash_value = self.calculate_hash_value(string)

        # Check if string is in table
        if self.table[hash_value] != None:
            if string in self.table[hash_value]:
                return hash_value
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""

        # Hash value = (ASCII value of first letter * 100) + ASCII value of second letter
        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value