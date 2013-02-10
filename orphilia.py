import sys

#generate sys.argv dictionary

####### Orphilia-specific modules
import orphilia

if len(sys.argv) > 1:
	print(sys.argv)
	parameters = sys.argv[2:]
	print parameters
	wtd = sys.argv[1]
else:
	wtd = "brick"

if wtd == "--client":
    orphilia.client.client_verbose(parameters)
	
if wtd == "--client-new":
    orphilia.client.client_new(parameters)

elif wtd == "--client--silent":
    orphilia.client.orphilia_client(parameters)

elif wtd == "--install":
    orphilia.installer.install()

elif wtd == "--uninstall":
    orphilia.installer.uninstall()

elif wtd == "--help":
	print("""\n
	Syntax: orphilia [OPTION] [PARAMETERS]
	
	  --help          - displays this text
	  --monitor       - monitors Dropbox folder activity
	  --configuration - runs configuration wizard
	  --public        - generates public links
	  --install       - installs Orphilia
	  --uninstall     - uninstalls Orphilia
	  --client        - runs Orphilia API Client
	     syntax: orphilia --client '"[parameter1]" "[parameter2]" "[parameter3]"'
	       get    - downloads file from path specified in parameter2 and saves them to \npath specified in parameter3
	       put    - uploads file from path specified in parameter2 to path specified in \nparameter3
	       mv     - moves file from path specified in parameter2 to path specified in \nparameter3
	       cp     - copies file from path specified in parameter2 to path specified in \nparameter3
	       rm     - removes a file (name specified in parameter2)
	       ls     - creates a list of files in directory specified in parameter2 and \nsaves it to file specified in parameter3
	       mkdir  - creates a directory (name specified in parameter2)
	       uid    - updates Orphilia configuration with current accounts Dropbox UID
	""")

elif wtd == "--configuration":
    orphilia.config.config()

elif wtd == "--configuration-haiku":
    orphilia.config.config_gui(parameters)

elif wtd == "--monitor":
    orphilia.monitor.monitor()

elif wtd == "--public":
    orphilia.client.public(parameters)

else:
     print("Invalid syntax. Type orphilia --help for more informations")

