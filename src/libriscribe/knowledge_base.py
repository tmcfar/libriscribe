# src/libriscribe/knowledge_base.py
"""
Core knowledge base implementation for LibriScribe.

This module provides the ProjectKnowledgeBase class which manages project metadata
and character information for book writing projects.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class Scene(BaseModel):
    """A scene within a chapter."""

    scene_number: int
    summary: str
    characters: List[str]
    setting: str
    goal: str
    emotional_beat: str


class Chapter(BaseModel):
    """A chapter in the book."""

    chapter_number: int
    title: str
    summary: str
    scenes: List[Scene] = []


class Character(BaseModel):
    """A character in the book project."""

    name: str = "Unnamed Character"
    age: str
    physical_description: str
    personality_traits: str
    background: str
    motivations: str
    relationships: dict
    role: str
    internal_conflicts: str
    external_conflicts: str
    character_arc: str


class ProjectKnowledgeBase(BaseModel):
    """Manages metadata and story information for a book project."""

    project_name: str = ""
    title: str = "Untitled"
    category: str = "fiction"
    genre: str = "Fantasy"
    description: str = "A great story"
    language: str = "en"
    book_length: str = "Novel"
    num_characters: str = "5"
    num_chapters: int = 10
    logline: str = ""
    outline: str = ""
    characters: List[Character] = []
    chapters: dict[int, Chapter] = {}
    project_dir: Optional[str] = None

    def add_chapter(self, chapter: Chapter) -> None:
        """Add a chapter to the knowledge base."""
        self.chapters[chapter.chapter_number] = chapter

    def add_character(self, character: Character) -> None:
        """Add a character to the knowledge base."""
        self.characters.append(character)

    def get_character(self, character_name: str) -> Optional[Character]:
        """Retrieve a character by name."""
        for character in self.characters:
            if character.name == character_name:
                return character
        return None


class Worldbuilding(BaseModel):
    """Worldbuilding information for the book project."""
    
    setting: str = ""
    time_period: str = ""
    geography: str = ""
    culture: str = ""
    technology_level: str = ""
    magic_system: str = ""
    political_structure: str = ""
    economy: str = ""
