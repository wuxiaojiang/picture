from numpy import *
import operator
def classify(inx,dataset,labels,k):
    dataset_size = dataset.shape[0]
    diff_mat = tile(inx,(dataset_size,1))-dataset
    print diff_mat
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sort_distances = distances.argsort()
    print sort_distances
    class_count = {}
    for i in range(k):
        vote_label = labels[sort_distances[i]]
        class_count[vote_label] = class_count.get(vote_label,0)+1
    sorted_class_count = sorted(class_count.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sorted_class_count[0][0]

if __name__ == "__main__":
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    print classify([0,0],group,labels,3)
