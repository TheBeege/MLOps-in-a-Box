import os

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from loguru import logger

from llm_engineering.domain.documents import ArticleDocument

from .base import BaseCrawler


class MediumCrawler(BaseCrawler):
    model = ArticleDocument

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()

        user_agent = os.getenv("USER_AGENT")
        if not user_agent:
            ua = UserAgent()
            user_agent = ua.random

        self.session.headers.update({
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        })

    def extract(self, link: str, **kwargs) -> None:
        old_model = self.model.find(link=link)
        if old_model is not None:
            logger.info(f"Article already exists in the database: {link}")
            return

        logger.info(f"Starting scrapping Medium article: {link}")

        try:
            response = self.session.get(link, timeout=self.timeout)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch article {link}: {e}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find_all("h1", class_="pw-post-title")
        subtitle = soup.find_all("h2", class_="pw-subtitle-paragraph")

        data = {
            "Title": title[0].string if title else None,
            "Subtitle": subtitle[0].string if subtitle else None,
            "Content": soup.get_text(),
        }

        user = kwargs["user"]
        instance = self.model(
            platform="medium",
            content=data,
            link=link,
            author_id=user.id,
            author_full_name=user.full_name,
        )
        instance.save()

        logger.info(f"Successfully scraped and saved article: {link}")
