首先编辑~/blog/themes/next/layout/_partials/footer.swig：


在下面这行代码中，加上id="heart"
<span class="with-love" id="heart">


然后编辑custom.styl，加入：

// 自定义页脚跳动的心样式
@keyframes heartAnimate {
    0%,100%{transform:scale(1);}
    10%,30%{transform:scale(0.9);}
    20%,40%,60%,80%{transform:scale(1.1);}
    50%,70%{transform:scale(1.1);}
}
#heart {
    animation: heartAnimate 1.33s ease-in-out infinite;
}
.with-love {
    color: rgb(255, 113, 168);
}
