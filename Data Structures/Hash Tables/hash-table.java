//implement a hash table in java




import java.util.*;

class HashTable {

    private int ARRAY_SIZE;
    private int[] array;

    public HashTable(int size) {
        this.ARRAY_SIZE = size;
        array = new int[size];
        Arrays.fill(array, - 1);
    }

    public void insertKey(int key) {
        int hash = (key % ARRAY_SIZE);
        while (array[hash] != - 1) {
            hash = (hash + 1) % ARRAY_SIZE;
        }
        array[hash] = key;
    }

    public boolean searchKey(int key) {
        int hash = (key % ARRAY_SIZE);
        while (array[hash] != - 1) {
            if (array[hash] == key) {
                return true;
            }
            hash = (hash + 1) % ARRAY_SIZE;
        }
        return false;
    }

    public void deleteKey(int key) {
        int hash = (key % ARRAY_SIZE);
        while (array[hash] != - 1) {
            if (array[hash] == key) {
                break;
            }
            hash = (hash + 1) % ARRAY_SIZE;
        }
        if (array[hash] == key) {
            int temp = array[hash];
            array[hash] = - 1;
            hash = (hash + 1) % ARRAY_SIZE;
            while (array[hash] != - 1) {
                int newHash = (array[hash] % ARRAY_SIZE);
                if (hash <= newHash && newHash <= hash) {
                    array[hash] = array[newHash];
                    array[newHash] = - 1;
                    hash = newHash + 1;
                } else {
                    array[hash] = array[newHash];
                    array[newHash] = - 1;
                    hash = newHash + 1;
                }
            }
        } else {
            System.out.println("This key does not exist.");
        }
    }

    public void printHashTable() {
        for (int i = 0; i < ARRAY_SIZE; i++) {
            System.out.println(array[i]);
        }
    }

    public static void main(String[] args) {
        HashTable table = new HashTable(10);

        table.insertKey(25);
        table.insertKey(35);
        table.insertKey(45);
        table.insertKey(55);

        table.searchKey(25);
        table.searchKey(125);

        table.deleteKey(25);
        table.printHashTable();
    }
}