# Knowledge Management via Pocket

For the occasions where I'd like to revisit a piece of content but did not enter
it into the [knowledge-garden](https://github.com/lucapericlp/knowledge-garden)
then we can use Pocket.

# Implementation

We have a scheduled Lambda that invokes the Pocket API in order to send a
notification to me for what needs to be reviewed. The notification medium can be
either email or mobile push notification. A consideration for mobile push
notification -> use a Slack bot to ping me directly.

## Logic

- Grab entire Pocket 
