[comment]: # "Auto-generated SOAR connector documentation"
# JAMF

Publisher: Splunk Community  
Connector Version: 1\.0\.1  
Product Vendor: jamf  
Product Name: jamf  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

JAMF is a comprehensive enterprise management software for the Apple platform, simplifying IT management for Mac, iPad, iPhone, and Apple TV

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a jamf asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | URL to connect to Jamf service
**username** |  optional  | string | Username, LDAP, or local
**password** |  optional  | password | Password

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[get system info](#action-get-system-info) - Get information about an endpoint  
[get user](#action-get-user) - Get information about a user  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get system info'
Get information about an endpoint

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Computer ID to filter by | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.id | numeric | 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get user'
Get information about a user

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username to filter by | string |  `user name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.username | string |  `user name` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 