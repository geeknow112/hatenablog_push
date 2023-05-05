from datetime import datetime
import requests as req

'''
HATENA_ID = "yourenemy"
BLOG_DOMAIN = "tradehack.hatenablog.com"
API_KEY = "crxm68ghqj"
BASE_URL = f"https://blog.hatena.ne.jp/{HATENA_ID}/{BLOG_DOMAIN}/atom"
'''
HATENA_ID = "yourenemy"
BLOG_DOMAIN = "cashhack.hatenablog.com"
API_KEY = "crxm68ghqj"
BASE_URL = f"https://blog.hatena.ne.jp/{HATENA_ID}/{BLOG_DOMAIN}/atom"

def hatena_entry(title, content, categorys=[], custom_url=None, updated="", draft=True):
    """はてなブログへの投稿
    Attributes:
        HATENA_ID, API_KEY, BASE_URL (str)

    Args:
        title (str):
        content (str):
        categorys (List[str]):
        updated (str): %Y-%m-%dT%H:%M:%S
        draft (bool):

    Returns:
        str: xml
    """
    updated = updated if updated else datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    # draft = "yes" if draft else "no"
    draft = "no" # 即公開
    category = lambda x: "\n".join([f"<category term='{e}' />" for e in x])
    categorys = category(categorys) if category else ""

    print(custom_url)
    # カスタムURLを設定
    if custom_url:
        custom_url_xml = f"""<hatenablog:custom-url xmlns:hatenablog="http://www.hatena.ne.jp/info/xmlns#hatenablog">{custom_url}</hatenablog:custom-url>"""
    else:
        custom_url_xml = ""

    xml = f"""<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom" xmlns:app="http://www.w3.org/2007/app">
        <title>{title}</title><author><name>name</name></author>
        <content type="text/markdown">{content}</content>
        <updated>{updated}</updated>
        {categorys}
        <app:control>
            <app:draft>{draft}</app:draft>
        </app:control>
        {custom_url_xml}
    </entry>""".encode("UTF-8")
    
    print(custom_url_xml)

    r = req.post(BASE_URL + "/entry", auth=(HATENA_ID, API_KEY), data=xml)
    return r.text

def set_datetime():
    import os
    import datetime
    dt_now = datetime.datetime.now()
    print(dt_now)

    dt_now_jst_aware = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))
    )
    print(dt_now_jst_aware)
    print(dt_now_jst_aware.tzinfo)
    print(dt_now_jst_aware.strftime("%Y%m%d%H%M"))

    dt = dt_now_jst_aware.strftime("%Y%m%d%H")
    # dt = "2022042523"
    file = './articles/' + dt + '.md'

    isExists = os.path.exists(file) 
    print(isExists)
    if isExists != True:
        exit()

    '''
    f = open(file, 'r', encoding='UTF-8')
    data = f.read()
    print(data)
    f.close()
    '''
    return file

if __name__ == "__main__":
    import sys
    '''
    _, arg = sys.argv
    with open(arg, "r") as f:
        title, categorys, *content = f.readlines()
    categorys = categorys.split(",")
    content = "\n".join(content)
    '''
    
    file = set_datetime()
    with open(file, "r") as f:
        title, categorys, custom_url, *content = f.readlines()
    categorys = categorys.split(",")
    custom_url = custom_url.strip()
    content = "\n".join(content)
    #print(content)

    r = hatena_entry(title, content, categorys, custom_url)
    #print(r)

