import numpy as np


def create_train_data():
    data = np.array([['Sunny', 'Hot', 'High', 'Weak', 'no'],
                     ['Sunny', 'Hot', 'High', 'Strong', 'no'],
                     ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
                     ['Rain', 'Mild', 'High', 'Weak', 'yes'],
                     ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
                     ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
                     ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
                     ['Overcast', 'Mild', 'High', 'Weak', 'no'],
                     ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
                     ['Rain', 'Mild', 'Normal', 'Weak', 'yes']])
    return data

train_data = create_train_data()
print(train_data)

def compute_prior_probability(train_data):
  y_label = np.unique(train_data[:,4])
  result = np.zeros(len(y_label))
  for i in range(len(y_label)):
    result[i] = len(np.where(train_data[:,4] == y_label[i])[0])/len(train_data)
  return result

def compute_conditional_probability(train_data):
  y_label = np.unique(train_data[:,4])
  list_name_feature = []
  conditional_probability = []
  for i in range(train_data.shape[1]-1):
    feature_columns = np.unique(train_data[:,i])
    list_name_feature.append(feature_columns)
    feature_probability = np.zeros((len(feature_columns),len(y_label)))
    for j in range(len(y_label)):
      for k in range(len(feature_columns)):
        feature_probability[k,j] = len(np.where((train_data[:,4] == y_label[j]) & (train_data[:,i] == feature_columns[k]))[0])/len(np.where(train_data[:,4] == y_label[j])[0])
    conditional_probability.append(feature_probability)
  return conditional_probability,list_name_feature

def get_index_from_value(feature_name,list_feature):
  return np.where(list_feature == feature_name)[0][0]

def predict_play_tennis(X,list_x_name,prior_probability,conditional_probability,y_label):
  indexX = []
  p = []
  for i in range(len(X)):
    indexX.append(get_index_from_value(X[i],list_x_name[i]))
  for i in range(len(y_label)):
    temp =prior_probability[i]
    for j in range(len(X)):
      temp*=conditional_probability[j][indexX[j],i]
    p.append(temp)
  print(p)
  return y_label[np.argmax(p)]

X = ['Sunny','Cool','Normal','Weak']
conditional_probability,list_feature = compute_conditional_probability(train_data)
print(predict_play_tennis(X,list_feature,compute_prior_probability(train_data),conditional_probability,np.unique(train_data[:,4])))
