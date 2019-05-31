---
header:
  overlay_image: /assets/images/machine.jpg
  caption: "Photo credit: [**Aaron Barnaby**](https://unsplash.com)"
permalink: /portfolio/spindle_vibration/
date: 2019-05-31
toc: true
toc_label: "Contents"
---

# Spindle Vibration Analysis

When I worked at Turbocam International, I developed a software to analyze raw spindle vibration/load data and use this information to improve CNC programs. Unfortunately, the code and data are proprietary due to NDAs.

## Design

We were able to record 3-axis acceleration of the machine spindle and save this data as a .csv file. I wrote a GUI in Python (Using TkInter) to allow a user to
<ul>
<li>Browse for spindle vibration files (with multiple selection)</li>
<li>Examine sections of interest with various trimming options (User defined, trim to shortest, auto-trim)</li>
<li>Plot the vibration magnitude</li>
<li>Integrate the vibration energy</li>
<li>Plot the jerk (change in acceleration)</li>
</ul>

## Results

I used this program to optimize feed rates in CNC programs to minimize spindle vibration while only slowing down problematic sections to also minimize the effect on the cycle time of the CNC program. This methodology drastically improved the maximum spindle vibration in each program, leading to lower spindle wear and longer spindle life.
