# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:20:46 2016

@author: adil.alim
"""

import cPickle, gzip, numpy
import theano
import theano.tensor as T
import numpy

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
#print cPickle.load(f)
train_set, valid_set, test_set = cPickle.load(f)
print train_set[0],train_set[1],len(train_set[0][0])
print test_set[0],test_set[1],len(test_set[0][0])
f.close()

def shared_dataset(data_xy):
    """ Function that loads the dataset into shared variables

    The reason we store our dataset in shared variables is to allow
    Theano to copy it into the GPU memory (when code is run on GPU).
    Since copying data into the GPU is slow, copying a minibatch everytime
    is needed (the default behaviour if the data is not in a shared
    variable) would lead to a large decrease in performance.
    """
    data_x, data_y = data_xy
    shared_x = theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX))
    shared_y = theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX))
    # When storing data on the GPU it has to be stored as floats
    # therefore we will store the labels as ``floatX`` as well
    # (``shared_y`` does exactly that). But during our computations
    # we need them as ints (we use labels as index, and if they are
    # floats it doesn't make sense) therefore instead of returning
    # ``shared_y`` we will have to cast it to int. This little hack
    # lets us get around this issue
    return shared_x, T.cast(shared_y, 'int32')

test_set_x, test_set_y = shared_dataset(test_set)
valid_set_x, valid_set_y = shared_dataset(valid_set)
train_set_x, train_set_y = shared_dataset(train_set)
#print test_set_x.get_value()

a=T.neq(theano.shared(numpy.asarray([1,2,3,4,5], dtype=theano.config.floatX)), train_set_y[:4])
print a.eval
y=test_set_y[:]
print '---',y

batch_size = 500    # size of the minibatch

# accessing the third minibatch of the training set

data  = train_set_x[2 * batch_size: 3 * batch_size]
label = train_set_y[2 * batch_size: 3 * batch_size]
print data
#zero_one_loss = T.sum(T.neq(T.argmax(p_y_given_x), y))