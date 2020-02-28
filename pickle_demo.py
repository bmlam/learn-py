""" demonstrate the power of pickle, a module to persist runtime structured data to file and get the structured data back into memory
"""
import pickle
fh = open("data.pkl","bw")
programming_languages = ["Python", "Perl", "C++", "Java", "Lisp"]
python_dialects = ["Jython", "IronPython", "CPython"]
pickle_object = (programming_languages, python_dialects)
pickle.dump(pickle_object,fh)
fh.close()
"""The pickled data from the previous example, - i.e. the data which we have written to the file data.pkl, - can be separated into two lists again, when we read back in again the data:
"""
import pickle
f = open("data.pkl","rb")
(languages, dialects) = pickle.load(f)
print(languages, dialects)
""" output:
['Python', 'Perl', 'C++', 'Java', 'Lisp'] ['Jython', 'IronPython', 'CPython']
""" 
