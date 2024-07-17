with open('0022_names.txt') as filenames:
    data = filenames.read()
    data = data.replace('"','')
    names = data.split(',')
    sort_names = sorted(names)


    alpha_dict ={}
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for indx,alpha in enumerate(alphas):
        alpha_dict[alpha]=indx+1
    

    def get_score_name(name):
        sum = 0
        for i in name:
            sum += alpha_dict[i]
        return sum


total_sum = 0

for indx,name in enumerate(sort_names):
    total_sum += (indx + 1) * get_score_name(name)
print(total_sum)
