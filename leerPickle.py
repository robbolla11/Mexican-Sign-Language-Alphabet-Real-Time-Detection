import pickle

dat = pickle.load(open('./data.pickle','rb'))

print(dat.keys())
print(dat)


#Si concuerda con los datos de dataHandLandmarks