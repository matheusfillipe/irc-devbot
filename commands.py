import utils

# Simple commands that detect some regular expression and outputs text
# Useful if there is some keyboard or anything you want to detect in user messages
# and should output plain static text
#FORMAT: regexp: text

INFO_CMDS={
    r"^(.*) linux ": "Do you mean the best OS?",
    r"^(.*) vim ": "Do you mean the best Text editor???",
    "^(.*)!rules(.*)$" : ["1. Let's think about some rules?", "2. Yes I can send multiple messages"],
}


for r in INFO_CMDS:
    @utils.regex_cmd(r)
    def info_cmd(m, regexp=r):
        return INFO_CMDS[regexp]


from urllib.parse import urlparse

@utils.regex_cmd("^what is (.*)")
def what_is(m):
    search_for=m.group(1).split("?")[0]
    sq=search_for.split(" ")
    sq="+".join(sq)
    url="https://lmgtfy.com/?q="+sq
    if utils.validateUrl(url):
        return url


from linkpreview import link_preview

@utils.url_handler()
def url_reader(url):
    utils.debug("Getting preview")
    p = link_preview(url)
    return [f"{p.title}: ", p.description]

