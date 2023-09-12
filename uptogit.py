import os
os.chdir( os.path.abspath(os.getcwd()) )

os.system('git add .')
os.system('git reset -- main/uptogit.py')
os.system('git commit -m ",,"')
os.system('git push')



# os.system('git init')
# os.system('git add .')
# os.system('git commit -m "%s"' % ",,")
# os.system('git branch -M main')
# os.system('git remote add origin ""https://github.com/xxx/xxx.git')
# os.system('git push -u origin main')