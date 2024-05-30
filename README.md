
<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/citrixnetscalermemoryleak-tool.png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/citrixnetscalermemoryleak)
![PyPI - Downloads](https://img.shields.io/pypi/dm/citrixnetscalermemoryleak)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/citrixnetscalermemoryleak/total)
<a href="https://github.com/Cappricio-Securities/citrixnetscalermemoryleak/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/citrixnetscalermemoryleak"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install citrixnetscalermemoryleak 
        ```
   - Run bellow command to check
     - `citrixnetscalermemoryleak -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          citrixnetscalermemoryleak --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          citrixnetscalermemoryleak -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          citrixnetscalermemoryleak -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          citrixnetscalermemoryleak -i urls.txt -o out.txt
        ```
   - Want to Learn about [`citrixnetscalermemoryleak`](https://blogs.cappriciosec.com/cve/167/The%20Potential%20Citrix%20NetScaler%20Memory%20Leak)? Then Type Below command
      - ```bash
          citrixnetscalermemoryleak -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-05-29%20at%202.37.45%20PM.png)](https://asciinema.org/a/ARfK9usVLsdseyuqCfmWFhXKG)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                                                             v1.0
               __                  __                                                                __           __
   ____  ___  / /_______________ _/ /__  _____      ____ ___  ___  ____ ___  ____  _______  __      / /__  ____ _/ /__
  / __ \/ _ \/ __/ ___/ ___/ __ `/ / _ \/ ___/_____/ __ `__ \/ _ \/ __ `__ \/ __ \/ ___/ / / /_____/ / _ \/ __ `/ //_/
 / / / /  __/ /_(__  ) /__/ /_/ / /  __/ /  /_____/ / / / / /  __/ / / / / / /_/ / /  / /_/ /_____/ /  __/ /_/ / ,<
/_/ /_/\___/\__/____/\___/\__,_/_/\___/_/        /_/ /_/ /_/\___/_/ /_/ /_/\____/_/   \__, /     /_/\___/\__,_/_/|_|
                                                                                     /____/
                              Developed By https://cappriciosec.com

citrixnetscalermemoryleak : Bug scanner for WebPentesters and Bugbounty Hunters 

$ citrixnetscalermemoryleak [option]

Usage: citrixnetscalermemoryleak [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | citrixnetscalermemoryleak -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | citrixnetscalermemoryleak -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | citrixnetscalermemoryleak -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | citrixnetscalermemoryleak --chatid yourid |
| `-b` | `--blog` | To Read about citrixnetscalermemoryleak Bug | citrixnetscalermemoryleak -b |
| `-h` | `--help` | Help Menu | citrixnetscalermemoryleak -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com
