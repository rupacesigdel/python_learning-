import multiprocessing
import requests

def dowenloadFile(url, name):
    print(f"Start downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"Finished downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photo/200/300"
    pros = []
    for i in range(5):
        # dowenloadFile(url, i)
        p = multiprocessing.Process(target=dowenloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()