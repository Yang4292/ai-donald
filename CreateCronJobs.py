from crontab import CronTab
my_cron = CronTab(user='ec2-user')

scrape_headlines = my_cron.new(command='cd /home/ec2-user/environment && /usr/bin/python36 /home/ec2-user/environment/HeadlineScrape.py')
scrape_headlines.hour.every(2)

post_tweet = my_cron.new(command='cd /home/ec2-user/environment && /usr/bin/python36 /home/ec2-user/environment/PostTweet.py')
post_tweet.minute.every(10)

my_cron.write()