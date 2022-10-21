from pydoc import describe
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    name = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob',
            'reason','guardian','traveltime','studytime','failures','schoolsup','famsup',
            'paid','activities','nursery','higher','internet','romantic',
            'famrel','freetime','goout','Dalc','Walc','health','absences','G1,G2,G3']
    describ = ["student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)",
               "student's sex (binary: 'F' - female or 'M' - male)",
               "student's age (numeric: from 15 to 22)",
               "student's home address type (binary: 'U' - urban or 'R' - rural)",
               "family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)",
               "parent's cohabitation status (binary: 'T' - living together or 'A' - apart)",
               "mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)",
               "father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)",
               "mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')",
               "father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')",
               "reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')",
               "student's guardian (nominal: 'mother', 'father' or 'other')",
               "home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)",
               "weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)",
               "number of past class failures (numeric: n if 1<=n<3, else 4)",
               "extra educational support (binary: yes or no)",
               "family educational support (binary: yes or no)",
               "extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)",
               "extra-curricular activities (binary: yes or no)",
               "attended nursery school (binary: yes or no)",
               "wants to take higher education (binary: yes or no)",
               "Internet access at home (binary: yes or no)",
               "with a romantic relationship (binary: yes or no)",
               "quality of family relationships (numeric: from 1 - very bad to 5 - excellent)",
               "free time after school (numeric: from 1 - very low to 5 - very high)",
               "going out with friends (numeric: from 1 - very low to 5 - very high)",
               "workday alcohol consumption (numeric: from 1 - very low to 5 - very high)",
               "weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)",
               "current health status (numeric: from 1 - very bad to 5 - very good)",
               "number of school absences (numeric: from 0 to 93)",
               "first,second,final period grade (numeric: from 0 to 20)",
               ]
    number = [i for i in range(1,len(name)+1)]
    info = zip(number,name,describ)
    return render(request, 'index.html', {'info':info})

def graph_view(request):
    name = ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob',
            'reason','guardian','traveltime','studytime','failures','schoolsup','famsup',
            'paid','activities','nursery','higher','internet','romantic',
            'famrel','freetime','goout','Dalc','Walc','health','absences','G1,G2,G3']
    idx = int(request.GET['index'])
    image_set = {4,5,9,10,13,14,15,16,17,20,21,22,23,24,27,28,29,30}
    ment = {
        4:['위 그래프는 거리와 성적 증감간의 관계를 보여줍니다.','U는 도시, R은 농촌을 뜻합니다.','그래프 상으로 보았을 때, 농촌에 사는 것은 시간이 지남에 따라 수학성적에 부정적인 영향을 끼치는 것을 볼 수 있습니다.'],
        5:['위 그래프는 가족의 규모와 성적 증감간의 관계를 보여줍니다.','GT3는 3명 이상의 가족, LT3는 3명 이하의 가족을 뜻합니다.','그래프 상으로 보았을 때, 3명 이하의 소가족이 수학 성적 향상에 더 도움이 되는 것을 볼 수 있습니다.'],
        9:['위 그래프는 부모님의 직업과 성적간의 관계를 보여줍니다.','Fjob은 아버지의 직업, Mjob은 어머니의 직업을 보여줍니다.','일단 확실한 건, 부모님이 집에 계시는 상황이 아이들의 성적에 좋은 영향을 못 준다는 것을 알 수 있습니다','그리고 건강 관련 직업군에 부모님이 종사하시는 경우 성적이 안정적인 것을 볼 수 있습니다.'],
        10:['위 그래프는 부모님의 직업과 성적간의 관계를 보여줍니다.','Fjob은 아버지의 직업, Mjob은 어머니의 직업을 보여줍니다.','일단 확실한 건, 부모님이 집에 계시는 상황이 아이들의 성적에 좋은 영향을 못 준다는 것을 알 수 있습니다','그리고 건강 관련 직업군에 부모님이 종사하시는 경우 성적이 안정적인 것을 볼 수 있습니다.'],
        13:['위 그래프는 집-학교간의 거리와 성적간의 관계를 보여줍니다.','거리에 따른 성적 변화에는 큰 관계가 없는 것으로 보입니다.'],
        14:['위 그래프는 공부시간과 성적간의 관계를 보여줍니다.','공부 시간이 늘어남에 따라 성적이 증가하기보단 떨어지는 모습을 볼 수 있습니다.','일반적인 상식과 반대로 가는 경향으로 보아, 데이터 수집 과정에 대해 알아보아야 할 것으로 보입니다.'],
        15:['위 그래프는 낙제 횟수와 성적간의 관계를 보여줍니다.','낙제 횟수에 따른 성적 변화는 경향성이 없는 것으로 보입니다.'],
        16:['위 그래프는 학교 외 추가수업을 받는 것과 성적 간의 관계를 보여줍니다.','교외에서 추가적인 수업을 받는 것이 성적 향상에 도움이 되는 것이 확연하게 드러납니다.'],
        17:['위 그래프는 가정에서 추가수업을 받는 것과 성적 간의 관계를 보여줍니다.','가정에서 추가적인 수업을 받는 것은 오히려 부정적인 영향을 끼치는 것으로 보입니다.','하긴.. 집까지 와서 부모님이 공부를 시키면 안하는 것만 못한 효과가 나올 법도 합니다'],
        20:['위 그래프는 보육원을 다닌 것과 성적간의 관계를 보여줍니다.','보육원을 다니나 안다니나 큰 차이가 없는 것으로 보입니다.'],
        21:['위 그래프는 고등 교육을 원하는 것과 성적간의 관계를 보여줍니다.','고등 교육을 원하는 학생이 상대적으로 성적이 안정적인 것으로 보입니다.','성취도에 대한 욕심이 있을수록 성적에 긍정적인 영향을 끼치는 것으로 볼 수 있겠습니다.'],
        22:['위 그래프는 인터넷 유무와 성적간의 관계를 보여줍니다.','인터넷이 없는 것이 성적에 부정적인 영향을 끼치는 것으로 보입니다.','인터넷을 통해 얻을 수 있는 여러가지 교육 서비스를 못받게 되는 부분 때문으로 예상됩니다.'],
        23:['위 그래프는 연애와 성적간의 관계를 보여줍니다.', '연애를 하는 학생은 좋은 성적을 기대하기는 힘들어 보입니다.','하지만 학생 시절, 연애를 할 기회가 와도 성적때문에 하지 않는 사람이 얼마나 있을까요?'],
        24:['위 그래프는 가족관계 정도와 성적간의 관계를 보여줍니다.','1~5까지 관계가 좋을수록 높은 점수입니다.','둘 사이의 상관관계는 크게 드러나지 않는 것으로 보입니다.','2번이 높게 나온 것에 대해 약간의 비약으로 덧붙여보면','인과관계가 반대인 것으로 추정됩니다. 성적이 좋지 않게 나올수록 부모님과의 관계가 안좋아질수 있기 때문입니다. 그래서 중간보다는 안좋은 쪽으로 고르고','그렇다고 매우 사이가 안좋다고 할 정도는 아니기에 2번에서 그친 것이 아닐까라는 생각이 들었습니다'],
        27:['위 그래프는 일별 주량, 주별 주량과 성적간의 관계를 보여줍니다','Dalc은 일별 주량, Walc은 주별 주량, 1-5까지 스스로 생각하는 마시는 정도를 나타냅니다. 많다고 생각할수록 큰 숫자를 고릅니다.','주량이 적을수록 오히려 성적이 떨어지고 주량이 늘수록 성적이 올라가는 신기한 양상입니다.','물론 떨어지지 않는 정도이기에 술을 마시는 것이 성적 증가에 도움이 되진 않습니다.','하지만 스트레스 해소나 이외의 약간의 긍정적인 효과가 있다는 부분 정도는 있는 것으로 보아야 할 것입니다.'],
        28:['위 그래프는 일별 주량, 주별 주량과 성적간의 관계를 보여줍니다.','Dalc은 일별 주량, Walc은 주별 주량, 1-5까지 스스로 생각하는 마시는 정도를 나타냅니다. 많다고 생각할수록 큰 숫자를 고릅니다.','주량이 적을수록 오히려 성적이 떨어지고 주량이 늘수록 성적이 올라가는 신기한 양상입니다.','물론 떨어지지 않는 정도이기에 술을 마시는 것이 성적 증가에 도움이 되진 않습니다.','하지만 스트레스 해소나 이외의 약간의 긍정적인 효과가 있다는 부분 정도는 있는 것으로 보아야 할 것입니다.'],
        29:['위 그래프는 건강과 성적간의 관계를 보여줍니다.','전박적으로 상관관계가 없어 보이긴 합니다.','하지만 건강이 매우 좋지 않은 학생의 성적이 높게 나온 부분을 생각해보았을 때,','1점의 학생 수가 적은 것이 원인이 되는 것 같습니다.'],
        30:['위 그래프는 결석 횟수와 성적간의 관계를 보여줍니다.','결석 횟수와 성적간의 상관관계는 크게 없는것으로 보입니다.'],
    }
    if idx in image_set:
        return render(request,'graph.html',{'index':idx,'ment':ment[idx],'name':name[idx]})
    else:
        return render(request,'blank.html')
        
    # coffee_all = Coffee.objects.all()
    # # 만약 request가 POST라면
    #     # POST를 바탕으로 Form을 완성하면
    #     # Form이 유효하면 저장
    # if request.method == 'POST':
    #     form = CoffeeForm(request.POST) # 완성된 FOrm
    #     if form.is_valid(): # 채워진 Form이 유효하다면
    #         form.save() # Form내용을 Model에 저장
    
    # form =  CoffeeForm()
    return render(request,'coffee.html',{'index':idx})


def code_view(request):
    return 

