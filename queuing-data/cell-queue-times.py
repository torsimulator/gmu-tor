
import sys
def timeInSeconds(str_time):
	split_time = str_time.split(':');
	
	time_in_secs = split_time[0]*3600 + split_time[1]*60 + split_time[2] #+ split_time[3]*(10**(-9));
	return split_time;

arg = sys.argv
#file = open(arg[1],'r')		# Cell Tracking log of one circuit downloading one file
start_time = "00:12:02:12010" #arg[2]			# Download start time in seconds

time_in_secs = timeInSeconds(start_time);
time_in_secs
#file.close()





# log_time={}
# start_time = 1200
# download_time = 3
# end_time = start_time + download_time
# count = 0
# max_cells = 200;
# unaccounted_cells = 0

# for line in file:
# 	# print line
# 	if line.find("CELL_TRACK") != -1 & line.find("tor-message") != -1:
# 		cell_id = line.split('unique_id=')[1].split(' ')[0]
# 		part=line.split('[')
# 		time = part[5].split(']')[0]
# 		experiment_time = int(part[6].split(']')[0])
# 		# print cell_id
# 		# print time
# 		if (experiment_time >= start_time) &(experiment_time <= end_time):
# 			if (line.find("CREATE_CELL_RELAY")!=-1) & (line.find("exit")!=-1) & (max_cells > 0):
# 				log_time[cell_id] = time + " "
# 				# max_cells -= 1

# 			else:
# 				if (cell_id in log_time):
# 					if(len(log_time[cell_id].split(' ')) <= 7):
# 						log_time[cell_id] += time +" "
# 		else:
# 			if (experiment_time < start_time):
# 				unaccounted_cells +=1


# 		# print queue_time
# 		# count += 1
# 		# if count == 7:
# 		# 	break

# queuing_time_in_relay={}
# iterator = iter(log_time)

# # print log_time["07AE12D8"]
# # print len(log_time)
# # print unaccounted_cells
# # print log_time
# # quit()
# output_file =open("non-zero-queue-times-log.csv","a")

# relay_queue_counter = [0,0,0]		#EXIT,MIDDLE,ENTRY
# while count < len(log_time):
# 	cell_id=next(iterator)
# 	parts = log_time[cell_id].split(' ')
# 	if len(parts) != 8: 
# 		print "The log time of "+cell_id+" is not in the expected format!!"
# 		count +=1
# 		continue

# 	queuing_time_in_relay[cell_id]=""
# 	for i in (1,3,5):
# 		x=int(parts[i+1]) - int(parts[i])
# 		if (x > 0):
# 			log_str= str(count)+","+cell_id +","+ str((i-1)/2) +","+parts[i] +","+ parts[i+1]+","+str(x)+"\n"
# 			output_file.write(log_str)
# 			relay_queue_counter[(i-1)/2] +=x

# 		queuing_time_in_relay[cell_id] += str(x)+" "

# 	count += 1
# print "Exit={0[0]} Middle={0[1]} Entry={0[2]}".format(relay_queue_counter)

