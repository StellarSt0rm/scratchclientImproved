# **StudioComment**

## Properties

###`#!python id : int` { #id data-toc-label="id" }

The ID of the comment.

###`#!python parent_id : int | None` { #parent_id data-toc-label="parent_id" }

If the comment is a reply, this is the ID of its parent comment. Otherwise, it is `#!python None`.

###`#!python commentee_id : int | None` { #commentee_id data-toc-label="commentee_id" }

If the comment is a reply, this is the user ID of the author of the parent comment. Otherwise, it is `#!python None`.

###`#!python content : str` { #content data-toc-label="content" }

The content of the comment.

###`#!python reply_count : int` { #reply_count data-toc-label="reply_count" }

The number of replies the comment has. If the comment is a reply, this is simply `#!python 0`.

###`#!python author : str` { #author data-toc-label="author" }

The username of the author of the comment.

###`#!python author_id : int` { #author_id data-toc-label="author_id" }

The user ID of the author of the comment.

###`#!python created_timestamp : str` { #created_timestamp data-toc-label="created_timestamp" }

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the date the comment was created.

**Example:**

```python
import datetime

def iso_to_readable(iso):
    timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

    date = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    date.astimezone(timezone)

    return date.strftime("%Y-%m-%d %I:%M %p")

print(session.get_studio(14).get_comments()[0].created_timestamp)
# 2022-08-04 10:47 AM
```

###`#!python last_modified_timestamp : str` { #last_modified_timestamp data-toc-label="last_modified_timestamp" }

An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp representing the date the comment was last modified.

###`#!python visible : bool` { #visible data-toc-label="visible" }

A boolean value representing whether the comment has been deleted or not.

###`#!python studio : Studio` { #studio data-toc-label="studio" }

The studio that the comment is on, as a [Studio](../Studio) object.

## Methods

###`#!python delete()` { #delete data-toc-label="delete" }

Deletes the comment. You must be logged in, the author of the comment, and a manager of the studio that the comment is on for this to not throw an error. Returns an HTTP status code.

**RETURNS** - `#!python int`

**Example:**

```python
studio = session.get_studio(193293231031)
for comment in studio.get_comments(all=True):
  if "scratch" in comment.content:
    comment.delete()
```

###`#!python report()` { #report data-toc-label="report" }

Reports the comment. You must be logged in for this to not throw an error. Returns an HTTP status code.

**RETURNS** - `#!python int`

###`#!python reply(content)` { #reply data-toc-label="reply" }

Replies to the comment. You must be logged in for this to not throw an error. Returns the reply once it is posted as a [StudioComment](../StudioComment).

**PARAMETERS**

- **content** (`#!python str`) - The content of your reply.

**RETURNS** - `#!python StudioComment`

**Example:**

```python
comment = session.get_studio(14).get_comments()[0]
comment.reply("Go away")
```

###`#!python get_replies(all=False, limit=20, offset=0)` { #get_replies data-toc-label="get_replies" }

Gets a list of replies to the comment. Returns an array of [StudioComment](../StudioComment) objects.

**PARAMETERS**

- **all** (`#!python Optional[bool]`) - Whether to retrieve every single reply or just `#!python limit` replies.
- **limit** (`#!python Optional[int]`) - How many replies to retrieve if `#!python all` is `#!python False`.
- **offset** (`#!python Optional[int]`) -  The offset of the replies from the newest ones - i.e. an offset of 20 would give you the next 20 replies after the first 20.

**RETURNS** - `#!python list[StudioComment]`
