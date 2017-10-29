
# coding : utf-8

import statistics as ss
import sys
import time

# Fetch parameters

assert len(sys.argv) == 4, 'Miss some parameters!'


input_file_path = sys.argv[1]
output_zip_path = sys.argv[2]
output_date_path = sys.argv[3]

try:
    zip_output_file = open(output_zip_path, 'w')
    date_output_file = open(output_date_path, 'w')

except:
    print('the output file cannot open')
    if zip_output_file is not None:
        zip_output_file.close()
    if date_output_file is not None:
        date_output_file.close()
    sys.exit(1)


zip_data = dict() # CMTE_ID|ZIP_CODE as key
date_data= dict() # CMTE_ID|DATE as key


# Because the round(0.5) = 0, round(-0.5) = 0
# rewrite my own round func
def own_round(x):
    if x == 0.5:
        return 1
    elif x == -0.5:
        return -1
    else:
        return round(x)


# input_file_names = os.listdir(input_file_path)

with open(input_file_path, 'r') as f:
    for line in f:
        
        flag_zip = True
        flag_date = True
        
        data = line.split('|')
        # If Other ID is not none, CMTE_ID is none, Amount is none
        if len(data) != 21:
            continue

        if data[15] or not data[0] or not data[14]:
            continue
        
        # Discard this for zip_data
        if not data[10] or len(data[10]) < 5:
            flag_zip = False
        
        # Discard for date_data
        if not data[13]:
            flag_date = False
        try:
            trans_dt = time.strptime(data[13], '%m%d%Y')
        except:
            flag_date = False
        
        if flag_zip:
            key = data[0] + '|' + data[10][0:5]
            if key not in zip_data:
                zip_data[key] = [1, [int(data[14])]]
            else:
                zip_data[key][0] += 1
                zip_data[key][1] += [int(data[14])]
            cur_sum = sum(zip_data[key][1])
            
            # Reason why not using round rather than int(num+0.5) is round func sometimes up, sometimes down
            cur_median = own_round(ss.median(zip_data[key][1]))

            cur_time = zip_data[key][0]
            
            # Write to the zip output file
            zip_output_file.write(key + '|' + str(cur_median) + '|' + str(cur_time) + '|' + str(cur_sum) + '\n')
            
        if flag_date:
            key = data[0] + '|' + data[13]
            if key not in date_data:
                date_data[key] = [1, [int(data[14])]]
            else:
                date_data[key][0] += 1
                date_data[key][1] += [int(data[14])]

def comp(x):
    x = x.split('|')
    x[1] = time.strptime(x[1], '%m%d%Y')
    return x[0], x[1]
                
for key in sorted(date_data, key=comp):
    value = date_data[key]
    cur_sum = sum(value[1])
    cur_median = own_round(ss.median(value[1]))
    cur_time = value[0]
    date_output_file.write(key + '|' + str(cur_median) + '|' + str(cur_time) + '|' + str(cur_sum) + '\n')



zip_output_file.close()
date_output_file.close()

print('------------------Finished------------------')




