
// 创建 km 实例
/* global kityminder */
var km = window.km = new kityminder.Minder();
km.renderTo('#minder-view');
$.get(document.URL, {nofmt:'True'}, function(data){
    km.importData('json', data);
},'text');
km.enable();
// km.disable();
editflag=false;
function EditNode(){
    editflag=true;
    var node = km.getSelectedNode();
    if (node){
        var textinput = document.getElementById('textinput');
        textinput.oninput = function (){
            node.setText(this.value);
            km.refresh();
        };
        textinput.onfocus = function(){
            var thisNode = node.getRenderContainer()['node'].getElementsByTagName('text')[0].parentElement;
            thisNode.style.fillOpacity=0;
            this.value = node.getText();
            textinput.style.fontSize=node.getStyle('font-size')+'px';
            textinput.style.color = node.getStyle('color');
            textinputInter = setInterval(function(){
                var box = node.getRenderBox('TextRenderer');
                var bbox = node.getRenderBox();
                var parent = textinput.parentElement;
                // parent.style.left = Math.round(box.x) + 'px';
                // parent.style.top =  Math.round(box.y-bbox.height/2+11) + 'px';
                parent.style.left = Math.round(thisNode.getBoundingClientRect()['left']-5)+'px';
                parent.style.top = Math.round(thisNode.getBoundingClientRect()['top']-5)+'px';
                parent.style.height = Math.round(bbox.height+20)+'px';
                parent.style.width = Math.round(bbox.width+20)+'px';
                textinput.style.height = Math.round(bbox.height+20)+'px';
                textinput.style.width = Math.round(bbox.width+20)+'px';
            }, 50);
        };
        textinput.onblur = function(){
            var thisNode = node.getRenderContainer()['node'].getElementsByTagName('text')[0].parentElement;
            thisNode.style.fillOpacity=1;
            clearInterval(textinputInter);
            var parent = this.parentElement;
            parent.style.left = "-9999px";
            parent.style.top = "-9999px";
            km.focus();
            editflag=false;
        };
        textinput.focus();
    }
}
km.on('keyup', function(e) {
    var node = km.getSelectedNode();
    if (node==null) node=km.getRoot();
    if (node) {
        [ "l", "h", "k", "j" ].forEach(function(key) {
                            if (e.isShortcutKey(key)) {
                                switch(key){
                                    case 'h':k = 'left';break;
                                    case 'j':k = 'down';break;
                                    case 'k':k = 'top';break;
                                    case 'l':k = 'right';break;
                                }

                                var nextNode = node._nearestNodes[k];
                                if (nextNode) {
                                    km.select(nextNode, true);
                                }
                                e.preventDefault();
                            }
                        });
        if (e.isShortcutKey('i')) EditNode();
        if (e.isShortcutKey('x')) km.removeNode(node);
        if (e.isShortcutKey('o') && location.pathname == "/") {
            var new_url = node.data['text'];
            history.pushState(null,null,new_url);
            $.get(document.URL, {nofmt:'True'}, function(data){
                km.importData('json', data);
            },'text');
        }
    }
});
km.on('dblclick', function(e){EditNode()});
km.on('blur', function(e){
    if(!editflag) {
        setTimeout(function(){
            km.focus();
        },100);
        $.post(document.URL, 
                {
                    body: km.exportData('json').fulfillValue
                });
    }   
});
var mousedownonelement = false;

