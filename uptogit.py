import os
os.chdir( os.path.abspath(os.getcwd()) )

# os.system('git add --all -- :!uptogit.py')

os.system('git add . -f uptogit.py')
# os.system('git add -A ":!uptogit.py"')
# os.system('git reset -- uptogit.py')
# os.system('git add -p . :^uptogit.py')
os.system('git commit -m ",,"')
os.system('git pull')
os.system('git push')
# os.system('git branch -M main')
# os.system('git remote add origin "https://github.com/dtbao20/py-unikey.git"')
# os.system('git push -u origin main')


# os.system('git init')
# os.system('git add .')
# os.system('git reset -- uptogit.py')
# os.system('git reset -- uptogit.py')
# os.system('git add --all -- :!path/to/file1 :!path/to/file2 :!path/to/folder1/*')
# os.system('git commit -m "%s"' % ",,")
# os.system('git branch -M main')
# os.system('git remote add origin ""https://github.com/xxx/xxx.git')
# os.system('git push -u origin main')