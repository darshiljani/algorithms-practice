# Algorithm Name

> **Time complexity :** O(N<sup>2</sup>)

### Steps/Logic

1. Create an iterator over all elements of array
2. Create another iterator going from 0 to length of array - 1 - i (removed i elements from the end due to advantage #2)
3. If the left element is smaller than right element, swap those two
4. Pass complete, start over with step 2 until array is sorted

### When to use

- Reason 1

### Advantages

- Easy to learn
- Last element in each pass is the maximum

### Other notes

- Most basic sorting algorithm
