import webbrowser

print("give command")
q=str(input())

file=open('unsolve_'+q+'.txt', 'r')
rd=file.read().split()
webbrowser.open("https://codeforces.com/"+rd.pop(0))
file.close()

file=open('unsolve_'+q+'.txt', 'w')

for x in rd:
    print(x)
    file.write(x+'\n')
file.close()
