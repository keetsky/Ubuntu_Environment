优化了这么多，但还有一个最影响网站形象和阅读体验的项没有优化，瓦特？字体！

文章字体大小可以编辑～blog/themes/next/source/css/_variables/base.styl：
$font-size-base           = 15px
/* 我写15是单纯因为喜欢5这个数字 */

#############################################33
http://prozhuchen.com/2015/10/05/Hexo%E5%8D%9A%E5%AE%A2%E4%B9%8B%E6%94%B9%E5%AD%97%E4%BD%93/

字体在/themes/hexo-theme-next/source/css/_variables下的custom.styl（这个是NexT主题的目录，其他主题请按图索骥）。
或/themes/hexo-theme-next/source/css/_variables下的base.styl。



然后我们来看怎么改动。
custom.styl文件：
$font-family-headings = Georgia, sans // 标题，修改成你期望的字体族
$font-family-base = "Microsoft YaHei", Verdana, sans-serif // 修改成你期望的字体族

或如

// 站点子标题
.site-subtitle{ 
    font-family: Georgia, sans
    font-size: 16px;
    color: #a57070; //rgb(255, 255, 255);
}


######################
#说明
font-family: "楷体"     #字体类型
font-size:36px		#字体大小
font-style:italic      #normal:默认的正常字体italic:斜体显示文字oblique：属于中间状态
font-weight: normal;//bold; #粗还是细
color: #F00		#字体颜色
background-color:#F00   #置文字的背景颜色
background-image:url(1.png)	#设置元素的背景图像
background-repeat:no-repeat	#用于设置背景图像是否平铺no-repeat:不平铺repeat:平铺整个网页repeat-x:只在水平方向平铺repeat:只在垂直方向平铺
background-attachment:fixed	#设置背景图片是随着滚动条滚动而滚动,fixed的意思是图片固定。scroll的意思是随着浏览器滚动条的变动而变动
background-position:10px 10px	#背景位置。
				1）采用数字
				x:网页横向位置
				y:网页纵向位置
				2）百分比
				0%  0%  ；坐上位置
				100%  100%：右下位置
				50% 50%：中间位置
				等，还有许多，你可以自己尝试一下
				3）关键字设置
				top left:左上位置
				top center:靠上局中位置
				top right:右上位置

background:url(1.png)         #背景

####################3













我们可以看出来第一个字体变量是题目的字体，第二个是其余部分的字体。
因为我们是中文博客，所以肯定希望能改成一些比较漂亮的中文字体，但是显而易见，你改成宋体是不合理的，因为第一会出现乱码情况，第二Hexo也不接受中文名字的字体。所以我们需要使用中文字体的英文名称。下面是中文字体对应的英文名称。

新细明体：PMingLiU 
细明体：MingLiU 
标楷体：DFKai-SB 
黑体：SimHei 
宋体：SimSun 
新宋体：NSimSun 
仿宋：FangSong 
楷体：KaiTi 
仿宋_GB2312：FangSong_GB2312 
楷体_GB2312：KaiTi_GB2312 
微软正黑体：Microsoft JhengHei 
微软雅黑体：Microsoft YaHei 

装Office会多出来的一些字体： 
隶书：LiSu 
幼圆：YouYuan 
华文细黑：STXihei 
华文楷体：STKaiti 
华文宋体：STSong 
华文中宋：STZhongsong 
华文仿宋：STFangsong 
方正舒体：FZShuTi 
方正姚体：FZYaoti 
华文彩云：STCaiyun 
华文琥珀：STHupo 
华文隶书：STLiti 
华文行楷：STXingkai 
华文新魏：STXinwei 

苹果电脑中的字体： 
华文细黑：STHeiti Light [STXihei] 
华文黑体：STHeiti 
华文楷体：STKaiti 
华文宋体：STSong 
华文仿宋：STFangsong 
丽黑 Pro：LiHei Pro Medium 
丽宋 Pro：LiSong Pro Light 
标楷体：BiauKai 
苹果丽中黑：Apple LiGothic Medium 
苹果丽细宋：Apple LiSung Light 
google字体查看：https://fonts.google.com/
Arabic
Amiri
Lateef
Scheherazade
Myanmar
Padauk
Telugu
Dhurjati
Gidugu
Gurajada
Lakki Reddy
Mallanna
Mandali
NTR
Peddana
Ramabhadra
Ravi Prakash
Sree Krushnadevaraya
Suranna
Suravaram
Tenali Ramakrishna

我们只要将自己喜欢字体的英文名加到这两个变量的第一个前面就可以了，有多个字体是为了预防在某些场合前面的字体出现异常，后面的字体可以替代一下。下面是我的定义。

$font-family-headings = KaiTi,"Microsoft YaHei",Georgia, sans // 标题，修改成你期望的字体族
$font-family-base = SimHei, Verdana, sans-serif // 修改成你期望的字体族
至于字体大小，我们在前面提到的base.styl里面61行左右会看见如下定义
：

// Font size
$font-size-base           = 18px
$font-size-small          = $font-size-base - 2px
$font-size-smaller        = $font-size-base - 4px
$font-size-large          = $font-size-base + 4px


// Headings font size
$font-size-headings-base  = 28px
$font-size-headings-step  = 2px
同理，第一个部分$font-size-base是除了标题外的其余部分大小，第二个部分$font-size-headings-base是标题大小，你改动成你希望的大小就可以了。
