# https://neetcode.io/problems/design-twitter-feed?list=neetcode150

import heapq
from typing import List, Dict, Set, Tuple


class Twitter:

    def __init__(self):
        self.tweets: Dict[int, Tuple(int, int)] = {}
        self.followees: Dict[int, Set[int]] = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        tweet = (self.counter, tweetId)

        if userId in self.tweets:
            self.tweets[userId].append(tweet)
        else:
            self.tweets[userId] = [tweet]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.followees:
            self.followees[followerId].add(followeeId)
        else:
            self.followees[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        tenLatestTweets = []
        tweetSets = []

        if userId in self.tweets:
            tweetSets.append(self.tweets[userId])

        if userId in self.followees:
            for followee in self.followees[userId]:
                if followee in self.tweets:
                    tweetSets.append(self.tweets[followee])

        for ts in tweetSets:
            for tweet in ts:
                if len(tenLatestTweets) < 10:
                    heapq.heappush(tenLatestTweets, tweet)
                else:
                    # if current tweet is latest than the oldest tweet in the heap
                    if tweet[0] > tenLatestTweets[0][0]:
                        heapq.heappop(tenLatestTweets)
                        heapq.heappush(tenLatestTweets, tweet)

        feed = [-1] * len(tenLatestTweets)
        for i in range(len(tenLatestTweets) - 1, -1, -1):
            feed[i] = heapq.heappop(tenLatestTweets)[1]
        return feed
