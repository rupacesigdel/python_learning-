import argparse
import os
import requests

def download(url, output):
    get_response = requests.get(url, stream=True)
    with open(output, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return output

parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of file to download")
parser.add_argument("output", help="Name to save the downloaded file as")

args = parser.parse_args()

download(args.url, args.output)


# parse the arguments
# args = parser.parse_args()

# use the argument in owncode
# print(args.url)
# print(args.output)
# download(args.url, args)

