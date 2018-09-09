##DECISION TREE CLASSIFIER

#Training Data Set
training_data =[
    ['Red',2,2013,'Flower1'],
    ['Red',2,1993,'Flower1'],
    ['Green',3,765,'Flower2'],
    ['Blue',4,346,'Flower3'],
    ['Blue',4,323,'Flower3'],
    ['Green',3,766,'Flower2']
    ]

#Labels
header = ['colour','radius','leaves','label']

#Find possible values of each feature
def uniq_val(rows,col):
    return list(set(row[col] for row in rows))

#Count the occurance of label
def label_occurance(rows):
    counts = {}
    l = [row[-1] for row in rows]
    s = ''.join(l)
    l = uniq_val(rows,-1)
    for i in range(len(l)):
        counts[l[i]] = s.count(l[i])
    return counts

#Is_value
def is_numeric(value):
    return isinstance(value,int)

#question making
class Question:

    def __init__(self,column,value):
        self.c = column
        self.v = value

    def match(self, example):
        val = example[self.v]
        if is_numeric(val):
            return val >= self.v
        else:
            return val == self.v

    def __repr__(self):
        condition = "=="
        if is_numeric(self.v):
            condition = ">="
        return "Is %s %s %s?" % (header[self.c],condition,str(self.v))
    

#Partition of dataset
def partition(rows,question):
    true_row, false_row = [],[]
    for row in rows:
        if question.match(row):
            true_row.append(row)
        else:
            false_row.append(row)
    return true_row,false_row


#Gini_impurityfor row
def gini(rows):
    counts = label_occurance(rows)
    impurity = 1
    for lebel in counts:
        prob_of_lebel = counts[lebel] / float(len(rows))
        impurity -= prob_of_lebel**2
    return impurity

#Information Gain function
def info_gain(left,right,current):
    p = float(len(left)) / (len(left) + len(right))
    return current-p*gini(left)+(1-p)*gini(right)


def find_best_qus(rows):
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  

    for col in range(n_features):  

        values = uniq_val(rows,col) 
        for val in values:  # for each value

            question = Question(col, val)

            
            true_rows, false_rows = partition(rows, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

           
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


class Leaf:
    
    def __init__(self, rows):
        self.predictions = class_counts(rows)

class Decision_Node:

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows):
    gain, qus = find_best_qus(rows)
    if gain == 0:
        return Leaf(rows)

    right_rows, worng_rows = partition(rows, qus)
    right_rows = buil_tree(right_rows)

    wrong_rows = buil_tree(wrong_rows)
    return Decision_Node(qus, right_rows, wrong_rows)

def print_tree(node, spacing=""):
    
    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print (spacing + str(node.question))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


def classify(row,node):

    if isinstance(node, Leaf):
        return node.predictions

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lebel in counts.keys():
        probs[lebel] = str(int(counts[lebel] / total * 100)) + "%"
    return probs


# Evaluate
testing_data = [
    ['Red',2,2013,'Flower1'],
    ['Red',2,1993,'Flower1'],
    ['Green',3,765,'Flower2'],
    ['Blue',4,346,'Flower3'],
    ['Blue',4,323,'Flower3'],
    ['Green',3,766,'Flower2']
    ]

for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], print_leaf(classify(row, build_tree(testing_data)))))
