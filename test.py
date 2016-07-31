# encoding:utf-8

import convert
text = u'''{"root":{"data":{"id":"b5v6n6s9wxs0","created":1469286636927,"text":"中心主题"},"children":[{"data":{"id":"b5v6n9nbmfi8","created":1469286643159,"text":"3.  有备注","note":"测试\n\n* 第一\n\n$$E=mc^2$$\n"},"children":[{"data":{"id":"b5ybwr2jdygo","created":1469606171780,"text":"3.1"},"children":[{"data":{"id":"b5ybws0i7ogg","created":1469606173834,"text":"3.1.1","layout_right_offset":{"x":18,"y":0}},"children":[{"data":{"id":"b5ybwsjgzy0w","created":1469606174981,"text":"3.1.1.1"},"children":[]}]}]},{"data":{"id":"b61anrcq454w","created":1469907325879,"text":"3.2"},"children":[]},{"data":{"id":"b61anttq6u8g","created":1469907331261,"text":"3.3"},"children":[{"data":{"id":"b61anve97dsg","created":1469907334679,"text":"3.3.1"},"children":[]},{"data":{"id":"b61anwwvu5cg","created":1469907337982,"text":"3.3.2"},"children":[]}]}]},{"data":{"id":"b5ybwi1vf8gg","created":1469606152149,"text":"4.有图片","image":"http://img0.imgtn.bdimg.com/it/u=1869051530,4069646126&fm=21&gp=0.jpg","imageTitle":"linux玩挂之后,重装笔记","imageSize":{"width":200,"height":112},"priority":null,"progress":null},"children":[{"data":{"id":"b61ao84f6wow","created":1469907362382,"text":"4.1 标号1","priority":1},"children":[]},{"data":{"id":"b61aoba1pi8g","created":1469907369253,"text":"4.2 完成100%","progress":9},"children":[]}]},{"data":{"id":"b5ybwjzczhko","created":1469606156351,"text":"1.  有链接","hyperlink":"http://baidu.com","hyperlinkTitle":"hhh","layout_mind_offset":{"x":-22,"y":-90}},"children":[{"data":{"id":"b61amy8ra8wg","created":1469907262512,"text":"1.1"},"children":[]}]},{"data":{"id":"b5ybwk3tp9ss","created":1469606156621,"text":"2."},"children":[]}]},"template":"default","theme":"fresh-blue","version":"1.4.33"}'''.replace('\n','\\n')
md = convert.km2md(text)
print(md)
km = convert.md2km(md)
print(km)
md = convert.km2md(km)
print(md)
