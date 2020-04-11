def estimator(data):
  reportedCases=data['reportedCases']
  # totalHospitalBeds=data['totalHospitalBeds']
  output={"data": {},"impact": {},"severeImpact":{}}
  output['impact']['currentlyInfected']=reportedCases * 10
  output['severeImpact']['currentlyInfected']=reportedCases * 50
  days=28
  if days:
      factor=round(days/3,0)
      estimate_impact=output['impact']['currentlyInfected'] *pow(2,factor)
      output['impact']['infectionsByRequestedTime']=estimate_impact
      estimate_severeimpact=output['severeImpact']['currentlyInfected']* pow(2,factor)
      output['severeImpact']['infectionsByRequestedTime']=estimate_severeimpact
      # impact_=output['impact']['infectionsByRequestedTime'] *0.15
      # severimpact_=output['severeImpact']['infectionsByRequestedTime']*0.15
      # output['impact']['severeCasesByRequestedTime']=impact_
      # output['severeImpact']['severeCasesByRequestedTime']=severimpact_
      # beds_available =round(totalHospitalBeds*0.35,0) 
      # available_hospital_beds_impact=beds_available - output['impact']['severeCasesByRequestedTime']
      # available_hospital_beds_severeImpact= beds_available - output['severeImpact']['severeCasesByRequestedTime']
      # output['impact']['hospitalBedsByRequestedTime']=available_hospital_beds_impact
      # output['severeImpact']['hospitalBedsByRequestedTime']=available_hospital_beds_severeImpact
      # output['data']=data
      # impact_icu=output['impact']['infectionsByRequestedTime'] *0.05
      # severimpact_icu=output['severeImpact']['infectionsByRequestedTime']*0.05
      # output['impact']['casesForICUByRequestedTime']=impact_icu
      # output['severeImpact']['casesForICUByRequestedTime']=severimpact_icu
      # impact_vetilator=output['impact']['infectionsByRequestedTime'] *0.02
      # severimpact_vetilator=output['severeImpact']['infectionsByRequestedTime']*0.02
      # output['impact']['casesForVentilatorsByRequestedTime']=impact_vetilator
      # output['severeImpact']['casesForVentilatorsByRequestedTime']=severimpact_vetilator
      # dollarsInFlight_1=output['impact']['infectionsByRequestedTime'] 
      # dollarsInFlight_2=output['severeImpact']['infectionsByRequestedTime']
      # estimated_money=dollarsInFlight_1*0.85*5*30
      # estimated_money1=dollarsInFlight_2*0.85*5*30
      # output['impact']['dollarsInFlight']=estimated_money
      # output['severeImpact']['dollarsInFlight']=estimated_money1
      final_output={"data":{}, "estimate":{}}
      final_output['data']=data
      final_output['estimate']["impact"]=output["impact"]
      final_output['estimate']["severeImpact"]=output["severeImpact"]
      return final_output
      

  
