docker-build:
	docker image build . -t petvibe

docker-run:
	docker run -p 8000:8000 petvibe

midrate:
	alembic upgrade head

create-migration:
	alembic revision --autogenerate -m '${msg}'