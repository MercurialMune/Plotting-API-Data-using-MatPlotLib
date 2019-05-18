import requests
from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np


def home(request):
    resp = requests.get('https://api.ona.io/api/v1/data/161444')
    respon = resp.json()

    # clean data to remain with keys that you want to plot(psych_knowledge and not_comfortable)
    for i in respon:
        new = [i['psych_knowledge'], i['not_comfortable']]
        i.clear()
        i.update({'psych_knowledge': new[0], 'not_comfortable': new[1]})

    # get the number of entries for the graph
    total_entries = (sum(x.get('psych_knowledge') == 'no' for x in respon)) + (sum(x.get('psych_knowledge') == 'yes' for x in respon))

    # those with or without psychology knowledge
    no_psych_knowledge = sum(x.get('psych_knowledge') == 'no' for x in respon)
    with_psych_knowledge = sum(x.get('psych_knowledge') == 'yes' for x in respon)

    # those comfortable assessing their mental health under a community health worker
    comfortable = sum(x.get('not_comfortable') == 'agree' for x in respon)
    uncomfortable = sum(x.get('not_comfortable') == 'disagree' for x in respon)
    not_sure_comfortable = sum(x.get('not_comfortable') == 'dont_know' for x in respon)

    # plot the graph
    n=3
    noMean=(4,3,1)
    yesMean=(1,1,0)

    fig, ax = plt.subplots()
    index = np.arange(n)
    bar_width = 0.35
    opacity = 0.8

    bar1 = plt.bar(index, noMean, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Those with no mental health awareness')

    bar2 = plt.bar(index + bar_width, yesMean, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Those with mental health awareness')

    plt.ylabel('Mental Health Awareness')
    plt.xlabel('Willingness to Discuss Personal Mental Health')
    plt.title('Effect of mental health awareness in readiness to discuss personal mental health in Kenya')

    plt.xticks(index + bar_width, ('Willing', 'Not Willing', 'Unsure'))
    plt.legend()

    plt.tight_layout()
    # plt.show()
    return render(request, 'index.html', locals())
