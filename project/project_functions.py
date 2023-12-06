import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def data_processing(location):
    academy_2004_2008 = pd.read_csv(location+"사설학원_및_독서실(2004~2008).csv", index_col=False) # 파일 읽기
    drop_set_for_academy_2004_2008=set(['이수자수 (명)', '강사수 (명)', '직원수 (명)', '강의실수 (개)', '실험실습실수 (개)',
                                    '사무실수 (개)', '독서실수', '열람실수', '열람좌석수', '여', '인문사회', '직업기술', '경영실무'])
    drop_keys_for_academy_2004_2008=['자치구별(1)']

    for year in range(2004, 2009):
        academy_2004_2008.drop(str(year), axis=1, inplace=True)
        for i in range(1,50):
            key=str(year)+'.'+str(i)
            if key in academy_2004_2008 and \
                (academy_2004_2008[key][1] in drop_set_for_academy_2004_2008 or \
                    academy_2004_2008[key][2] in drop_set_for_academy_2004_2008 or \
                        academy_2004_2008[key][1]!='수강자수 (명)' and academy_2004_2008[key][2]=='소계'):
                drop_keys_for_academy_2004_2008.append(key)
    academy_2004_2008.drop(drop_keys_for_academy_2004_2008, axis=1, inplace=True)
    academy_2004_2008.drop(0, axis=0, inplace=True)
    academy_2004_2008.to_csv(location+'academy_2004_2008.csv', encoding="utf-8-sig", index=False)


    academy_2009_2020 = pd.read_csv(location+"서울시_사설학원_통계(2009~2020).csv", index_col=False)
    # 필요없는 columns를 지운다.
    # 독서실, 강사수, 직원수, 실험실습실수, 사무실수 등등
    # 평생직업, 교육학원

    drop_set_for_academy_2009_2020=set(['이수자수 (명)', '강사수 (명)', '직원수 (명)', '강의실수 (개)',  '사무실수 (개)',
           '실험실습실 (개)', '독서실수 (개)', '열람실수 (개)', '열람좌석수 (개)', '여자','평생직업 교육학원', '특수교육'])
    drop_keys_for_academy_2009_2020=['자치구별(1)']
    for year in range(2009, 2021):
        academy_2009_2020.drop(str(year), axis=1, inplace=True)
        for i in range(1,50):
            key=str(year)+'.'+str(i)
            if key in academy_2009_2020 and \
                (academy_2009_2020[key][1] in drop_set_for_academy_2009_2020 or \
                academy_2009_2020[key][2] in drop_set_for_academy_2009_2020 or \
                    academy_2009_2020[key][3] in drop_set_for_academy_2009_2020 or \
                        academy_2009_2020[key][1]!='수강자수 (명)' and academy_2009_2020[key][3]=='소계'):
                drop_keys_for_academy_2009_2020.append(key)
    academy_2009_2020.drop(drop_keys_for_academy_2009_2020, axis=1, inplace=True)
    academy_2009_2020.drop(2, axis=0, inplace=True)
    academy_2009_2020.drop(0,axis=0,inplace=True)

    academy_2009_2020.to_csv(location+'academy_2009_2020.csv', encoding="utf-8-sig", index=False)

    adv_rate_2000_2010 = pd.read_csv(location+"상급학교_진학률(2000~2010).csv", index_col=False)
    # 필요없는 columns를 지운다.
    # 취업자, 기타 등등

    drop_set_for_adv_rate_2000_2010=set(['취업자', '기타', '일반계고', '전문계고', '대학교', '전문대학', '기타'])
    drop_keys_for_adv_rate_2000_2010=['자치구별(1)']
    for year in range(2000, 2011):
        for i in range(1,50):
            key=str(year)+'.'+str(i)
            if key in adv_rate_2000_2010 and \
                (adv_rate_2000_2010[key][0] in drop_set_for_adv_rate_2000_2010 or \
                adv_rate_2000_2010[key][1] in drop_set_for_adv_rate_2000_2010):
                drop_keys_for_adv_rate_2000_2010.append(key)
    adv_rate_2000_2010.drop(drop_keys_for_adv_rate_2000_2010, axis=1, inplace=True)
    adv_rate_2000_2010.drop(1,axis=0, inplace=True)
    adv_rate_2000_2010.to_csv(location+'adv_rate_2000_2010.csv', encoding="utf-8-sig", index=False)

    adv_rate_2011_2020 = pd.read_csv(location+"서울시_상급학교_진학률_통계(2011~2020).csv", index_col=False)
# 필요없는 columns를 지운다.
# 취업자, 기타 등등
# 고등학교 분류 지우기

    drop_set_for_adv_rate_2011_2020=set(['취업자 (명)','기타 (명)'])
    drop_keys_for_adv_rate_2011_2020=['고등학교별(1)' ,'고등학교별(2)','자치구별(1)']
    for year in range(2011, 2021):
        for i in range(1,50):
            key=str(year)+'.'+str(i)
            if key in adv_rate_2011_2020 and (adv_rate_2011_2020[key][0] in drop_set_for_adv_rate_2011_2020):
                drop_keys_for_adv_rate_2011_2020.append(key)
    for i in range(2,117):
        if adv_rate_2011_2020['고등학교별(2)'][i]!='소계':
            adv_rate_2011_2020.drop(i,axis=0,inplace=True)
    adv_rate_2011_2020.drop(drop_keys_for_adv_rate_2011_2020, axis=1, inplace=True)

    adv_rate_2011_2020.to_csv(location+'adv_rate_2011_2020.csv', encoding="utf-8-sig", index=False)



def data_generation(location):
    regions = list(pd.read_csv(location+"academy_2004_2008.csv", index_col=False)['자치구별(2)'][2:])
    academy_dict={'자치구':regions}
    academy_classification=['입시검정학원수', '비입시검정학원수', '수강자수']
    academy_2004_2008 = pd.read_csv(location+"academy_2004_2008.csv", index_col=False)

    for year in range(2004,2021): # dataframe을 초기화
        for c in academy_classification:
            key=str(year)+" "+c
            academy_dict[key]=['0']*26
    academy=pd.DataFrame(academy_dict)  

    # 초기화한 dataframe의 적절한 위치에 데이터를 삽입
    dict_for_academy_2004_2008={'입시검정및보충학습':'입시검정학원수', '예능':'비입시검정학원수', '국제실무':'비입시검정학원수', '소계':'수강자수'}
    for year in range(2004, 2009):
        for i in range(1,50):
            key=str(year)+'.'+str(i)
            if key in academy_2004_2008:
                key2=str(year)+' '+dict_for_academy_2004_2008[academy_2004_2008[key][1]]
                for j in range(26):
                    if academy_2004_2008[key][j+2]=='-':n=0
                    else:n=int(academy_2004_2008[key][j+2])
                    academy[key2][j]=str(int(academy[key2][j])+n)

    academy_2009_2020 = pd.read_csv(location+"academy_2009_2020.csv", index_col=False)
    dict_for_academy_2009_2020={'입시검정 및 보습':'입시검정학원수', '예능':'비입시검정학원수', '국제화':'비입시검정학원수', '기타':'비입시검정학원수', '소계':'수강자수', '종합':'비입시검정학원수'}
    for year in range(2009, 2021):
        for i in range(1,50):
            key=str(year)+'.'+str(i)
            if key in academy_2009_2020:
                key2=str(year)+' '+dict_for_academy_2009_2020[academy_2009_2020[key][1]]
                for j in range(26):
                    if academy_2009_2020[key][j+2]=='-':n=0
                    else:n=int(academy_2009_2020[key][j+2])
                    academy[key2][j]=str(int(academy[key2][j])+n)

    academy.to_csv(location+'academy.csv', encoding="utf-8-sig", index=False)


    adv_rate_dict = {'자치구':regions}
    adv_rate_classification = ['졸업자수', '진학자수', '진학률']
    for year in range(2004,2021): # dataframe을 초기화
        for c in adv_rate_classification:
            key=str(year)+" "+c
            adv_rate_dict[key]=['0']*26
    adv_rate = pd.DataFrame(adv_rate_dict)

    # 초기화한 dataframe의 적절한 위치에 데이터를 삽입
    adv_rate_2000_2010 = pd.read_csv(location+"adv_rate_2000_2010.csv", index_col=False)
    dict_for_adv_rate_2000_2010={'졸업자':'졸업자수', '진학자':'진학자수', '진학률 (%)':'진학률'}
    for year in range(2004, 2011):
        for i in range(50):
            if i==0:key=str(year)
            else:key=str(year)+'.'+str(i)
            if key in adv_rate_2000_2010:
                key2=str(year)+' '+dict_for_adv_rate_2000_2010[adv_rate_2000_2010[key][0]]
                for j in range(26):
                    try:adv_rate[key2][j]=str(int(adv_rate[key2][j])+int(adv_rate_2000_2010[key][j+1]))
                    except:adv_rate[key2][j]=str(float(adv_rate[key2][j])+float(adv_rate_2000_2010[key][j+1]))

    adv_rate_2011_2020 = pd.read_csv(location+"adv_rate_2011_2020.csv", index_col=False)
    dict_for_adv_rate_2011_2020={'졸업자 (명)':'졸업자수', '진학자수 (명)':'진학자수', '진학률 (%)':'진학률'}
    for year in range(2011, 2021):
        for i in range(50):
            if i==0:key=str(year)
            else:key=str(year)+'.'+str(i)
            if key in adv_rate_2011_2020:
                key2=str(year)+' '+dict_for_adv_rate_2011_2020[adv_rate_2011_2020[key][0]]
                for j in range(26):
                    try:adv_rate[key2][j]=str(int(adv_rate[key2][j])+int(adv_rate_2011_2020[key][j+1]))
                    except:adv_rate[key2][j]=str(float(adv_rate[key2][j])+float(adv_rate_2011_2020[key][j+1]))

    adv_rate.to_csv(location+'adv_rate.csv', encoding="utf-8-sig", index=False)


def print_graph(location, font):
    academy = pd.read_csv(location+"academy.csv", index_col=False)
    adv_rate = pd.read_csv(location+"adv_rate.csv", index_col=False)
    regions = list(pd.read_csv(location+"academy_2004_2008.csv", index_col=False)['자치구별(2)'][2:])

    #한글 폰트 설정
    plt.rcParams['font.family'] = font
    plt.rcParams['axes.unicode_minus']=False

    for year in range(2004, 2021):
        bar_width=0.25
        x = np.arange(25)
    
        key=str(year)+" 졸업자수" #졸업자수 
        graduate = adv_rate[key].to_numpy()
        for i in range(26):graduate[i]=int(graduate[i])

        key=str(year)+" 수강자수" #졸업자수 대비 수강자수
        value = academy[key].to_numpy()
        sum_student=int(value[0]) #총 수강자수
        for i in range(26):value[i]=int(value[i])/graduate[i]
        plt.bar(x+0*bar_width, value[1:], bar_width, label='졸업자수 대비 수강자수', alpha=1)

        
        key=str(year)+" 진학자수" # 진학률 (보정)
        value = adv_rate[key].to_numpy()
        rate=sum_student/int(value[0])
        for i in range(26):value[i]=int(value[i])/graduate[i]*rate
        plt.bar(x+1*bar_width, value[1:], bar_width, label='진학률 (보정)', alpha=1)

        plt.xlabel(str(year)+"년")
        plt.xticks(np.arange(bar_width/2, 25+bar_width/2, 1),regions[1:])
        plt.legend()
        plt.show()