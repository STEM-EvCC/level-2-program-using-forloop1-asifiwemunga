#all of the pregiven mission information 
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
#Basic setup 
total_missions = len(mission_names)
successful_missions = 0
missions_before_2000 = []
# analyzing the missions with a forloop
for x in range(total_missions):
    name = mission_names[x]
    year = mission_years[x]
    success = mission_success[x]
# counting succesfull missions 
    if success: 
        successful_missions += 1 
# collect missions before 2000
    if year < 2000:
        missions_before_2000.append(name)
# calculating success rate 
success_rate = (successful_missions / total_missions) * 100
# output to the console 
print(f"Total number of missions: {total_missions}")
print(f"Number of succesfull missions: {successful_missions}")
print(f"Sucess rate: {success_rate:.2f}%")
print("Missions launched before the year 2000")
for name in missions_before_2000:
    print(f" {name}")