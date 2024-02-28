class RandomizedSet:

    def __init__(self):
        # Initialize a dictionary to store the mapping of elements to their indices,
        # and a list to store the elements.
        self.element_to_index = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        # If the value is not already present in the set, add it.
        if val not in self.element_to_index:
            # Append the value to the list of elements.
            self.elements.append(val)
            # Store the index of the value in the dictionary.
            self.element_to_index[val] = len(self.elements) - 1
            return True  # Return True indicating successful insertion.
        return False  # Return False if value is already present.

    def remove(self, val: int) -> bool:
        # If the value is present in the set, remove it.
        if val in self.element_to_index:
            # Get the index of the value to be removed.
            last_index, current_pos = len(self.elements) - 1, self.element_to_index[val]
            # Replace the value to be removed with the last element in the list.
            self.elements[current_pos] = self.elements[last_index]
            # Update the index of the last element in the dictionary.
            self.element_to_index[self.elements[last_index]] = current_pos
            # Delete the value from the dictionary.
            del self.element_to_index[val]
            # Remove the last element from the list.
            self.elements.pop()
            return True  # Return True indicating successful removal.
        return False  # Return False if value is not present.

    def getRandom(self) -> int:
        # Return a random element from the list of elements.
        return self.elements[random.randint(0, len(self.elements) - 1)]
