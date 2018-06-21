def scalarMultVec(scalar,vector):
  '''
  This function takes a scalar and a vector and multiplies them together. A is an empty list. For each element in length i, multiply
  by the scalar. This creates a new list for A and returns A.
  '''
  if type(scalar) == list:
    print('error')
    return None
  A = [ ]
  for i in range(len(vector)):
    A.append(vector[i] * scalar)
  return A
