from bs4 import BeautifulSoup
import subprocess
import os
import time

user = 'username'
password = 'password'
xml_base_url = 'https://jiradc.ext.net.nokia.com/si/jira.issueviews:issue-xml/'

def download_jira_xml(key):
    url = xml_base_url + key + '/' + key +'.xml'
    cur_dir = os.getcwd()
    xml_path = os.path.join(cur_dir, 'data', key+'.xml')
    print(xml_path)
    cmd = 'wget --tries=100  --no-check-certificate --user="{0}" --password="{1}" --auth-no-challenge \"{2}\" -O \"{3}\"'.format(user, password, url, xml_path)
    print(cmd)
    # subprocess.run([cmd], shell=False)
    os.system(cmd)
    parse_all_child_links(key)

def parse_all_child_links(key):
    xml_path = os.path.join(os.getcwd(), 'data', key+'.xml')
    with open(xml_path) as fp:
        soup = BeautifulSoup(fp, 'lxml-xml')
        outlinks = soup.find('outwardlinks')
        if outlinks:
            issuelinks = outlinks.find_all('issuekey')
            if issuelinks:
                for issuelink in issuelinks:
                    print(issuelink.get_text())
                    download_jira_xml(issuelink.get_text())
                    time.sleep(5)


def main():
    key = 'FPB-677417'
    download_jira_xml(key)
    # parse_all_child_links(key)

if __name__ == '__main__':
    main()
