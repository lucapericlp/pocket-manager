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

Tag-based tracking - `sr-{N}` where `N` are the number of days from date of
creation for the next review. If `sr-1` & `time_added` is today, then do not emit a notification. If `sr-1` & `time_added` is yesterday, then emit a notification.

- Grab fav'd Pocket entries
- If no tag:
  - no emittance & tag with `sr-1`
- If tag present, check if time has elapsed
  - if yes emit & update to the next expo number of days
  - if no, do nothing
