# PhosGraph Instagram Example

We use a mixture of manual control and Python Selenium script, to extract data from Instagram pages, and save them to the PhosGraph database, as illustrated with the series of screenshots below.

After login to Instagram using a web browser, we navigate to a typical user page like the following, with screenshot as shown in figure 1:

- https://www.instagram.com/emmeline_glam/

- Figure 1
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/emmeline_glam.png" width=600>

We run the Python Selenium script as shown in figure 2 in interactive mode (`python3 -i`):

- Figure 2
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/PhosGraph_py.png" width=400>

We have omitted other start up scripts in figure 2 for clarity. Additional explanation can be found ....

Figure 3 shows the PhosGraph page where the json data is entered, corresponding to lines 9 to 14 in figure 2.

- Figure 3
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/post_rc_1.png" width=600>

Figure 4 shows the PhosGraph GET interface, where the database, essentially kept as a space delimited text file, can be accessed via Phoscript Reverse Polish Notation.

- Figure 4
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/phos_get.png" width=600>

Figure 5 shows the same database text file displayed using the text editor provided by the free hosting website.

- Figure 5
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/data_log.png" width=600>

Figures 6 through 9 show the steps PRIOR to opening the page shown in figure 1. We have arranged the explanation for the steps leading to figure 1 after the steps described above because the steps above are easier to understand.

After saving the json data to PhosGraph database, we may navigate back to figure 1. Figure 6 shows the similar page in the PREVIOUS cycle.

- Figure 6
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/basskitten.png" width=600>

By clicking on "following" at the second row of texts from the top, it opens the "PEOPLE / HASHTAGS" floating window as show in figure 7. By clicking "HASHTAG", all the hashtags followed by the current user will be displayed.

- Figure 7
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/hashtags.png" width=600>

Clicking at "#novababe", it leads to a page as shown in figure 8. By hovering the mouse pointer above the thumbnails in figure 8, the number of likes for each thumbnail can be seen. We then chose the thumbnail with the highest number of likes, which then led us to figure 9.

- Figure 8
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/novababe.png" width=600>

By clicking at the user name shown at the top right of the floating window in figure 9, it led us back to the page shown in figure 1.

- Figure 9
<img src="https://github.com/udexon/Phosway/blob/master/Instagram/likes.png" width=600>

The above cycle is repeated to discover more hashtags and popular Instagram accounts with large number of followers.
