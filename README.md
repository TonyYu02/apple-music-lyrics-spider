## Apple Music Lyrics Spider

(**experimental**) this project is immature and very simple, you can update it as you wish.

## Introduction

This project use your own apple music subscription to get text lyrics from apple music.

### Preparation

1. An Apple Account with Apple Music subscription
  
2. ``` pip install requests re ```

3. get your media-user-token from website

   Open [Apple Music](https://music.apple.com/) and log in, open the Developer tools, Click `Application -> Storage -> Cookies -> https://music.apple.com`, find the cookie named `media-user-token`, copy to code.
  
5. get Authorization from website

   go to console and type`MusicKit.getInstance().developerToken`, add them after `Bearer `(remind the space)
  

## Usage

Just input your url and nation of your account and done

**you may use a vpn to get correct lyrics**

## Reference

[GitHub - zhaarey/apple-music-alac-atmos-downloader: Apple Music ALAC / Dolby Atmos Downloader](https://github.com/zhaarey/apple-music-alac-atmos-downloader)
