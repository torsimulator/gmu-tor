
import sys
def timeInSeconds(str_time):

	split_time = str_time.split(':');

	time_in_secs = int(split_time[0])*3600 + int(split_time[1])*60 + int(split_time[2])+ int(split_time[3])*(10**(-9));
	return float(time_in_secs);

def diffTimeInSeconds (time_1,time_2):
	return (time_1-time_2);

def getUniqueId(line):
	return line.split('unique_id=')[1].split(' ')[0]

def getIndex(track_cell, unique_id):
	for i,x in enumerate(track_cell):
		if(x[0] == unique_id):
			return i;
	return -1;

if __name__ == '__main__':
	arg = sys.argv
	file = open(arg[1],'r')		# Cell Tracking log of one circuit downloading one file
	start_time = float(arg[2])	# Download start time in seconds
	track_cell =[];				#Stores cell queuing and de-queuing times. Format: ['Cell_ID', Exit_Queue, Exit_DeQueue, Middle_Queue, Middle_DeQueue, Entry_Queue, Entry_DeQueue]


	for line in file:
		if(line.find("fg-download-complete")!=-1):								# Download Complete. Need not log cell queuing time of subsequent cells
			break;

		if ((line.find("CELL_TRACK") != -1) & (line.find("tor-message")!=-1)):
			split_entry = line.split(' ');
# 			print(line);
			log_time = timeInSeconds(split_entry[2]);									#Retrieve log time

			if((log_time >= start_time)):												# Log cells after download begins
				unique_id = getUniqueId(line);
				if (line.find("CREATE_CELL_RELAY")!=-1) & (line.find("exit")!=-1):		# A new relay cell is created at the exit node
					track_cell.append([]);
					track_cell[len(track_cell)-1].append(unique_id);

				else:
					if((line.find("CIRC_QUEUE_APPEND")!=-1) | (line.find("CIRC_QUEUE_POP")!=-1)): #Logging Queuing and De-Queuing times.
						cell_index=getIndex(track_cell, unique_id);

						if (cell_index!=-1):
							if ((len(track_cell[cell_index]) < 7)): 					#Ignore duplicate cell ID from client side
								track_cell[cell_index].append(log_time)
# 							else:
# 								break;



# 	print(track_cell)
# 	print(track_cell.__len__())
# 	print(track_cell[0])

# Extracting Cell Queuing Time at Exit, Middle and Entry
	exit_cell_queue_time=[];
	middle_cell_queue_time=[];
	entry_cell_queue_time=[];
	for cell in track_cell:
		exit_cell_queue_time.append((cell[2]-cell[1]));
		middle_cell_queue_time.append((cell[4]-cell[3]));
		entry_cell_queue_time.append((cell[6]-cell[5]));

	avg_exit_cell_queue=sum(exit_cell_queue_time)/exit_cell_queue_time.__len__();
	avg_middle_cell_queue=sum(middle_cell_queue_time)/middle_cell_queue_time.__len__();
	avg_entry_cell_queue=sum(entry_cell_queue_time)/entry_cell_queue_time.__len__();

	print(avg_exit_cell_queue)
	#print (exit_cell_queue_time)
	print(avg_middle_cell_queue)
	#print(middle_cell_queue_time)
	print(avg_entry_cell_queue)
	#print(entry_cell_queue_time)

file.close()
