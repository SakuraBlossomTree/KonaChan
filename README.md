<h1>Ishitori - イシトリ</h1>

<h2>Rewrote the entire program</h2>

<p>Now you don't have to worry about PRAW and all those stuff because i migrated to safebooru because of reddit's API changes</p>

<br />

<p>A project which I started because i wanted a terminal based wallpaper downloader of my own uses</p>

<p>But I am making this project which is named Ishitori open-sourced so that everyone can use it</p>

<br/>

<h2>Install</h2>

```

git clone git@github.com:SakuraBlossomTree/Ishitori.git

cd Ishitori

mkdir pics/

mkdir vids/

python booru.py


```

Static pictures are saved in the ```pics/```

If you want to also system link it you can do it by using this command 

```
ln -s $HOME/Ishtori/ /usr/local/bin/link_name
```

Change the link_name to your desired name

The file anime-wallpaper.sh just loops through the images in ```pics/``` directory it only works for WM(And no Wayland I am sorry)

booru.sh file is an automated prcoess it's up to you if you want to use the full automated or just the program