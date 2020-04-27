# Book Image Reader
A Dash application primarily built for reading books with pages in image format
<br><br>
The main motivation that lead to the development of this mini application was the lack of satisfaction that arose from reading books, which happen to be portrait oriented, on a landscape oriented screen. One solution I found was to mirror the screen on a tablet and change the orientation to portrait, which I found extremely tedious. The current application is aimed at solving this issue.
<br><br>
This application is for reading books where the pages are in image formats (JPEG, PNG, etc.). This is mostly the case with comics with high graphic content. This app can be used to make reading such books easier.

### Usage Instructions
<br>
![Home](https://github.com/nsurampu/Book-Image-Reader/blob/master/home.png)
<br><br>
The above is the screenshot which you get when launching the app for the first time. To launch the app, navigate into the repo folder and run the ***home.py*** file. This will launch the app on the localhost, which can be accessed by entering the link ***127.0.0.1:8050*** in any web browser. Once here, all you need to do is select the files/images you wish to view, and wait for them to load into the app. Once loaded, you can navigate one page at a time using the **Continue to NEXT PAGE --->** button. If you wish to jump to a particular page, scroll down and select the page number from the dropdown menu. This will show the selected page below the dropdown as preview. Here on, you can use the next page button to continue reading from the immediate next page.
<br><br>
Another feature that needs to be highlighted is the **page cache** feature. This means that when the application is closed, the latest image data that was loaded into the application before closing will be saved. These images will be automatically loaded on the next start-up and will continue unless overridden with some other data.
<br><br>
To get the best out of the app, it is advised to pair it with **ngrok**. Install the ngrok application, tunnel your localhost, and now access the images on any other device by simply connecting to the URL provided. With this, you will be able to read the loaded images on any device of your choice, making for a better reading experience.

## More Features Coming Soon!
