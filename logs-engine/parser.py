from models import LogEvent
import time,re
class LogParser:
    """
    This class's main responsibility is to parse a log file and split it into lines to feed it to the model to structurise it a bit.
    """
    def __init__(self,log_file_path):
        self.log_file_path=log_file_path
        self.analysed_log_lines={'error_count':0,
                                 'warning_count':0,
                                 'info_count':0,
                                 'passed_endpoints':[],
                                 'total_bytes_sent':0
                                 }
    def read_log(self):
        lines=[]
        start_time=time.time()
        with open(self.log_file_path,"r") as f:
            lines=f.readlines()
        for line_string in lines:
            # print(type(line_string))
            log_line= LogEvent(line_string).get_structured_log()
            self.analyse_log_line(log_line)    
        end_time=time.time()
        self.duration_to_read=end_time-start_time
    
    def analyse_log_line(self,log_line):
        level=log_line['log_level']
        endpoint=log_line['endpoint']
        bytes_sent=log_line['bytes_sent']
        status=log_line['status_code']
        timestamp=log_line['timestamp']
        # Analyse what type of log level we are recieiving for a particular line
        # and note it in the class level dict for a particular file
        if re.search('error',level,re.I):
            self.analysed_log_lines['error_count']+=1
        elif re.search('warn',level,re.I):
            self.analysed_log_lines['warning_count']+1
        elif re.search('info',level,re.I):
            self.analysed_log_lines['info_count']+=1

        # Add the passed endpoints to the class level list
        if status == 200:
            self.analysed_log_lines['passed_endpoints'].append({'timestamp':timestamp,'endpoint':endpoint})
        self.analysed_log_lines['total_bytes_sent']+=bytes_sent
        
    
    def print_result(self):
        print("WELCOME TO LOG ANALYSER ,Here's the results for the file you have entered")
        print("The number of errors that we have encountered are",self.analysed_log_lines['error_count'])
        print("The number of warnings that we have encountered are",self.analysed_log_lines['warn_count'])
        print("The number of info api calls encountered are",self.analysed_log_lines['info_count'])
        print('list of dictionaries containing timestamp and the endpoint of successful hits')
        for record in self.analysed_log_lines['passed_endpoints']:
            print(*(f'{k} : {v}' for k,v in record.items()),sep='\n')

            
    