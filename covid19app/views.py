import json
from django.shortcuts import render
from covidconsumer1.settings import COVID_19_FILE


# Create your views here.
def states(request):
    dict_data = json.loads(open(COVID_19_FILE).read())
    states = [x for x in dict_data]
    states.pop(0)
    return render(request, 'statelist.html', {'states': states})


def districtwise(request, state):
    dict_data = json.loads(open(COVID_19_FILE).read())
    total = [[], [], [], []]
    for x in dict_data[state]['districtData']:
        for k, v in dict_data[state]['districtData'][x].items():
            if k != 'delta' and k != 'notes':
                if k == 'active':
                    total[0].append(v)
                elif k == 'confirmed':
                    total[1].append(v)
                elif k == 'deceased':
                    total[2].append(v)
                else:
                    total[3].append(v)
    # print(total)
    list_of_total = [sum(total[0]), sum(total[1]), sum(total[2]), sum(total[3])]
    return render(request, 'districtwise.html', {'districts': dict_data[state], 'total': list_of_total, 'state':state})
