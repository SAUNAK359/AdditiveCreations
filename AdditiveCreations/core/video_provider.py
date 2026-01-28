from abc import ABC, abstractmethod

class VideoProvider(ABC):

    @abstractmethod
    def generate(
        self,
        image_path: str,
        prompt: str,
        duration: int,
        fps: int
    ) -> str:
        pass
