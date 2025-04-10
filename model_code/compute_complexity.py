import torch

def compute_complexity(paradigm, probabilities):
  N_TENSE, N_NUMBER, N_PERSON, N_GENDER = paradigm.size()
  assert paradigm.size() == probabilities.size()
  # paradigm is a torch tensor of shape (tense present/perfect, number sg/du/pl, persons 1/2/3, gender m/f); its elements are integers
  # probabilities has the same shape, but its elements are floats summing up to 1
  numberOfForms = paradigm.max().item() + 1
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

  marginalProbabilitiesOfForms = (pFormGivenMeaning * probabilities.view(-1).unsqueeze(1)).sum(dim=0)
  complexity = (probabilities.view(-1).unsqueeze(0) * pFormGivenMeaning.t() * ((pFormGivenMeaning+1e-10).t().log() - (marginalProbabilitiesOfForms+1e-10).unsqueeze(1).log())).sum()
  return complexity.item()



if __name__ == "__main__":
  paradigm = torch.zeros(2,3,3,2, dtype=torch.int64)
  paradigm[0,0,1,0] = 3
  paradigm[0,0,0,0] = 2
  paradigm[1,0,0,1] = 1
  probabilities = torch.rand(2,3,3,2).clamp(min=0.01)
  probabilities = probabilities / probabilities.sum()
  print(compute_complexity(paradigm, probabilities))

