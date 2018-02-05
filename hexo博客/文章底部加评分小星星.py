打开主题配置文件~/blog/themes/next/_config.yml：
# Star rating support to each article.
# To get your ID visit https://widgetpack.com
rating:
  enable: true
  id:     
  color: ff7600

先去注释中的网站，首页点Rating，然后注册个帐号，填一下自己网站的信息，左上角有个ID，填进主题配置文件中就行，color改成自己喜欢的即可。另：

可以配置评分方式，侧栏>Rating>Setting，建议用IP address或Device(cookie)，免登录，毕竟Socials里面的选项几乎都被墙，不适合国内网络环境。
建议侧栏>Site>Setting中勾选Private选项。
上面两步勾选后别忘了点击页面右下方的SAVE SETTING绿色按钮保存。

打开文件~/blog/themes/next/layout/_macro/post.swig：

{% if theme.rating.enable %}
  <div class="wp_rating">
    <div style="color: rgba(255, 0, 255, 0.95); font-size:13px; letter-spacing:3px;">看完记得五星好评哦亲～</div>
    <div id="wpac-rating"></div>
  </div>
{% endif %}
