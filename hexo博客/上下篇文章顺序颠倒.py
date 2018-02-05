方法就是修改~/blog/themes/next/layout/_macro/post.swig：

{% if not is_index and (post.prev or post.next) %}
  <div class="post-nav">
    <div class="post-nav-next post-nav-item">
      {% if post.prev %}
        <a href="{{ url_for(post.prev.path) }}" rel="prev" title="{{ post.prev.title }}">
          <i class="fa fa-chevron-left"></i> {{ post.prev.title }}
        </a>
      {% endif %}
    </div>
    <span class="post-nav-divider"></span>
    <div class="post-nav-prev post-nav-item">
      {% if post.next %}
        <a href="{{ url_for(post.next.path) }}" rel="next" title="{{ post.next.title }}">
          {{ post.next.title }} <i class="fa fa-chevron-right"></i>
        </a>
      {% endif %}
    </div>
  </div>
{% endif %}
