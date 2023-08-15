# Linear Search

Algorithm used to check whether a given element exists in an array/list or not.

## Time complexity

**Best Case :** O(1) since it finds the required value on first position in the array

<!-- **Average Case :** O(N) since it loops over N elements of array -->

**Worst Case :** O(N) since it has to loop over all N elements of array

## Steps

1. Create an iterator over given array/list
2. Check on each pass of iterator whether the value equals to required value or not
3. If iterator value matches the required value, return True
4. If no values match the required value, return False

## When to use

- A small array/list is provided

## Advantages

- Simplest algorithm

### Other notes

- Used in built-in methods of multiple languages like **indexOf** (JavaScript).
