

1、找到 \themes\next\layout\partials\下面的footer.swig文件，打开会发现，有如下图的语句：

{% if theme.footer.powered %}
  <div class="powered-by">{#
  #}{{ __('footer.powered', '<a class="theme-link" target="_blank" href="https://hexo.io">Hexo</a>') }}{#
#}</div>



  <div class="powered-by">{#
  #}{{ __('footer.powered', '<a class="theme-link" target="_blank" href="https://hexo.io">Hexo</a>') }}{#
#}</div>







  <div class="theme-info">{#
  #}{{ __('footer.theme') }} &mdash; {#
  #}<a class="theme-link" target="_blank" href="https://github.com/iissnan/hexo-theme-next">{#
    #}NexT.{{ theme.scheme }}{#
  #}</a>{% if theme.footer.theme.version %} v{{ theme.version }}{% endif %}{#
#}</div>



第一个框 是下面侧栏的“日期❤ XXX”
如果想像我一样加东西，一定要在双大括号外面写。如：xxx,当然你要是想改彻底可以变量都删掉，看个人意愿。


第二个，是图一当中 “由Hexo驱动” 的Hexo链接，先给删掉防止跳转，如果想跳转当然也可以自己写地址，至于中文一会处理。注意删除的时候格式不能错，只把<a>...</a>标签这部分删除即可，留着两个单引号’’,否则会出错哦。

第三个框也是最后一个了，这个就是更改图一后半部分“主题-Next.XX”,这个比较爽直接将..都删掉，同样中文“主题”一会处理，删掉之后在上一行 ‘-’后面可以随意加上你想显示的东西，不要显示敏感信息哟，请自重。

2、接下来，处理剩余的中文信息。找到这个地方\themes\next\languages\ 下面的语言文件zh-Hans.yml（这里以中文为例，有的习惯用英文的配置文件，道理一样，找对应位置即可）
打开之后,修改

footer:
  powered: "%s 个人专属"
  theme: 博客

看到了吧，这个就是传值传过去的，你想显示什么就在这里面大肆的去改动吧。其实在第二个框中，就可以把值都改掉，不用接受传值的方式，完全自己可以重写。不过我不建议那样做，因为传值这样只要是后续页面需要这几个值那么就都会通过取值去传过去，要是在刚才footer文件中直接写死，后续不一定哪个页面需要传值，但是值为空了或者还是原来的，可就尴尬了。所以还是这样改动吧




