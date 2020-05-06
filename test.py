prog={'JS':'Atom', 'CSharp':'visualStudio','python':['sublime', 'pycharm'],'java':{'JSE':'netbeans','JEE':'Eclispe'}}
{'JS': 'Atom', 'CSharp': 'visualStudio', 'python': ['sublime', 'pycharm'], 'java': {'JSE': 'netbeans', 'JEE': 'Eclispe'}}
print(prog['java'])
{'JSE': 'netbeans', 'JEE': 'Eclispe'}
print(prog['java']['JEE'])
print(prog.get(['java']['jee'],'not found')
print(prog['java']['JEE'])