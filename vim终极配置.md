####图省事的配置
    (github_web)[https://github.com/sakurazhu/vim]

####经典配置
> spf13-vim +YouCompleteMe

1. spf13-vim 安装
```
   $ curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh
```
2. YouCompleteMe 安装
(web)[https://www.bbsmax.com/A/LPdoMe6jJ3/]
2.1.1 在spf13中指定安装YouCompleteMe插件也很方便，只需要在文件~/.vimrc.before.local中添加下面一行
```
    let g:spf13_bundle_groups=['general', 'youcompleteme'] 
    或#let g:spf13_bundle_groups['general', 'writing', 'neocomplcache', 'programming', 'php', 'ruby', 'python', 'javascript', 'html', 'misc', 'youcompleteme', ]
```
  然后采用Vundle命令安装
```
   $ vim
   在vim中输入 
   :BundleInstall!
```
2.1.2 编译ycm_core.so

```
cd ~/.vim/bundle/YouCompleteMe/
./install.py --all #编译支持所有功能
or
./install.py --clang-completer #只支持C/C++补全
```

2.1.3 YouCompleteMe配置
   .vimr或.vimrc.local配置添加
```
" YouCompleteMe {
        if count(g:spf13_bundle_groups, 'youcompleteme')
            let g:acp_enableAtStartup = 0
            " global conf which is needed to resolve name in system include
            " file or other  third-part include file
            let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
            let g:ycm_server_python_interpreter='/usr/bin/python'
            " enable completion from tags
            let g:ycm_collect_identifiers_from_tags_files = 1
            let g:ycm_seed_identifiers_with_syntax = 1
            let g:ycm_confirm_extra_conf = 0
            let g:ycm_cache_omnifunc=0
            let g:ycm_key_invoke_completion = '<C-;>'
            nnoremap <F5> :YcmForceCompileAndDiagnostics<CR>
            nnoremap <leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR>
```
> 上面配置中全局.ycm_extra_conf.py路径很重要，如果不配置将无法解析C/C++头文件

.ycm_extra_conf.py 模版位于YouCompleteMe/third_party/ycmd/cpp/ycm/，其中-isystem flag用来配置系统头文件路径，-I用来配置第三方头文件路径, 一个支持C/C++工程的ycm_extra_conf.py部分配置文件修改添加如下：
```
'-std=c++11',
#'-std=c99',
# ...and the same thing goes for the magic -x option which specifies the
# language that the files to be compiled are written in. This is mostly
# relevant for c++ headers.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
'-isystem',
'../BoostParts',
#-isystem: system include file path按照自己的头文件添加iinclude路径
'-isystem', '/usr/include',
'-isystem', '/usr/local/include',
'-isystem', '/usr/include/c++/4.8.4',
'-isystem','/usr/include/x86_64-linux-gnu/c++',
]
```

----
2.2 基于vundle安装
(web)[https://www.cnblogs.com/274914765qq/p/4439189.html]
使用vundle进行安装，在.vimrc中添加如下代码
```
Bundle 'Valloric/YouCompleteMe'
```
保存退出后打开vim，在正常模式下输入
```
:BundleInstall
```
等待vundle将YouCompleteMe安装完成，而后需要进行编译安装
```
cd ~/.vim/bundle/YouCompleteMe
./install.sh --clang-completer
```
在.vimrc中对YouCompleteMe的配置如下
```
" YouCompleteMe配置
let g:ycm_error_symbol = '>>'
let g:ycm_warning_symbol = '>*'
nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>gf :YcmCompleter GoToDefinition<CR>
nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR>
nmap <F4> :YcmDiags<CR>
```
nmap<C-a> :YcmCompleter FixIt<CR>  




#######自动补全法2
因为安装`YouCompleteMe`太麻烦了，可能会安装`jedi-vim`代替;
在.vimrc 添加 jedi-vim 和 supertab
```
 call vundle#begin()  
...  
 Bundle 'davidhalter/jedi-vim'  
 Bundle 'ervandew/supertab'  
...  
 call vundle#end()            " required  
 filetype plugin indent on    " required  
```
 打开 vim 使用 :PluginInstall 命令安装插件
cd ~/.vim/bundle/jedi-vim/ && git submodule update --init
 在 .vimrc 添加
```
let g:SuperTabDefaultCompletionType = "context"  
let g:jedi#popup_on_dot = 0  
```
#### 问题
1. YouCompleteMe unavailable : requires Vim 7.4.143
   vim 版本不够新需要升级
   查看下vim版本`$vim --version`
```
sudo add-apt-repository ppa:jonathonf/vim 
sudo apt update 
sudo apt install vim 
#or
sudo add-apt-repository ppa:jonathonf/vim
sudo apt-get update && sudo apt-get upgrade
```
如果还不行，进行如下操作：sudo apt-get -u dist-upgrade（强制更新软件包到最新版本，并自动解决缺少的依赖包） ，问题解决。在不行就下载vim源码安装

