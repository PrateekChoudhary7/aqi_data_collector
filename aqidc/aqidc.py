"""
A simple python datacollector to fetch the AQI data for two cities Bangalore and Delhi using the Python Wrapper for AQICN data built by valentinalexeev.
"""
import pwaqi

def createRowItem(obs):
    valcity=obs['city']['name']
    valtime=obs['time']
    valaqi=obs['aqi']
    valco=valh=valno2=valpm10=valpm25=valso2=valt=''
    for x in obs['iaqi']:
        if x['p']=='co':
            valco=x['v']
            continue
        if x['p']=='h':
            valh=x['v']
            continue
        if x['p']=='no2':
            valno2=x['v']
            continue
        if x['p']=='pm10':
            valpm10=x['v']
            continue
        if x['p']=='pm25':
            valpm25=x['v']
            continue
        if x['p']=='so2':
            valso2=x['v']
            continue
        if x['p']=='t':
            valt=x['v']
            continue
    return [valcity,valaqi,valtime,valco,valh,valno2,valpm10,valpm25,valso2,valt]

token="8a44be330249ff56edb42808dae9a7f12278bd5c"
file_obj=open("C:\\Users\\Prateek\\aqi_data.csv","a")

delcd=pwaqi.findStationCodesByCity('delhi',token)[0]
bancd=pwaqi.findStationCodesByCity('bangalore',token)[0]
delobs=pwaqi.get_station_observation(delcd,token)
banobs=pwaqi.get_station_observation(bancd,token)
delrow=createRowItem(delobs)
banrow=createRowItem(banobs)

file_obj.write("\n'"+str(delrow[0])+"',"+str(delrow[1])+","+str(delrow[2])+","+str(delrow[3])+","+str(delrow[4])+","+str(delrow[5])+","+str(delrow[6])+","+str(delrow[7])+","+str(delrow[8])+","+str(delrow[9]))
file_obj.write("\n'"+str(banrow[0])+"',"+str(banrow[1])+","+str(banrow[2])+","+str(banrow[3])+","+str(banrow[4])+","+str(banrow[5])+","+str(banrow[6])+","+str(banrow[7])+","+str(banrow[8])+","+str(banrow[9]))
