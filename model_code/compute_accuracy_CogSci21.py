import torch

def featureRepresentation(a, b, c, d):
   assert a in [0] # TENSE
   assert b in [0,1] # NUMBER
   assert c in [0,1,2,3] # PERSON
   assert d in [0] # GENDER
   number = b
   person = c
   referents_grid = [["s", "s+o", "s+o+o"], ["NONE", "s+a", "s+a+o"], ["a", "a+o", "a+o+o"], ["o", "o+o", "o+o+o"]]
   if number == 0:
     if person == 0: # first: s
       return torch.FloatTensor([1, 0, 0, 0, 0])
     elif person == 1: # second: a
       return torch.FloatTensor([0, 1, 0, 0, 0])
     elif person == 2: # third: o
       return torch.FloatTensor([0, 0, 1, 0, 0])
     elif person == 3:
       return torch.FloatTensor([0, 0, 0, 0, 0])
   elif number == 1: 
     if person == 0: # s+o+o
       return torch.FloatTensor([1, 0, 1, 1, 1])
     elif person == 1: # a+o+o
       return torch.FloatTensor([0, 1, 1, 1, 1])
     elif person == 2: # o+o+o
       return torch.FloatTensor([0, 0, 1, 1, 1])
     elif person == 3: # s+a+o
       return torch.FloatTensor([1, 1, 1, 1, 1])

def compute_accuracy_CogSci21(paradigm, probabilities, gamma=2):
  N_TENSE, N_NUMBER, N_PERSON, N_GENDER = paradigm.size()
  assert paradigm.size() == probabilities.size()
  # paradigm is a torch tensor of shape (tense present/perfect, number sg/du/pl, persons 1/2/3, gender m/f); its elements are integers
  # probabilities has the same shape, but its elements are floats summing up to 1
  numberOfForms = paradigm.max().item() + 1
  #print(probabilities.sum())
  #print(torch.ones(1))
  assert torch.isclose(probabilities.sum(), torch.ones(1))
  pFormGivenMeaning = torch.zeros(N_TENSE*N_NUMBER*N_PERSON*N_GENDER, numberOfForms)
  for w in range(N_TENSE):
   for i in range(N_NUMBER):
    for j in range(N_PERSON):
      for k in range(N_GENDER):
        pFormGivenMeaning[w*N_NUMBER*N_PERSON*N_GENDER+i*N_PERSON*N_GENDER+j*N_GENDER+k,paradigm[w,i,j,k]] = 1
#  print(pFormGivenMeaning.size(), probabilities.size())
  
  pMeaningGivenForm = (pFormGivenMeaning.t() * probabilities.view(-1))
  pMeaningGivenForm = pMeaningGivenForm / (pMeaningGivenForm.sum(dim=1, keepdim=True) + 1e-10)
#  print(pMeaningGivenForm.size())
  similarity_metric = torch.zeros(N_TENSE*N_NUMBER*N_PERSON*N_GENDER, N_TENSE*N_NUMBER*N_PERSON*N_GENDER)  # similarity_metric[i,j] is the similarity between the meaning of form i and the meaning of form j



  for i in range(N_TENSE*N_NUMBER*N_PERSON*N_GENDER):
    i0, i1, i2, i3 = i//(N_NUMBER*N_PERSON*N_GENDER), (i//(N_PERSON*N_GENDER))%N_NUMBER, (i//N_GENDER)%N_PERSON, i%N_GENDER
    feat1 = featureRepresentation(i0, i1, i2, i3)
    for j in range(N_TENSE*N_NUMBER*N_PERSON*N_GENDER):
      j0, j1, j2, j3 = j//(N_NUMBER*N_PERSON*N_GENDER), (j//(N_PERSON*N_GENDER))%N_NUMBER, (j//N_GENDER)%N_PERSON, j%N_GENDER
      feat2 = featureRepresentation(j0, j1, j2, j3)
      similarity_metric[i,j] = torch.FloatTensor([16, 1, 0.1, 1, 1]).dot((feat1 != feat2).float())
  mental_representations_of_referents = torch.softmax(gamma * similarity_metric, dim=1)

  pMeaningGivenForm = (pMeaningGivenForm.view(numberOfForms, N_TENSE*N_NUMBER*N_PERSON*N_GENDER, 1) * mental_representations_of_referents.view(1, N_TENSE*N_NUMBER*N_PERSON*N_GENDER, N_TENSE*N_NUMBER*N_PERSON*N_GENDER)).sum(dim=1)
#  print(pMeaningGivenForm)


#  print(similarity_metric)
#  print(mental_representations_of_referents)


#  print(mental_representations_of_referents.size(), pMeaningGivenForm.size())
  klDivergence = (mental_representations_of_referents.view(N_TENSE*N_NUMBER*N_PERSON*N_GENDER, 1, N_TENSE*N_NUMBER*N_PERSON*N_GENDER) * torch.log((1e-10 + mental_representations_of_referents.view(N_TENSE*N_NUMBER*N_PERSON*N_GENDER,1,N_TENSE*N_NUMBER*N_PERSON*N_GENDER)) / (1e-10 + pMeaningGivenForm.view(1, numberOfForms, N_TENSE*N_NUMBER*N_PERSON*N_GENDER)))).sum(dim=2)
  averagedKLDivergence = (klDivergence * pFormGivenMeaning * probabilities.view(-1, 1)).sum()
  return averagedKLDivergence.item()
#  print(averagedKLDivergence)



if __name__ == "__main__":
  paradigm = torch.zeros(1,2,4,1, dtype=torch.int64)
  
  paradigm.random_(0,10).round_()
  probabilities = torch.rand(1,2,4,1).clamp(min=0.01)
  probabilities = probabilities / probabilities.sum()
  print(compute_accuracy(paradigm, probabilities))

