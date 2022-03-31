import unittest
from unemployment_matching_experiment import build_comment_portfolio


def test_build_comment_portfolio(self):
    user_comments = [{"author":"DansThrowaway"}]
    user_comment_data = []
    build_comment_portfolio(user_comments,user_comment_data)
