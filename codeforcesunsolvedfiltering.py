import urllib.request
import json
import webbrowser

def get_request(method):
    url = "https://codeforces.com/api/"+method
    response = urllib.request.urlopen(url)
    data=json.loads(response.read())
    return data['result']


def submission(handle):
    all_problems=get_request('user.status?handle='+handle+'&from=1&count=100000')
    return all_problems


submit_problems=submission('t17')
submit_problems=submit_problems+submission('a_void')
submit_problems=submit_problems+submission('tanvirtareq')


def myfilter(dicts, key, value):
    ret=[]
    for x in dicts:
        if x[key]==value:
            ret.append(x)
    return ret

solved_problems=myfilter(submit_problems, 'verdict', 'OK')

print(len(solved_problems))

solved=dict()

for x in solved_problems:
    y=x['problem']
    contestid=str(y['contestId'])
    problemindex=str(y['index'])
    url="contest/"+contestid+"/problem/"+problemindex
    
    # if url=="contest/1454/problem/B":
    #     print("autto thik ase")
    solved[url]=1

    # if y['index']=='B':
    #     print(url)
    #     print(solved[url])
    #     print(solved.get(url))
 
# print("ou ses")
contests=get_request('contest.list')
contestidtoname=dict()
for x in contests:
    contestidtoname[x['id']]=x['name']

problems=get_request('problemset.problems?')
problems=problems['problems']


target_problem=[]
problem_a=[]
problem_b=[]
problem_c=[]
problem_d=[]
problem_e=[]
problem_url_a=[]
problem_url_b=[]
problem_url_c=[]
problem_url_d=[]
problem_url_e=[]

for x in problems:
    contestid=x['contestId']
    problemindex=x['index']
    url="contest/"+str(contestid)+"/problem/"+str(problemindex)
    
    if 'Div. 3' in contestidtoname[contestid]:
        continue

    if 'Div. 1' in contestidtoname[contestid]:
        continue

    if 'Div. 4' in contestidtoname[contestid]:
        continue


    
    if (solved.get(url)==None) and ('Div. 2' in contestidtoname[contestid]):
        target_problem.append(x)
        if problemindex=='A':
            problem_a.append(x)
            problem_url_a.append(url)
        
        if problemindex=='B':
            problem_b.append(x)
            problem_url_b.append(url)
            # print(url)
        
        if problemindex=='C':
            problem_c.append(x)
            problem_url_c.append(url)
        
        if problemindex=='D':
            problem_d.append(x)
            problem_url_d.append(url)
        
        if problemindex=='E':
            problem_e.append(x)
            problem_url_e.append(url)


# print(problem_url_a)

# webbrowser.open("https://codeforces.com/"+problem_url_a[0])

file=open('unsolve_a.txt', 'w')
ct=0
for x in problem_url_a:
    file.write(x+'\n')
    ct=ct+1
    if ct>20:
        break
file.close()

file=open('unsolve_b.txt', 'w')
ct=0
for x in problem_url_b:
    file.write(x+'\n')
    ct=ct+1
    if ct>20:
        break
file.close()

file=open('unsolve_c.txt', 'w')
ct=0
for x in problem_url_c:
    file.write(x+'\n')
    ct=ct+1
    if ct>20:
        break
file.close()


file=open('unsolve_d.txt', 'w')
ct=0
for x in problem_url_d:
    file.write(x+'\n')
    ct=ct+1
    if ct>20:
        break
file.close()


file=open('unsolve_e.txt', 'w')
ct=0
for x in problem_url_e:
    file.write(x+'\n')
    ct=ct+1
    if ct>20:
        break
file.close()


# while 1==1:
#     print("give command")
#     query=input()
#     if query=='a' or query=='A':
#         webbrowser.open("https://codeforces.com/"+problem_url_a.pop(0))
#     elif query=='b' or query=='B':
#         webbrowser.open("https://codeforces.com/"+problem_url_b.pop(0))
#     elif query=='C' or query=='c':
#         webbrowser.open("https://codeforces.com/"+problem_url_c.pop(0))
#     elif query=='d' or query=='D':
#         webbrowser.open("https://codeforces.com/"+problem_url_d.pop(0))
#     elif query=='e' or query=='E':
#         webbrowser.open("https://codeforces.com/"+problem_url_e.pop(0))
#     else:
#         break
        

