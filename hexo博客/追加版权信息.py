
文章末尾追加版权信息

找到themes/next/layout/_macro/post.swig，在footer之前添加如下代码(添加之前确保已添加样式)：

<div>
	    <p id="div-border-left-red">
	   <b>本文基于<a target="_blank" title="Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" href="http://creativecommons.org/licenses/by-sa/4.0/"> 知识共享署名-相同方式共享 4.0 </a>国际许可协议发布</b><br/>
	    <span>
	    <b>本文地址：</b><a href="{{ url_for(page.path) }}" title="{{ page.title }}">{{ page.permalink }}</a><br/><b>转载请注明出处，谢谢！</b>
	    </span>
	    </p>
</div>


