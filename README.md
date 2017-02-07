# MindWiki

用mindmap来复习感觉还不错的样子?

总之就是闲的蛋疼...

## 使用

[GIF](http://7xkunb.com1.z0.glb.clouddn.com/gif.gif)

```
git clone https://github.com/zYeoman/mindwiki
cd mindwiki
pip install -r requirement.txt
python app.py runserver
```

## 快捷键

* `h` `j` `k` `l` 移动
* `Enter` 添加同级节点
* `Tab` 添加子节点
* `o` /下打开新页面
* `q` 返回上一级
* `x` 删除节点

## TODO
* 备注, 链接, 图片, 数学公式, Emoji等支持
* 更多快捷键
* 登录
* git-base 存储
* 新的MindMap JS实现

## CHANGELOG
* 0.1.3:
    * Python3支持
    * Fix Bug: 没有失去焦点时直接打开下一层导致当前记录丢失
    * Fix Bug: 多层url时新页面标题错误
    * Enhance: 改进多层url处理方式
* 0.1.2:
    * 新增快捷键`qx`
    * 修复BUG
    * 文件夹层次
* 0.1.1:
    * image,link,note 支持
* 0.1.0:
    * 基础快捷键(`hjklo<Tab><Enter>`)
    * 存储与读取
    * 自动保存，全程无刷新

## 鸣谢
* [kityminder-core](https://github.com/fex-team/kityminder-core)
* [wiki](https://github.com/alexex/wiki)

## LICENSE

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                       Version 2, December 2004

    Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.

               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
      TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

     0. You just DO WHAT THE FUCK YOU WANT TO.
