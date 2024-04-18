import socket
import sys
import time
from datetime import datetime

import dns.resolver
import requests
import whois
from cymruwhois import Client

from src.exception import CustomException
from src.logger import logging
from src.url.url_substrings import URLSubStrings


class url_credentials():
    def __init__(self, url: str):
       self.url_substrings = URLSubStrings(url)  #Importing and creating the object of Url Substrings 
       self.url = self.url_substrings.url        #Assigning the URL from URL substring Constructor to the current class
       self.url_domain = self.url_substrings.url_domain()     #Getting the URL domain from the URL SubStrings class
       self.url_path_file = self.url_substrings.url_path_file()
       self.url_parameters = self.url_substrings.url_parameters()
       self.url_directory = self.url_substrings.url_domain()
       #to avoid Path/File and Directory are same.
       if self.url_path_file == self.url_directory:
           self.url_directory = None
        
    def time_response(self):
        try:
            response = requests.get(self.url)
            time_response = response.elapsed.total_seconds()
            
            return time_response
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def domain_spf(self):
        try:
            answers = dns.resolver.resolve(self.url_domain, 'TXT')
            for rdata in answers:
                txt_data = rdata.to_text()
                if "v=spf1" in txt_data:
                    return 1
            return 0
       
        except dns.resolver.NXDOMAIN:
            return 0
       
        except dns.resolver.NoAnswer:
            return 0
       
        except dns.resolver.NoNameservers:
            return 0
       
        except Exception as e:
            raise CustomException(e, sys)
        
    def asn_ip(self):
        try:
            c = Client()
            ip = socket.gethostbyname(self.url_domain)
            for r in c.lookupmany([ip]):
               return(r.asn)
           
        except Exception as e:
            raise CustomException(e, sys)
    
    def time_domain_activation_expiration(self):
        domain_info = whois.whois(self.url_domain)
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        if creation_date and expiration_date:
            # Convert to datetime objects
            if isinstance(creation_date, str):
                creation_date = datetime.strptime(creation_date, "%Y-%m-%d")
            if isinstance(expiration_date, str):
                expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

            # Calculate duration in days
            time_domain_activation = (datetime.now() - creation_date).days
            time_domain_expiration = (expiration_date - datetime.now()).days
        
        return (
            time_domain_activation,
            time_domain_expiration
        )
   
    def qty_ip_resolved(self):
        try:
           ips = socket.getaddrinfo(self.url_domain, None)
           return len(ips)
       
        except socket.gaierror:
            logging.info("Error: Could not resolve hostname.")
            return 0
    
        except Exception as e:
           raise CustomException(e, sys)
       
    def qty_nameservers(self):
        try:
            answers = dns.resolver.resolve(self.url_domain, 'NS')
            return len(answers)
        except dns.resolver.NXDOMAIN:
            print("Error: Domain not found.")
            return 0
        except dns.resolver.NoAnswer:
            print("No nameservers found for", self.url_domain)
            return 0
        except dns.resolver.NoNameservers:
            print("Error: No nameservers found.")
            return 0
        except Exception as e:
            raise CustomException(e, sys)
    
    def qty_mx_servers(self):
        try:
            answers = dns.resolver.resolve(self.url_domain, 'MX')
            return len(answers)
        except dns.resolver.NXDOMAIN:
            print("Error: Domain not found.")
            return 0
        except dns.resolver.NoAnswer:
            print("No nameservers found for", self.url_domain)
            return 0
        except dns.resolver.NoNameservers:
            print("Error: No MX servers found.")
            return 0
        except Exception as e:
            raise CustomException(e, sys)
       
          
if __name__ == "__main__":
    url = url_credentials("https://www.youtube.com/")
    print(url.time_response())
    print(url.domain_spf())
    print(url.asn_ip())
    activation_days, expiration_days = url.time_domain_activation_expiration()
    print(activation_days)
    print(expiration_days)
    print(url.qty_ip_resolved())
    print(url.qty_nameservers())
    print(url.qty_mx_servers())