import cognitive_face as CF
from global_variables import personGroupId

Key = 'd238bdf434db4334bac279668f970cd7'
CF.Key.set(Key)

res = CF.person_group.train(personGroupId)
print(res)
