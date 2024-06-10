The code first calculates the width and height of the matrix and the total number of elements.
It then builds a map where each key is an index in the original matrix. The corresponding value is a dictionary containing the "new_index" (index after rotation) and the "value" (original value at that index).
The get_new_index function calculates the new position for an element based on its original row and column. It essentially swaps the row and column indices during rotation.
The get_value function retrieves the original value from the matrix using its index.
The main loop iterates through the map, retrieves the original value and its new position.
Finally, it updates the matrix with the original value at its new position.
The build_matrix function is used to create sample matrices for testing.
