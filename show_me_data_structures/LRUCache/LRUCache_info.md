## Caching is an optimization technique that you can use in your applications to keep recent or often-used

## data in memory locations that are faster or computationally cheaper to access than their source.

## Imagine you’re building a newsreader application that fetches the latest news from different sources.

## As the user navigates through the list, your application downloads the articles and displays them on

## the screen.

## What would happen if the user decided to move repeatedly back and forth between a couple of news

## articles? Unless you were caching the data, your application would have to fetch the same content every time!

## That would make your user’s system sluggish

## and put extra pressure on the server hosting the articles.

## Time Complexity:

this solution is a combination of `Hashtable` and `DoublyLinkedList` because:

1. inserting and deleting items in DoubleLinkedList is very fast
2. time complexity in look up in Dictionaries will always be constant time `O(1)`
