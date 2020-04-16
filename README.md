# The truth is more important than ever—let's make sure easy privacy protection is available.

Differential privacy should be simple. Now that data defines our world, we need to look at the cost of privacy. Let's make protecting privacy easy [(not like this!)](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf).

<br><br>

# What is differential privacy and how can I start protecting privacy?

Differential privacy allows for data to be preserved while making sure that attackers cannot gain access to an individual's data. Even if you publish summary statistics (like average age of participants, unlabeled addresses of participants, etc.), attackers can gain access to *individual* data (like age of *each* participant, *labeled* addresses of participants, etc.). In order to achieve this, differential privacy slightly changes the actual dataset to make sure that any uncovered data will not give away personal information. See below for how to get started!

<br>

# The world is data
![The world is data](https://live.staticflickr.com/5228/5679642883_24a2e905e0_b.jpg)

# Read the Docs
Read the docs for how to use this API. See also [Quantalabs](https://www.github.com/Quantalabs)

# What's new?

The latest release `v2.0-alpha` features the all-new exponential mechanism, which allows for differential privacy while maximizing a policy function `u`. This is great for auctions and many other applications which seek to maximize some objective. The code is available on Github under the `Releases` tab. However, there is no documentation on this yet and there may be bugs. We hope to fix this in the next release ... 

<br>
#Made with ❤️ at 🏠.
