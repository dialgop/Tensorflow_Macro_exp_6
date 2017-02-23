import scipy.io as sp
import numpy as np
import math

#Load data and labels from the file
def loadData(file_name):
    data = sp.loadmat(file_name)    
    train_data = data['trainD']    
    test_data = data['testD']        
    return train_data, test_data
    
def loadLabels(file_name):
    data = sp.loadmat(file_name)
    train_labels = data['trainL']
    z_train_labels = fillZerosMat(train_labels)
    avg_max_labels = data['testL']
    z_avg_max_labels = fillZerosMat(avg_max_labels)
    return z_train_labels, z_avg_max_labels

def fillZerosMat(labels):
    m_val = np.max(labels)    
    x,y = labels.shape
    data_labels = np.zeros((x,m_val)) #m_val corresponds to the maximum number of labels (the maximum number in the label).
    i=0
    while(i<x):
        data_labels[i][labels[i]-1] = 1
        i+=1
    return data_labels
    
def extractValidationData(shuf_data,shuf_label):
    train_size = math.ceil(shuf_data.shape[0]*0.7)
    train_data = shuf_data[0:train_size]
    validation_data = shuf_data[train_size:]
    train_label = shuf_label[0:train_size]
    validation_label = shuf_label[train_size:]
    return train_data,validation_data,train_label,validation_label

def loadAll(dataFileName,labelsFileName,validation=0):
    #If validation = 0 --> returns just 5 data, otherwise it will return 7 data (5+2 of validation tests)
    trainData,testData = loadData(dataFileName)
    trainLabels,testLabels = loadLabels(labelsFileName)
    if validation == 0:
        data = {'trainD': trainData, 'testD': testData}
        labels = {'trainL': trainLabels, 'testL': testLabels}                
    else:        
        data = {'trainD': trainData, 'vldtD': validationData, 'testD': testData}
        labels = {'trainL': trainLabel, 'vldtL': validationLabel, 'testL': testLabels}                        
    return data, labels

def next_batch(array,initial,batch_size):
    
    # ----------------------------------- #
    # Fix this to erase the rows of zeros #
    # ----------------------------------- #    
    
    if(batch_size>array.shape[0]):
        print('The batch amount required is bigger than the size of the batch itself, returning NONE')
        return None
    else:
        fixed_initial = initial%array.shape[0]
        fixed_end = (initial + batch_size)%array.shape[0]
        if(fixed_initial > fixed_end):
            return np.concatenate([array[fixed_initial:],array[0:fixed_end]])
        else:
            return array[fixed_initial:fixed_end]
