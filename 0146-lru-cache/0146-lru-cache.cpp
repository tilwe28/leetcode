class LRUCache {
private:
    list<int> order;
    unordered_map<int, pair<int, list<int>::iterator>> cache; 
    int capacity;

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (!cache.contains(key))
            return -1;

        order.erase(cache[key].second);
        order.push_back(key);
        cache[key].second = --order.end();
        return cache[key].first;
    }
    
    void put(int key, int value) {
        if (cache.contains(key)) {
            order.erase(cache[key].second);
        } else if (order.size() == capacity) {
            cache.erase(order.front());
            order.pop_front();
        }
        order.push_back(key);
        cache[key] = {value, --order.end()};
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

/*
- doubly linked list to store LRU order
    - node contains value
    - O(1) insertion and removal
- hashmap for store key and index into list
    - O(1) access
*/