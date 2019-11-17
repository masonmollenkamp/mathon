import urllib
import threading
import queue
threads = 50
target_url = "http://www.jcommunitys.com"
wordlist_file = "C:/Users/Mason Mollenkamp/Desktop/repo/mathon/hackerstuff/allFromSVNDigger.txt" # from SVNDigger
resume = None
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.50 Safari/537.36 Edg/78.0.276.17"

def build_wordlist(wordlist_file):
    # read in the word list
    fd = open(wordlist_file,"rb")
    raw_words = fd.readlines()
    fd.close()

    found_resume = False
    words = queue.Queue()

    for word in raw_words:

        word = word.rstrip()

        if resume is not None:

            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print("Resuming wordlist from: {}".format(resume))

                else:
                    words.put(word)

    return words

def dir_bruter(word_queue,extensions=None):

    while not word_queue.empty():
        attempt = word_queue.get()

        attempt_list = []

        # check to see if there is a file extension; if not,
        # it's a directory path we're bruting
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s" % attempt)

        # if we want to bruteforce extensions
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt,extension))

        # iterate over our list of attempts
        for brute in attempt_list:

            url = "%s%s" % (target_url,urllib.quote(brute))

            try:
                headers = {}
                headers["User-Agent"] = uer_agent
                r = urllib.Request(url,headers=headers)


                response = urllib.urlopen(r)

                if len(response.read()):
                    print("[%d] => %s".format(response.code,url))

            except urllib.URLError as e:
                if hasattr(e, 'code') and e.code != 404:
                    print("!!! %d => %s" % (e.code,url))

        pass

word_queue = build_wordlist(wordlist_file)
extensions = [".php",".bak",".orig",".inc"]
for i in range(threads):
    dir_bruter(word_queue,extensions)