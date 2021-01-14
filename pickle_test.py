import pickle

f = open('features\\features1_answerkeys\\answerkey_index.pkl', 'rb')
g = open('features\\features1_answerkeys\\answerkey_value.pkl', 'rb')

list1 = pickle.load(f)
list2 = pickle.load(g)
print(len(list1))
print(len(list2))
f.close()
g.close()