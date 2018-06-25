def scalarMultVec(scalar,vector):
  '''
  This function takes a scalar and a vector and multiplies them together.
  '''
  if type(scalar) == list:
    print('error')
    return None
  #If the scalar is a list, then the algorithim will print error and return none.
  A = [ ]
  #A is an empty list.
  for i in range(len(vector)):
    #For the length of the vector.
    A.append(vector[i] * scalar)
    #For each element in length i, multiply by the scalar.
  return A
  #This creates a new list for A and returns A.
