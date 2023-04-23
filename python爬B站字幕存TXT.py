import os
import re
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree

# 获取视频页面的 HTML 内容
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    return response.text

# 提取字幕的 URL
def extract_subtitle_url(html):
    soup = BeautifulSoup(html, 'lxml')
    scripts = soup.find_all('script')
    for script in scripts:
        if 'window.__INITIAL_STATE__' in script.text:
            subtitle_info = re.search(r'"subtitle":{"allow_submit":\w+,"list":(\[.*\])}', script.text)
            if subtitle_info:
                subtitle_list = subtitle_info.group(1)
                subtitle_json = requests.utils.unquote(subtitle_list)
                lan_info = re.search(r'\{"id":\d+,"lan":"\w+","lan_doc":"\w+","subtitle_url":"(.*?)","author"', subtitle_json)
                if lan_info:
                    return lan_info.group(1)
    return None

# 解析 XML 字幕文件并转换为 TXT
def parse_xml_to_txt(xml_data):
    root = ElementTree.fromstring(xml_data)
    lines = [elem.text.strip() for elem in root.iter() if elem.text and elem.text.strip()]
    return "\n".join(lines)

# 保存字幕到桌面
def save_to_desktop(filename, content):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    with open(os.path.join(desktop_path, filename), "w", encoding="utf-8") as file:
        file.write(content)

# 主函数
def main():
    video_url = "https://www.bilibili.com/video/BV1w24y1c7ba/?share_source=copy_web&vd_source=4b064bf02eb581f208146d3e4cf14f48"
    html = get_html(video_url)
    subtitle_url = extract_subtitle_url(html)

    if subtitle_url:
        xml_data = requests.get(subtitle_url).content.decode("utf-8")
        txt_content = parse_xml_to_txt(xml_data)
        save_to_desktop("bilibili_subtitle.txt", txt_content)
        print("字幕已保存到桌面。")
    else:
        print("未找到字幕。")

if __name__ == "__main__":
    main()
