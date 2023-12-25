import pytest

from reviveme.db import db
from reviveme.models import Thread, Comment

class TestVoteController:
    @pytest.fixture()
    def thread(self, user) -> Thread:
        thread = Thread(
            author_id=user.id,
            title="Test Thread",
            content="Test Content"
        )

        db.session.add(thread)
        db.session.commit()
        return thread
    
    @pytest.fixture()
    def comment(self, user, thread):
        comment = Comment(
            author_id=user.id,
            thread_id=thread.id,
            content="Test Comment"
        )

        db.session.add(comment)
        db.session.commit()
        return comment

    @pytest.fixture()
    def comment(self, user, thread):
        comment = Comment(
            author_id=user.id,
            thread_id=thread.id,
            content="Test Comment"
        )

        db.session.add(comment)
        db.session.commit()
        return comment
    
    def test_thread_upvote(self, client, user, thread):
        response = client.post(
            f'/api/v1/threads/{thread.id}/upvote',
            json={'user_id': user.id, 'upvote': True}
        )
        assert response.status_code == 200

        response = client.get(f'/api/v1/threads/{thread.id}')
        assert 'score' in response.json
        assert response.json['score'] == 1

    def test_thread_downvote(self, client, user, thread):
        response = client.post(
            f'/api/v1/threads/{thread.id}/downvote',
            json={'user_id': user.id, 'downvote': True}
        )
        assert response.status_code == 200

        response = client.get(f'/api/v1/threads/{thread.id}')
        assert 'score' in response.json
        assert response.json['score'] == -1

    def test_comment_upvote(self, client, user, comment):
        response = client.post(
            f'/api/v1/comments/{comment.id}/upvote',
            json={'user_id': user.id, 'upvote': True}
        )
        assert response.status_code == 200

        response = client.get(f'/api/v1/comments/{comment.id}')
        assert 'score' in response.json
        assert response.json['score'] == 1

    def test_comment_downvote(self, client, user, comment):
        response = client.post(
            f'/api/v1/comments/{comment.id}/downvote',
            json={'user_id': user.id, 'downvote': True}
        )
        assert response.status_code == 200

        response = client.get(f'/api/v1/comments/{comment.id}')
        assert 'score' in response.json
        assert response.json['score'] == -1