# Google PageRank

## Introduction

Larry Page and Sergey Brin developed PageRank at Stanford University in 1996 as part of a research project about a new kind of search engine. Rajeev Motwani and Terry Winograd co-authored with Page and Brin the first [paper](http://infolab.stanford.edu/pub/papers/google.pdf) about the project, describing PageRank and the initial prototype of the Google search engine, published in 1998. Shortly after, Page and Brin founded Google Inc., the company behind the Google search engine. PageRank is a way of measuring the importance of website pages. According to Google: PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites.

Currently, PageRank is not the only algorithm used by Google to order search results, but it is the first algorithm that was used by the company, and it is the best known. While just one of many factors that determine the ranking of Google search results, PageRank continues to provide the basis for all of Google's web search tools.

## Theory

The algorithm is explained in detail at below resources:
- [The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://infolab.stanford.edu/pub/papers/google.pdf)
- [The Google PageRank Algorithm](https://web.stanford.edu/class/cs54n/handouts/24-GooglePageRankAlgorithm.pdf)
- [Method for node ranking in a linked database](https://patents.google.com/patent/US6285999B1/en)
- [PageRank](https://cs.brown.edu/courses/cs016/static/files/assignments/projects/GraphHelpSession.pdf)

The math (specifically, linear algebra) behind this algorithm is explained at below resources:

- [THE $25,000,000,000 EIGENVECTOR - THE LINEAR ALGEBRA BEHIND GOOGLE](https://www.rose-hulman.edu/~bryan/googleFinalVersionFixed.pdf)
- [PageRank Algorithm - The Mathematics of Google Search](http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html)

## About this application

This python program implements the primitive PageRank algorithm leveraging Eigenvectors using the scipy library.
This program takes a matrix representing the significance of the web pages (Refer [this](https://www.rose-hulman.edu/~bryan/googleFinalVersionFixed.pdf)). It then computes the Eigenvector of the input matrix whose Eigenvalue is 1. The calculated Eigenvector represents the importance of each web page in the input matrix. The program prints the pages in decreasing order of their importance. 

### Prerequisites

Refer to requirements.txt for the required libraries.

