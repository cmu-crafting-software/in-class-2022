
def build_comment_portfolio(user_comments,user_comment_data):
    #iterate through all the comments for a given user
    for comment in user_comments:
                user_comment_data.append(
                    [comment.author, comment.created_utc, comment.id, comment.body, comment.subreddit,
                     comment.score, comment.parent_id, comment.is_submitter])
    return user_comment_data