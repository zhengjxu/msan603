import os
import json
import sys
    
def extract_json(json_line):
    flag = 0
    name, age = '', ''
    try:
        a_dict = json.loads(json_line)
        # check present
        name, age = a_dict['name'], a_dict['prop']['age']
    except Exception as e:
        print('having error load json line: %s' % e)
        flag = 1
    
    # check non-empty
    if name=='' or age=='': flag=1
    
    return '%s\t%s' % (name, age), flag

def process_file(prefix, input_dir='/srv/runme', output_dir = '/srv/runme'):
    output_file = '%s/%s.txt' % (output_dir, prefix)
    if os.path.exists(output_file): os.remove(output_file)
    
    result = []
    
    files = os.listdir(input_dir)
    files = [f for f in files if f.startswith(prefix)]
    if len(files)==0:
        print('No qualified files')
        return None

    for file in files:
        file_path = input_dir+'/'+file
        print('process %s' % file_path) 
        f = open(file_path)
        for json_line in f:
            json_line = json_line[:-1]
            
            name_age, flag = extract_json(json_line)
            if flag==1: continue
            
            result.append(name_age)
        f.close()
    
    f = open(output_file, 'w')
    f.write('\n'.join(result))
    f.close()
    print('Done!')  

if __name__ == '__main__':
    prefix = sys.argv[1]
    process_file(prefix, '/srv/runme', '/srv/runme')