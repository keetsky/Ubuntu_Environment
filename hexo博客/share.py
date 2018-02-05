分享到QQ等
网址教程：http://ookamiantd.top/2017/build-blog-hexo-advanced/#好玩的样式
只能有一种share

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
集成Mod分享组件


Step1、获取 AppKey
在 Mob http://www.mob.com/注册账号后，点击头像进入后台，选择 shareSDK 添加一个 Web应用：可以查看概况获得appkey
##########
Step2、在主题配置文件中添加配置：
mob_share:
  enable: true
  appkey: ********
###################
Step3、在next/layout/_partials/share/里面添加mob_share.swig：
<!--MOB SHARE BEGIN-->
<div class="-hoofoo-share-title">分享到：</div>
<div class="-hoofoo-share-buttons">
    <div class="-mob-share-weibo -hoofoo-share-weibo -hoofoo-share-ui-button"><i class="fa fa-weibo" aria-hidden="true"></i></div>
    <div class="-mob-share-weixin -hoofoo-share-weixin -hoofoo-share-ui-button"><i class="fa fa-weixin" aria-hidden="true"></i></div>
    <div class="-mob-share-qq -hoofoo-share-qq -hoofoo-share-ui-button"><i class="fa fa-qq" aria-hidden="true"></i></div>
    <div class="-mob-share-twitter -hoofoo-share-twitter -hoofoo-share-ui-button"><i class="fa fa-twitter" aria-hidden="true"></i></div>
    <div class="-hoofoo-share-more -hoofoo-share-ui-button -mob-share-open"><i class="fa fa-ellipsis-h" aria-hidden="true"></i></div>
</div>
<div class="-mob-share-ui" style="display: none">
    <ul class="-mob-share-list">
        <li class="-mob-share-weibo"><p>新浪微博</p></li>
        <li class="-mob-share-weixin"><p>微信</p></li>
        <li class="-mob-share-qzone"><p>QQ空间</p></li>
        <li class="-mob-share-qq"><p>QQ好友</p></li>
        <li class="-mob-share-tencentweibo"><p>腾讯微博</p></li>
        <li class="-mob-share-renren"><p>人人网</p></li>
        <li class="-mob-share-kaixin"><p>开心网</p></li>
        <li class="-mob-share-douban"><p>豆瓣</p></li>
        <li class="-mob-share-youdao"><p>有道云笔记</p></li>
        <li class="-mob-share-mingdao"><p>明道</p></li>
        <li class="-mob-share-pengyou"><p>朋友网</p></li>
        <li class="-mob-share-facebook"><p>Facebook</p></li>
        <li class="-mob-share-twitter"><p>Twitter</p></li>
        <li class="-mob-share-pocket"><p>Pocket</p></li>
        <li class="-mob-share-google"><p>Google+</p></li>
        <li class="-mob-share-tumblr"><p>Tumblr</p></li>
        <li class="-mob-share-instapaper"><p>Instapaper</p></li>
        <li class="-mob-share-linkedin"><p>Linkedin</p></li>
    </ul>
    <div class="-mob-share-close">取消</div>
</div>
<div class="-mob-share-ui-bg"></div>
<script id="-mob-share" src="http://f1.webshare.mob.com/code/mob-share.js?appkey={{theme.mob_share.appkey}}"></script>
<!--MOB SHARE END-->
########
Step4、在next/layout/post.swig中修改条件分支将mob_share加入：
{% if theme.jiathis %}
      {% include '_partials/share/jiathis.swig' %}
    {% elseif theme.baidushare %}
      {% include '_partials/share/baidushare.swig' %}
    {% elseif theme.add_this_id %}
      {% include '_partials/share/add-this.swig' %}
    {% elseif theme.duoshuo_shortname and theme.duoshuo_share %}
      {% include '_partials/share/duoshuo_share.swig' %}
    {% elseif theme.mob_share.enable %}
      {% include '_partials/share/mob_share.swig' %}
{% endif %}

#############
Step5、在next/source/css/_common/components/third-party/里添加样式文件mob_share.styl：
.-hoofoo-share-buttons{
    display: inline-block;
}
.-hoofoo-share-title{
    font-size: 1.1em;
    font-weight: 200;
}
.-hoofoo-share-ui-button{
    cursor: pointer;
    background-color: #555;
    color: #fff;
    font-size: 24px;
    line-height: 40px;
    width: 40px;
    height: 40px;
    margin: 10px;
    border-radius: 25px;
    float: left;
    transition: background 0.4s;
    -moz-transition: background 0.4s;    /* Firefox 4 */
    -webkit-transition: background 0.4s;    /* Safari 和 Chrome */
    -o-transition: background 0.4s;
}
.-hoofoo-share-weibo:hover{
    background-color: #cf3f41;
}
.-hoofoo-share-weixin:hover{
    background-color: #18a01a;
}
.-hoofoo-share-qq:hover{
    background-color: #950c0c;
}
.-hoofoo-share-twitter:hover{
    background-color: #2ab3e6;
}
.-hoofoo-share-more:hover{
    background-color: #777;
}
.-mob-share-weixin-qrcode-content{
    border-radius: 4px;
    -webkit-box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    -moz-box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    -o-box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}
.-mob-share-weixin-qrcode{
    margin: 5% !important;
    width: 90% !important;
    height: auto !important;
}
.-mob-share-weixin-qrcode-close {
    background-image: url('/lib/fancybox/source/fancybox_sprite.png') !important;//因为兼容问题把vendor改成了lib，根据自己的路径修改
}
.-mob-share-weixin-qrcode-close {
    overflow: hidden;
    line-height: 100px !important;
    position: absolute !important;
    top: -18px !important;
    right: -18px !important;
    width: 36px !important;
    height: 36px !important;
    cursor: pointer !important;
    z-index: 8040 !important;
}
/*Retina graphics!*/
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
       only screen and (min--moz-device-pixel-ratio: 1.5),
       only screen and (min-device-pixel-ratio: 1.5){
    .-mob-share-weixin-qrcode-close {
        background-image: url('/lib/fancybox/source/fancybox_sprite@2x.png') !important;//因为兼容问题把vendor改成了lib，根据自己的路径修改
        background-size: 44px 152px !important; /*The size of the normal image, half the size of the hi-res image*/
    }
}
.-mob-share-close{
    height: 4em !important;
    font-size: 0.8em !important;
    line-height: 4em !important;
    background: #555 !important;
    color: #fff !important;
}

#############
Step6、同一目录下的 third-party.styl 中添加：
@import "mob_share";
#############
Step7、在next/layout/_scripts/third-party/里添加脚本文件mob_share.swig：
{% if theme.mob_share.enable %}
<script type="text/javascript">
    //微信二维码点击背景关闭
    $('body').delegate('.-mob-share-weixin-qrcode-bg','click', function(){
         $(".-mob-share-weixin-qrcode-close").trigger("click");
    }); 
</script>
{% endif %}


############
Step8、在next/layout/_layout.swig的body标签结束前添加：
{% include '_scripts/third-party/mob_share.swig' %}











































































