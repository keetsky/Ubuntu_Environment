在/themes/hexo-theme-next/layout/_macro/post.swig里面的下面的位置加上如下代码：

{% if post.categories and post.categories.length %}
        <span class="post-category" >
        </span>
      {% endif %}
 <!-- 在下面的位置加上如下代码 -->
      <span id="busuanzi_container_page_pv">
      &nbsp; | &nbsp; 热度&nbsp; <span id="busuanzi_value_page_pv"></span>°C
      </span>
  <!-- 在上面的位置加上如上代码 -->    
  
      {% if post.comments %}
        {% if (theme.duoshuo and theme.duoshuo.shortname) or theme.duoshuo_shortname %}
          <span class="post-comments-count">
            &nbsp; | &nbsp;
            <a href="{{ url_for(post.path) }}#comments" itemprop="discussionUrl">
              <span class="post-comments-count ds-thread-count" data-thread-key="{{ post.path }}" itemprop="commentsCount"></span>
            </a>
          </span>


但是这有一个缺陷。就是我们会发现在主页时显示的热度和进入博客后的热度不一样，那是因为在主页时他显示的是主页这个页面的阅读量，而不是博客的阅读量，所以我们需要改变一些：

我们在/themes/hexo-theme-next/layout/_macro/目录下新建post-article.swig,把这些post.swig中的内容复制过去，而且加上上面的统计代码，然后在/themes/hexo-theme-next/layout/post.swig上面% import '_macro/post.swig' as post_template %中的post.swig改成post-article.swig，这样子就解决啦。就是在主页上的博客名字下面不会有阅读人数，进入博客才能看见
