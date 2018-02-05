
文章加密

打开themes->next->layout->_partials->head.swig文件,插入这样一段代码：
<script>
    (function(){
        if('{{ page.password }}'){
            if (prompt('请输入文章密码') !== '{{ page.password }}'){
                alert('密码错误！');
                history.back();
            }
        }
    })();
</script>


然后在文章上写成类似这样：
---
title: Hello World
date: 2016/7/13 20:46:25
categories:
- Diary
tags:
  - Testing
  - Another Tag
password: 123456
---

