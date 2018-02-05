npm install hexo-wordcount --save
出错的化删除这个插件再安装
npm install hexo-helper-word-count --save
或
# Node 版本7.6.0之前,请安装 2.x 版本 (Node.js v7.6.0 and previous)
npm install hexo-wordcount@2 --save


通过以上安装后，你可以在你的模板文件或者.md文件加入以下相关的标签实现本插件的功能
字数统计:WordCount
阅读时长预计:Min2Read
总字数统计: TotalCount



修改post.swig模板
找到themes\next\layout\_macro\post.swig并打开在如下位置插入代码：

{# LeanCould PageView #}
         {% if theme.leancloud_visitors.enable %}
            <span id="{{ url_for(post.path) }}" class="leancloud_visitors" data-flag-title="{{ post.title }}">
		 &nbsp; | &nbsp;
              <span class="post-meta-item-icon">
                <i class="fa fa-eye"></i>
              </span>
              <span class="post-meta-item-text">{{__('post.visitors')}} </span>
              <span class="leancloud-visitors-count"></span>
             </span>
         {% endif %}
	  
#在此处部分为：字数统计、阅读时长插入代码

         <span class="post-time">
	   &nbsp; | &nbsp;
           <span class="post-meta-item-icon">
             <i class="fa fa-calendar-o"></i>
           </span>
           <span class="post-meta-item-text">字数统计:</span>
           <span class="post-count">{{ wordcount(post.content) }}(字)</span>
           
         </span>
	  
      <span class="post-time">
	   &nbsp; | &nbsp;
           <span class="post-meta-item-icon">
             <i class="fa fa-calendar-o"></i>
           </span>
           <span class="post-meta-item-text">阅读时长:</span>
           <span class="post-count">{{ min2read(post.content) }}(分)</span>
           
         </span>
#以上部分为：字数统计、阅读时长插入代码










