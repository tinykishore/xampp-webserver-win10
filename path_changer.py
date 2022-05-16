# Automated XAMPP target-directory changer

import sys
args = sys.argv

if len(args) != 2:
    print("Invalid Parameter")
    exit(-1)

target = args[1]
destination_path = "C:\\xampp\\apache\\conf\\extra\\"
destination_file = "C:\\xampp\\apache\\conf\\extra\\httpd-vhosts.conf"
file = open(destination_file, "w")
file.write("# File Generated by Python Script\n")
file.write("<Directory " + target + ">\n")
file.write("\tOptions Indexes FollowSymLinks MultiViews\n\t"
           "AllowOverride all\n\tOrder Deny,Allow\n\t"
           "Allow from all\n\tRequire all granted\n</Directory>\n")
file.write("<VirtualHost *:80>\n\tDocumentRoot " + target +
           "\n\tServerName localhost\n</VirtualHost>")
file.close()
