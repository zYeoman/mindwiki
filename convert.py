# encoding:utf-8
'''
Convert
Convert markdown to kmjson(md2km) and kmjson to markdown(km2md)

Author: zYeoman(zhuangyw.thu#gmail.com)
Create: 2016-07-31
Modify: 2016-07-31
Version: 0.1.1
'''
import re
import json

HEADER=u'''---
theme:{theme}
template:{template}
version:{version}
---
'''

def km2md(km):
    js = json.loads(km)
    header = HEADER.format(**js)
    content = u'\n'.join(_md_build(js['root'], 1))
    return header+content

def _md_build(node, level):
    lines = []
    empty_line = ''
    data = node['data']
    lines.append('#'*level+' '+data.get('text','Empty'))
    lines.append(empty_line)
    image = data.get('image')
    link = data.get('hyperlink')
    note = data.get('note')
    if link:
        lines.append(u'[{hyperlinkTitle}]({hyperlink})'.format(**data))
        lines.append(empty_line)
    if image:
        lines.append(u'![{imageTitle}]({image})'.format(**data))
        lines.append(empty_line)
    if note:
        lines.append(note)
        lines.append(empty_line)
    children = node.get('children',[])
    children.sort(key=lambda x:x['data']['text'])
    for child in children:
        lines += _md_build(child, level+1)
    return lines

def md2km(md):
    km = {"root":{}}
    meta_flag = 0
    code_flag = False
    node_level = 0
    parent_node = []
    current_node = None
    for line in md.split('\n'):
        if re.match(r'^-{3,}$', line) is not None:
            meta_flag += 1
            continue
        if meta_flag == 1:
            groups = re.match('(.+):(.+)', line).groups()
            km[groups[0]] = groups[1]
            continue
        if re.match(r'^```\w*', line) is not None:
            code_flag = not code_flag
            continue
        level, content = re.match('^(#+)? ?(.*)$', line).groups()
        if code_flag or level is None or len(level) > node_level+2:
            if current_node is not None:
                img = re.match(r'!\[(.*)\]\((https?.*)\)', line)
                link = re.match(r'\[(.*)\]\((https?.*)\)', line)
                if img is not None:
                    current_node['data']['image'] = img.groups()[1]
                    current_node['data']['imageTitle'] = img.groups()[0]
                elif link is not None:
                    current_node['data']['hyperlink'] = link.groups()[1]
                    current_node['data']['hyperlinkTitle'] = link.groups()[0]
                else:
                    current_node['data']['note'] += line + '\n'
            continue
        current_node = {
            "data":{
                "text": content,
                "note": ""
            }
        }
        node_level = len(level) - 1
        if node_level > 0:
            if parent_node[node_level - 1].get('children') is not None:
                parent_node[node_level - 1]['children'].append(current_node)
            else:
                parent_node[node_level - 1]['children'] = [current_node]
        if len(parent_node) < node_level+1:
            parent_node.append(current_node)
        else:
            parent_node[node_level] = current_node
    _clean(parent_node[0])
    km['root'] = parent_node[0]
    return json.dumps(km)
    
def _clean(node):
    if re.match('^\s*$',node['data']['note']):
        del node['data']['note']
    else:
        node['data']['note'] = node['data']['note'][1:-2] 
    children = node.get('children',[])
    for child in children:
        _clean(child)
        

def test():
    text = u'''{"root":{"data":{"id":"b5v6n6s9wxs0","created":1469286636927,"text":"中心主题"},"children":[{"data":{"id":"b5v6n9nbmfi8","created":1469286643159,"text":"3.  有备注","note":"测试\n\n* 第一\n\n$$E=mc^2$$\n"},"children":[{"data":{"id":"b5ybwr2jdygo","created":1469606171780,"text":"3.1"},"children":[{"data":{"id":"b5ybws0i7ogg","created":1469606173834,"text":"3.1.1","layout_right_offset":{"x":18,"y":0}},"children":[{"data":{"id":"b5ybwsjgzy0w","created":1469606174981,"text":"3.1.1.1"},"children":[]}]}]},{"data":{"id":"b61anrcq454w","created":1469907325879,"text":"3.2"},"children":[]},{"data":{"id":"b61anttq6u8g","created":1469907331261,"text":"3.3"},"children":[{"data":{"id":"b61anve97dsg","created":1469907334679,"text":"3.3.1"},"children":[]},{"data":{"id":"b61anwwvu5cg","created":1469907337982,"text":"3.3.2"},"children":[]}]}]},{"data":{"id":"b5ybwi1vf8gg","created":1469606152149,"text":"4.有图片","image":"http://img0.imgtn.bdimg.com/it/u=1869051530,4069646126&fm=21&gp=0.jpg","imageTitle":"linux玩挂之后,重装笔记","imageSize":{"width":200,"height":112},"priority":null,"progress":null},"children":[{"data":{"id":"b61ao84f6wow","created":1469907362382,"text":"4.1 标号1","priority":1},"children":[]},{"data":{"id":"b61aoba1pi8g","created":1469907369253,"text":"4.2 完成100%","progress":9},"children":[]}]},{"data":{"id":"b5ybwjzczhko","created":1469606156351,"text":"1.  有链接","hyperlink":"http://baidu.com","hyperlinkTitle":"hhh","layout_mind_offset":{"x":-22,"y":-90}},"children":[{"data":{"id":"b61amy8ra8wg","created":1469907262512,"text":"1.1"},"children":[]}]},{"data":{"id":"b5ybwk3tp9ss","created":1469606156621,"text":"2."},"children":[]}]},"template":"default","theme":"fresh-blue","version":"1.4.33"}'''.replace('\n','\\n')
    md1 = km2md(text)
    km = md2km(md1)
    md2 = km2md(km)
    return md1==md2
    
if __name__ == '__main__':
    print(test())
