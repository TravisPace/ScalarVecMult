def scalarMultVec(scalar,vector):
  A = [ ]
  for i in range(len(vector)):
    A.append(vector[i] * scalar)
  return A
