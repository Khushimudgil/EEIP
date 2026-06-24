from celery_app import celery_app


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def process_repository(
    repo_url
):

    print(
        f"Processing {repo_url}"
    )

    return {
        "status": "completed"
    }