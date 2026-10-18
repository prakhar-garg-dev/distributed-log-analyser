import json
class LogEvent:
    """
    What should this class do 
    # It should define a simple Log structure
    # Log can contain data of various type but for simplicity sake for beginning we are defining a simple structure 
    # Log{
    # "timestamp":"2026-10-08T14:44:29.060Z",
    # "level":"ERROR",
    # "method":"DELETE",
    # "path":"/api/v1/users/123",
    # "status":500,
    # "response_time_ms":11,
    # "client_ip":"53.94.181.150",
    # "user_agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    # "request_id":"req_m52kowmwx2o",
    # "bytes_sent":3654}
    # } 
    """
    def __init__(self,log_line):
        self.log_line=log_line
                 
    def get_structured_log(self):
        parsed_log_line=json.loads(self.log_line)
        timestamp=parsed_log_line['timestamp']
        log_level=parsed_log_line['level']
        http_method=parsed_log_line['method']
        endpoint=parsed_log_line['path']
        status_code=parsed_log_line['status']
        bytes_sent=parsed_log_line['bytes_sent']
        return {'timestamp':timestamp,
                'log_level': log_level,
                'http_method': http_method,
                 'endpoint':endpoint,
                 'status_code':status_code,
                 'bytes_sent':bytes_sent
                }
        
        





