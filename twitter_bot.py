import tweepy
from time import sleep

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('',
                      "")

api = tweepy.API(auth)

user = api.me()


def handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        sleep(1)
    except tweepy.TweepError:
        print('Broke from handler loop')
        yield cursor.next()

string = 'a'
counter = 0
for follower in api.followers():
    # temp =
    # sleep(1)
    # temp1 = temp.text
    print(api.home_timeline(follower.id))
    break
    except tweepy.RateLimitError:
        counter += 1
        print(counter)
        continue
    for posts in temp:
        if string in posts.text:
            print(posts.text)
    for tweet in tweepy.Cursor(api.home_timeline).items(2):
        try:
            print(tweet.text)
        except tweepy.TweepError:
            break
        except StopIteration:
            break
        except RuntimeError:
            break

    temp = follower.get_user()
    for post in temp:
        print(post.text)
        break
for follower in api.followers():
    sn = follower.screen_name
    print(follower.get_user(sn))
    break
print(api.followers())
for tweet in tweepy.Cursor(api.search, string).items(5):
    try:

    except tweepy.TweepError:
        break
    except StopIteration:
        break
    except RuntimeError:
        break
