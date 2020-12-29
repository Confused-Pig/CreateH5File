import h5py
import numpy as np


#write h5py
#model can be replaced 'w',if is 'a',you will don't open the existence file
with h5py.File('datasets/test.h5','a') as f:
    f.create_dataset('test',data=np.array(['test1'.encode(),'test2'.encode()]))
    test_group=f.create_group('test-group')
    f.create_dataset('test1',data=np.array(np.random.randn(5,64,64,3)))
    test_group.create_dataset('testGroup1',data=np.random.randn(64,64,3))
    test_group.create_dataset('testGroup2',data=np.random.randn(64,64,3))


#read h5py
with h5py.File('datasets/test.h5',"r") as f:
    for key in f.keys():
        print(f[key],key,f[key].name)

    test_Group=f['test-group']
    for tkey in test_Group.keys():
        print(tkey,test_Group[tkey],test_Group[tkey].name,test_Group[tkey].value)