# In the name of God


import re
from time import sleep
import os


def remove_last_forward_slash(url):
    if url[-1] == "/":
        url = url[:-1]
    return url

def url_to_folder(url):
    domain = find_domain(url)
    _, split_domain = split_protocol_part_of_url(domain)
    split_domain = remove_last_forward_slash(split_domain)
    
    return split_domain.replace(".", "_")

def make_requierd_dir(path, folder):
    requierd_dir = os.path.join(path, folder)
    if not os.path.isdir(requierd_dir):
        os.mkdir(requierd_dir)

def find_domain(url):
    url = url.lower()
    # input shape: https://tarh.ir/golha/ ---> output shape: https://tarh.ir/
    res_url = re.findall(r"^.+?\..+?/", url)
    res_url = res_url[0] if len(res_url) else url

    return res_url

def split_protocol_part_of_url(url):
    splited_with_double_qute_url = url.split(":")
    number_of_parts = len(splited_with_double_qute_url)
    assert number_of_parts <= 2, f"Not a normal link passed. url: {url}"

    protocol_part = splited_with_double_qute_url[0] if number_of_parts == 2 else ""
    url_without_protocol = (
        splited_with_double_qute_url[1] if number_of_parts == 2 else url
    )
    url_without_protocol = (
        url_without_protocol[2:]
        if "//" == url_without_protocol[:2]
        else url_without_protocol
    )

    return protocol_part, url_without_protocol

def read_domains():
    with open('domains.txt', "r") as f:
        d = f.readlines()
    return [remove_last_forward_slash(url.strip()) for url in d]

def write_domains(urls):
    with open('domains.txt', "w") as f:
        f.write("\n".join(urls) + "\n")

def make_url(url, suburl):
    if suburl[:2] == "//":
        protocl, _ = split_protocol_part_of_url(url)
        result = protocl + suburl
    elif suburl[:1] == "/":
        domain = find_domain(url)
        result = domain + suburl
    else:
        result = suburl
    return result
