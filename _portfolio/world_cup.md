---
header:
  overlay_image: /assets/images/soccer_ball.jpg
  caption: "Credit: [**Peter Glaser**](https://www.unsplash.com)"
permalink: /portfolio/world_cup/
toc: true
toc_label: "Contents"
---

# World Cup Passing Networks

I got really interested in the structural characteristics of the network of passes in a soccer game. I used [WebWeb][1], an excellent Python package developed by Hunter Wapman and Dan Larremore at CU Boulder, to visualize these networks. I used the StatsBomb [database][2] on Github for the game data.

You can use the up/down arrows to switch between matches. The size of the nodes indicates how many passes that player has completed, and the width of the lines between nodes (edges) indicates how many passes have been completed between two players.

# Visualization of the 2018 FIFA Men's World Cup
<iframe src="/portfolio/mens_world_cup_2018.html" frameborder="0" scrolling="no" width="900" height="700"></iframe>

This covers 64 matches: 48 matches in group play and 16 matches in the knockout stage.

# Visualization of the 2018 National Women's Soccer League
<iframe src="/portfolio/nwsl_2018.html" frameborder="0" scrolling="no" width="900" height="700"></iframe>

This covers 18 matches out of the 108 matches played in the 2018 NWSL season.

# Visualization of the 2018/2019 FA Women's Super League
<iframe src="/portfolio/fa_super_league_2018_2019.html" frameborder="0" scrolling="no" width="900" height="700"></iframe>

This covers 54 matches out of the 104 matches played in the 2018/2019 FA Women's Super League season.

# Visualization of the 2019 FIFA Women's World Cup
<iframe src="/portfolio/womens_world_cup_2019.html" frameborder="0" scrolling="no" width="900" height="700"></iframe>

This covers 52 matches: 36 matches in group play and 16 matches in the knockout stage.

You can also check out my Github [project][3] to use the GUI to analyze other datasets in this format.

[1]: https://webwebpage.github.io/

[2]: https://github.com/statsbomb/open-data

[3]: https://github.com/NLandry91/World-Cup-Passing-Networks
