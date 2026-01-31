import re

def email_chain_count(subject):

    pattern = "fw:|fwd:|re:"
    count = re.findall(pattern, subject, flags=re.IGNORECASE)

    return len(count)

if __name__ == "__main__":

    print(email_chain_count("Re: Meeting Notes"))
    print(email_chain_count("Meeting Notes"))
    print(email_chain_count("Re: re: RE: rE: Meeting Notes"))
    print(email_chain_count("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"))