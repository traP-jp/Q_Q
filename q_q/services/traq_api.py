from traq import ApiClient, Configuration
from q_q.core.config import settings

client = ApiClient(Configuration(access_token=settings.api_token))
