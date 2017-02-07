# encoding:utf-8
'''
Convert
Convert markdown to kmjson(md2km) and kmjson to markdown(km2md)

Author: zYeoman(zhuangyw.thu#gmail.com)
Create: 2016-07-31
Modify: 2017-02-07
Version: 0.1.3
'''
import re
import json

HEADER = u'''---
theme:{theme}
template:{template}
version:{version}
---
'''


def km2md(km):
    js = json.loads(km)
    header = HEADER.format(**js)
    content = u'\n'.join(_md_build(js['root'], 1))
    return header + content


def _md_build(node, level):
    lines = []
    empty_line = ''
    data = node['data']
    lines.append('#' * level + ' ' + data.get('text', 'Empty'))
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
    children = node.get('children', [])
    children.sort(key=lambda x: x['data']['text'])
    for child in children:
        lines += _md_build(child, level + 1)
    return lines


def md2km(md):
    km = {"root": {}}
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
        if code_flag or level is None or len(level) > node_level + 2:
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
        current_node = {"data": {"text": content, "note": ""}}
        node_level = len(level) - 1
        if node_level > 0:
            if parent_node[node_level - 1].get('children') is not None:
                parent_node[node_level - 1]['children'].append(current_node)
            else:
                parent_node[node_level - 1]['children'] = [current_node]
        if len(parent_node) < node_level + 1:
            parent_node.append(current_node)
        else:
            parent_node[node_level] = current_node
    _clean(parent_node[0])
    km['root'] = parent_node[0]
    return json.dumps(km)


def _clean(node):
    if re.match(r'^\s*$', node['data']['note']):
        del node['data']['note']
    else:
        node['data']['note'] = node['data']['note'][1:-2]
    children = node.get('children', [])
    for child in children:
        _clean(child)
