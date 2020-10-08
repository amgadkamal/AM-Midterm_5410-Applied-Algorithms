import re
def description():
 '''
 Midterm 2020
 Algorithms 5410
 Available jobs with each company, some companies have more than a job, and there are common jobs between companies.
 The user will check the which companies available for his multiple inputs (the desired job or jobs),
 then check the minimum number of companies for his desired jobs and which they are.
 Project by:Amgad Morsy.
 Supervised by: Dr. Jonathan Lee
'''
pass

def process_file(fname, enc):
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()
    return (dat)


def write_results(fname, data, enc):
    with open(fname, 'w', encoding=enc) as file:
        file.write(data)


def words_to_dict(all_words, dictionary):
    for w in all_words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1

#source of set cover functions:http://www.martinbroadhurst.com/greedy-set-cover-in-python.html
def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover

def main():
    unique_words = {}
    words = process_file("final.txt", "utf-8")
    words_to_dict(words, unique_words)
    # ask the user for the desired number of jobs
    Numerofinputs= int(input(" Please enter the number of jobs: "))

    ListOfInputs = []
    ListOfCompaniesAndJobs=[]

    #make list of inputs
    for w in range(Numerofinputs):
        Input_job = input("Please type a job :")
        ListOfInputs.append(Input_job)

    # scan the data for only one time to get a list of both companies and jobs depends on the user inputs
    for eachline in words.splitlines():
         for i in range(Numerofinputs):
           find= re.findall(str(ListOfInputs[i]), eachline)
           if find:
              companyAndJob = list(eachline.split('\t'))
              q = companyAndJob[0:2]
              ListOfCompaniesAndJobs.append(q)

    list1=[]
    list2=[]

    #make a list of sets for the companies that cover each job, "list for each job with companies, then set for all lists"
    for i in range(Numerofinputs):
        for eachjob in ListOfCompaniesAndJobs:
          find = re.findall(str(ListOfInputs[i]), eachjob[0])
          if (find):
            list1.append(eachjob[1])
        list2.append(set(list1[:]))
        list1.clear()
    # to make the set cover step, I will extract only companies form the original list,
    #first step make it flat not list of list
    # then get the company names only
    FlatList = [item for sublist in ListOfCompaniesAndJobs for item in sublist]
    OnlyCompanies=FlatList[1::2]
    universe = set(OnlyCompanies)
    subsets = list2
    cover = set_cover(universe, subsets)
    print("the minimum companies to cover the jobe are", cover)
    print("and the minimum number is",len(str(cover).split(',')))

if __name__ == '__main__':
    print(description.__doc__)
    while True:
      main()

