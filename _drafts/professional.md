---
header:
  overlay_image: /assets/images/code.jpg
  caption: "Photo credit: [**Marcus Spiske**](https://unsplash.com)"
toc: true
toc_label: "Contents"
permalink: /professional/
---

# Professional

*(For the bulleted version of my professional life, see [my resume][1]. Order is
reverse chronological, starting wtih my most recent work.)*

## the Trade Desk

**10/2017 to present**

[The Trade Desk][2] is a company that runs a software platform which interprets
user data to bid on advertising space on the web.[^fnote1] They process over 7
millions bids each second, and their algorithms have a maximum latency on the
order of milliseconds, as all the processing must happen as the webpage
loads. Most of the adjustments to bidding strategies are done by traders, who
analyze a given advertising campaign and suggest adjustments.

I work with the research & development team to develop algorithms that
automatically optimize advertising campaigns. These algorithms utilize both the
internal feedback data collected by TTD, and external data sources, such as
health metrics or Twitter sentiment analysis. The technological core of this
method is the deep learning library TensorFlow. In a test deployment of these
automated strategies, they performed twice as well as the baseline campaign.

We heavily employ the full Python machine learning stack, including TensorFlow,
pandas, and scikit-learn. To interact with databases, we use SQL and
Spark. Amazon Web Services is our main cloud ecosystem. We use S3 for storage,
Glue for crawling, Athena for querying, and SageMaker for prototyping and
deploying models. The team eploys the Agile development method, which allows for
quick iteration through ideas and flexibility in the face of changing
constraints.

## Entelligent

**11/2016 to 10/2017**

[Entelligent][3] works to synthesize financial and envioronmental data in a way
that provides market insights generates portfolio value. This is done by
combining traditional techniques from financial analysis with modeling and
dynamics insights provided by the [En-ROADS climate model][4]. Entelligent has
recently published the Smart Climate index (ticker SCLMX), which is available on
Bloomberg and Thompson Reuters terminals.

I was hired to establish the technical foundation for what was then an idea
(climate data influences markets) without any mathematical grounding. I built the
codebase that is used to maintain their indices, which involved not only coding,
but the development of the optimization and regression techniches that
facilitate the combination of market and climate data. In backtesting, our
indices outperform the S&P 500, showing higher returns and lower risk.

As at the Trade Desk, the technological foundation here is the Python ML stack,
including pandas, scikit-learn, and cvxpy, a convex optimization library. Data
visualization is also an essential aspect of work like this; I do this in
Python, primarily via matplotlib and seaborn.

## University of Colorado

**9/2013 to present**

In my time as a graduate student in the [Applied Math department][5] at CU, I
worked almost continuously[^fnote3] as a teaching assistant and instructor. I
have taught classes in single- and multivariable calculus, as well as computer
lab classes on Mathematica and Matlab. My favorite course to teach is definitely
multivariable calculus; I get a kick out of helping the students wrap their head
around the kind of spatial reasoning that this work requires.

I try to use alternative class structures that encourage student participation;
I know from experience that passive learning (i.e. listening to a lecture)
doesn't work. In my classes the students work together while standing at a
blackboard, which helps them stay alert and engaged. In this way, I function as
more of a mentor or a guide than someone who is going to inject them with
mathematical knowledge; the format helps them realize that they'r really
teaching themselves.

Working as a teacher has honed my presentation and communication skills
immensely. I've learned that there are ten thousand ways to present given
material, but only a few of them are good at both making the ideas clear, and
inspiring interest in it. Working as an instructur also hinges on good customer
relations skills, and I learned through experience the best ways to work with
dissatisfied students in order to keep them happy and engaged in the work.



[1]: /assets/docs/resume.pdf

[2]: https://www.thetradedesk.com/about

[3]: https://www.entelligent.com/

[4]: https://www.climateinteractive.org/tools/en-roads/

[^fnote1]: This field is often referred to as "ad-tech."

[^fnote2]: As is often the case in the financial world, the code here is not
    open source.
	
[^fnote3]: I worked as a research assistant at NIST from Summer 2012 through
    Spring 2013 semesters. See [this project](/portfolio/qm_stats/) in the research
    section.
