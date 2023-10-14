import statistics

# Initialize an empty list to store the extracted AUC values
FPSs=[20,50,125,250,500]
all_auc_values = {}


for FPS in FPSs:
    # Script to extract AUC values from text file
    file_path = f'/home/test4/code/EventBenchmark/lib/pytracking/pytracking/analysis/JieChuExp_11trackers_{FPS}fps.txt'  # replace with the path to your file
    
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read lines from file
        lines = file.readlines()    

    tracker_auc={}
    tracker_name=""
    # Iterate over each line in the file
    for line in lines:
        # Split the line into words
        words = line.split('|')

        if len(words) >= 2 and words[0].strip()!="esot500s":            
            if words[0].strip()!=tracker_name:
                tracker_name=words[0].strip()
                tracker_auc[tracker_name]=[]
            tracker_auc[tracker_name].append(float(words[1].strip()))
        else:
            continue
    
    all_auc_values[FPS]=tracker_auc


all_means={}
all_variances={}
all_means_change_rate={}
all_means_change_magnitude={}
all_variances_change_rate={}
all_variances_change_magnitude={}

for FPS in FPSs:
    means={}
    variances={}
    means_change_rate={}
    means_change_magnitude={}
    variances_change_rate={}
    variances_change_magnitude={}

    for tracker_name in all_auc_values[FPS].keys():
        means[tracker_name]=statistics.mean(all_auc_values[FPS][tracker_name])
        variances[tracker_name]=statistics.variance(all_auc_values[FPS][tracker_name])
        
        if FPS!=FPSs[0]:
            last_FPS=FPSs[FPSs.index(FPS)-1]
            means_change_magnitude[tracker_name]=means[tracker_name]-all_means[last_FPS][tracker_name]
            means_change_rate[tracker_name]=means_change_magnitude[tracker_name]/all_means[last_FPS][tracker_name]*100
            variances_change_magnitude[tracker_name]=variances[tracker_name]-all_variances[last_FPS][tracker_name]
            variances_change_rate[tracker_name]=variances_change_magnitude[tracker_name]/all_variances[last_FPS][tracker_name]*100

    all_means[FPS]=means
    all_variances[FPS]=variances
    all_means_change_rate[FPS]=means_change_rate
    all_means_change_magnitude[FPS]=means_change_magnitude
    all_variances_change_rate[FPS]=variances_change_rate
    all_variances_change_magnitude[FPS]=variances_change_magnitude


def print_statistics(all_means, all_variances, all_means_change_rate, all_means_change_magnitude, all_variances_change_rate, all_variances_change_magnitude):
    fps_values = all_means.keys()
    
    print('='*140)
    # Printing means
    print("\nMeans:")
    for fps in fps_values:
        print(f"\nFPS: {fps}")
        for tracker_name, mean_value in all_means[fps].items():
            print(f"{tracker_name:<15}: {mean_value:.2f}")
    
    print('='*140)
    # Similar blocks for other dictionaries
    print("\nVariances:")
    for fps in fps_values:
        print(f"\nFPS: {fps}")
        for tracker_name, variance_value in all_variances[fps].items():
            print(f"{tracker_name:<15}: {variance_value:.2f}")

    print('='*140)
    print("\nMeans Change Rate:")
    for fps in fps_values:
        print(f"\nFPS: {fps}")
        for tracker_name, change_rate_value in all_means_change_rate[fps].items():
            print(f"{tracker_name:<15}: {change_rate_value:.2f}")

    print('='*140)
    print("\nMeans Change Magnitude:")
    for fps in fps_values:
        print(f"\nFPS: {fps}")
        for tracker_name, change_magnitude_value in all_means_change_magnitude[fps].items():
            print(f"{tracker_name:<15}: {change_magnitude_value:.2f}")

    print('='*140)
    print("\nVariances Change Rate:")
    for fps in fps_values:
        print(f"\nFPS: {fps}")
        for tracker_name, var_change_rate_value in all_variances_change_rate[fps].items():
            print(f"{tracker_name:<15}: {var_change_rate_value:.2f}")

    print('='*140)
    print("\nVariances Change Magnitude:")
    for fps in fps_values:
        print(f"\nFPS: {fps}")
        for tracker_name, var_change_magnitude_value in all_variances_change_magnitude[fps].items():
            print(f"{tracker_name:<15}: {var_change_magnitude_value:.2f}")
    
    print('='*140)

# Call the function with the dictionaries
print_statistics(all_means, all_variances, all_means_change_rate, all_means_change_magnitude, all_variances_change_rate, all_variances_change_magnitude)



def cal_statistic_info(FPS1,FPS2):
    means,variances,means_change_magnitude,variances_change_magnitude,means_change_rate,variances_change_rate={},{},{},{},{},{}
    means[FPS1]=all_means[FPS1]
    means[FPS2]=all_means[FPS2]
    variances[FPS1]=all_variances[FPS1]
    variances[FPS2]=all_variances[FPS2]
    for tracker_name in all_means[FPSs[0]].keys():
        means_change_magnitude[tracker_name]=means[FPS2][tracker_name]-means[FPS1][tracker_name]
        means_change_rate[tracker_name]=means_change_magnitude[tracker_name]/means[FPS1][tracker_name]*100
        variances_change_magnitude[tracker_name]=variances[FPS2][tracker_name]-variances[FPS1][tracker_name]
        variances_change_rate[tracker_name]=variances_change_magnitude[tracker_name]/variances[FPS1][tracker_name]*100
    return means,variances,means_change_magnitude,variances_change_magnitude,means_change_rate,variances_change_rate


def print_statistics(FPS1,FPS2,means, variances, means_change_magnitude, variances_change_magnitude, means_change_rate, variances_change_rate):
    # Print the table header
    print(f"{'Tracker Name':<15}{'Means(FPS1)':<15}{'Means(FPS2)':<15}{'Means Change Mag.':<20}{'Means Change Rate':<20}{'Variances(FPS1)':<20}{'Variances(FPS2)':<20}{'Variances Change Mag.':<25}{'Variances Change Rate':<25}")
    print('-'*160)  # Print a line to separate header from data
    
    # Print each row of the table
    for tracker_name in means[FPS1].keys():
        print(f"{tracker_name:<15}{means[FPS1][tracker_name]:<15.2f}{means[FPS2][tracker_name]:<15.2f}{means_change_magnitude[tracker_name]:<20.2f}{means_change_rate[tracker_name]:<20.2f}{variances[FPS1][tracker_name]:<20.2f}{variances[FPS2][tracker_name]:<20.2f}{variances_change_magnitude[tracker_name]:<25.2f}{variances_change_rate[tracker_name]:<25.2f}")
        

while True:
    user_input=input("请输入你要比较的FPS1和FPS2:")
    try:
        FPS1=int(user_input.split()[0])
        FPS2=int(user_input.split()[1])
        if FPS1 not in FPSs or FPS2 not in FPSs:
            raise ValueError 
    except ValueError:
        print("Invalid input:Please enter two integers which are in FPSs.")

    means,variances,means_change_magnitude,variances_change_magnitude,means_change_rate,variances_change_rate=cal_statistic_info(FPS1,FPS2)
    print_statistics(FPS1,FPS2,means, variances, means_change_magnitude, variances_change_magnitude, means_change_rate, variances_change_rate)
    
    comparing=input("是否继续比较？[y/n]：")
    try: 
        if comparing=="y" or comparing=="Y":
            continue
        elif comparing=="n" or comparing=="N":
            break
        else:
            raise ValueError 
    except ValueError:
        print("Invalid input:Please enter 'y' or 'n'.")
