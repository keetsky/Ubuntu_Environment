
首先在文件~/blog/themes/next/layout/_custom/sidebar.swig中加入下面代码，Date的值改为你自己的：

<div id="days"></div>
</script>
<script language="javascript">
function show_date_time(){
window.setTimeout("show_date_time()", 1000);
BirthDay=new Date("05/27/2017 15:00:00");
today=new Date();
timeold=(today.getTime()-BirthDay.getTime());
sectimeold=timeold/1000
secondsold=Math.floor(sectimeold);
msPerDay=24*60*60*1000
e_daysold=timeold/msPerDay
daysold=Math.floor(e_daysold);
e_hrsold=(e_daysold-daysold)*24;
hrsold=setzero(Math.floor(e_hrsold));
e_minsold=(e_hrsold-hrsold)*60;
minsold=setzero(Math.floor((e_hrsold-hrsold)*60));
seconds=setzero(Math.floor((e_minsold-minsold)*60));
document.getElementById('days').innerHTML="已运行"+daysold+"天"+hrsold+"小时"+minsold+"分"+seconds+"秒";
}
function setzero(i){
if (i<10)
{i="0" + i};
return i;
}
show_date_time();
</script>

#
然后修改~/blog/themes/next/layout/_macro/sidebar.swig：

{# Blogroll #}
{% if theme.links %}
  <div class="links-of-blogroll motion-element {{ "links-of-blogroll-" + theme.links_layout | default('inline') }}">
    <div class="links-of-blogroll-title">
      <i class="fa  fa-fw fa-{{ theme.links_icon | default('globe') | lower }}"></i>
      {{ theme.links_title }}&nbsp;
      <i class="fa  fa-fw fa-{{ theme.links_icon | default('globe') | lower }}"></i>
    </div>
    <ul class="links-of-blogroll-list">
      {% for name, link in theme.links %}
        <li class="links-of-blogroll-item">
          <a href="{{ link }}" title="{{ name }}" target="_blank">{{ name }}</a>
        </li>
      {% endfor %}
    </ul>
{# 移动到这下面 #}
{% include '../_custom/sidebar.swig' %}
  </div>
{# 原位置 #}
{% endif %}



#
这样就可以了，当然，要是不喜欢颜色，感觉不好看，就可以在上文所提的custom.styl加入：

// 自定义的侧栏时间样式
#days {
    display: block;
    color: rgb(34, 244, 246);
    font-size: 13px;
    margin-top: 15px;
}
